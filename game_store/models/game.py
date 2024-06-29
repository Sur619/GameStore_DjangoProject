from django.db import models

from CourseDjango.game_store.models import Platform, Genre, Publisher, Developer


class Game(models.Model):
    title = models.CharField(max_length=200)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    genres = models.ManyToManyField(Genre)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    developer = models.OneToOneField(Developer, on_delete=models.CASCADE)
    release_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.title