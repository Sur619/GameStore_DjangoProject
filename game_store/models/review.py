from django.db import models


class Review(models.Model):
    game = models.ForeignKey('game_store.Game', on_delete=models.CASCADE, related_name='reviews')
    customer = models.ForeignKey('game_store.Customer', on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer} - {self.game} - {self.rating}"
