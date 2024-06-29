from django.db import models

from CourseDjango.game_store.models import Game


class Customer(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    favorite_games = models.ManyToManyField(Game, related_name='fans')

    def __str__(self):
        return self.username