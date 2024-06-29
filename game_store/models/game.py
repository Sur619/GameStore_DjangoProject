from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=200)
    platform = models.ForeignKey('game_store.Platform', on_delete=models.CASCADE)
    genres = models.ManyToManyField('game_store.Genre')
    publisher = models.ForeignKey('game_store.Publisher', on_delete=models.CASCADE)
    developer = models.OneToOneField('game_store.Developer', on_delete=models.CASCADE)
    release_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.title
