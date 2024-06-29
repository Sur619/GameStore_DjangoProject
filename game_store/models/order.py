from django.db import models

from CourseDjango.game_store.models import Customer, Game


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer} - {self.game} - {self.order_date}"
