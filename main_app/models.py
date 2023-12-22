from django.db import models
from django.urls import reverse


class Game(models.Model):
    title = models.CharField(max_length=100)
    players = models.CharField(max_length=20)
    playing_time = models.CharField(max_length=100)
    complexity = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('games_detail', kwargs={'game_id': self.id})

    class Meta:
        ordering = ['title']
