from django.db import models

from CourseDjango.game_store.models import Game


class Discount(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    code = models.CharField(max_length=20, unique=True)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.game} - {self.discount_percentage}% discount ({self.code})"