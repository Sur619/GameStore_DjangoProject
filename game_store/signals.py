from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User

from game_store.models import Order, Customer, Discount, Review, Game
from game_store.tasks import send_telegram_notification, create_order_telegram_notification, write_stock_to_google_sheets

# Deactivate related models when a User is deleted

@receiver(post_delete, sender=User)
def deactivate_related_customers(sender, instance, **kwargs):
    # Get all customers associated with the deleted user and mark them as inactive
    related_customers = Customer.objects.filter(user=instance)
    related_customers.update(is_active=False)


@receiver(post_delete, sender=User)
def deactivate_related_objects(sender, instance, **kwargs):
    # Get all customers associated with the deleted user and mark them as inactive
    related_customers = Customer.objects.filter(user=instance)
    related_customers.update(is_active=False)

    # Get all orders associated with the deleted user and mark them as inactive
    related_orders = Order.objects.filter(customer__user=instance)
    related_orders.update(is_active=False)

    # Mark the user as inactive instead of deleting it
    instance.is_active = False
    instance.save()

# Create and update notifications for Discounts

@receiver(post_save, sender=Discount)
def create_discount_telegram_notification(sender, instance, created, **kwargs):
    if created:
        # Fetching all developers associated with the discount
        developer = instance.game.developer
        chat_id = developer.telegram_chat_id
        text = (f"New Discount {instance.code} has been created for {instance.game.title}."
                f"\nDiscount: {instance.discount_percentage}%"
                f"\nStart Date: {instance.start_date}"
                f"\nEnd Date: {instance.end_date}")
        send_telegram_notification.delay(chat_id, text)

@receiver(post_save, sender=Discount)
def update_discount_telegram_notification(sender, instance, created, **kwargs):
    if not created:
        developer = instance.game.developer
        chat_id = developer.telegram_chat_id
        text = (f"Discount {instance.code} for {instance.game.title} has been updated."
                f"\nDiscount: {instance.discount_percentage}%"
                f"\nStart Date: {instance.start_date}"
                f"\nEnd Date: {instance.end_date}")
        send_telegram_notification.delay(chat_id, text)

# Create and update notifications for Reviews

@receiver(post_save, sender=Review)
def create_review_telegram_notification(sender, instance, created, **kwargs):
    if created:
        # Fetching the customer associated with the review
        customer = instance.customer
        chat_id = customer.telegram_chat_id
        text = (f"New review created for {instance.game.title} by {instance.customer.username}."
                f"\nRating: {instance.rating}"
                f"\nComment: {instance.comment}")
        send_telegram_notification.delay(chat_id, text)

@receiver(post_save, sender=Review)
def update_review_telegram_notification(sender, instance, created, **kwargs):
    if not created:
        customer = instance.customer
        chat_id = customer.telegram_chat_id
        text = (f"Review for {instance.game.title} by {instance.customer.username} has been updated."
                f"\nRating: {instance.rating}"
                f"\nComment: {instance.comment}")
        send_telegram_notification.delay(chat_id, text)

# Create order notifications

@receiver(post_save, sender=Order)
def send_create_order_telegram_notification(sender, instance: Order, created, **kwargs):
    if created:
        create_order_telegram_notification.apply_async((instance.id,), countdown=10)

@receiver(post_save, sender=Order)
def update_order_telegram_notification(sender, instance, created, **kwargs):
    if not created:
        customer = instance.customer
        chat_id = customer.telegram_chat_id
        text = f"Order {instance.id} has been updated for {instance.game.title}.\nPlease review the changes."
        send_telegram_notification.delay(chat_id, text)
