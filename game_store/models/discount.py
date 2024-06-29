from django.db import models

class Discount(models.Model):
    game = models.ForeignKey('game_store.Game', on_delete=models.CASCADE)
    code = models.CharField(max_length=20, unique=True)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.game} - {self.discount_percentage}% discount ({self.code})"
