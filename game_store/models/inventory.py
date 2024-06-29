from django.db import models

class Inventory(models.Model):
    game = models.OneToOneField('game_store.Game', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.game} - {self.quantity} available at {self.price}"
