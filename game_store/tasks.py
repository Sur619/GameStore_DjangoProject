from celery import shared_task


from game_store.models import Order, Customer, Review, Discount, Game
from google_sheets.api import write_to_sheet

from telegram.client import send_message


@shared_task
def write_stock_to_google_sheets():
    write_to_sheet('Sheet1', 'A1')

@shared_task
def send_telegram_notification(chat_id, text):
    # This function will be executed asynchronously by Celery
    send_message(chat_id, text)

@shared_task
def create_order_telegram_notification(order_id):
    order = Order.objects.get(id=order_id)
    vendor_staff_list = Customer.objects.filter(id=order.customer.id)
    for vendor_staff in vendor_staff_list:
        chat_id = vendor_staff.telegram_chat_id
        text = f"New order {order.id} has been created. \nPlease proceed to a packing area."
        send_message(chat_id, text)
