from django.db import models
from django.urls import reverse


class EventVenue(models.Model):
    name = models.CharField(max_length=100)
    max_players = models.IntegerField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('venues_detail', kwargs={'pk': self.id})
    
    class Meta:
        ordering = ['name']


class Game(models.Model):
    title = models.CharField(max_length=100)
    players = models.CharField(max_length=20)
    playing_time = models.CharField(max_length=100)
    complexity = models.DecimalField(max_digits=3, decimal_places=2)
    venues = models.ManyToManyField(EventVenue)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('games_detail', kwargs={'game_id': self.id})

    class Meta:
        ordering = ['title']


class GameSession(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    date = models.DateField()
    playing_time = models.CharField(max_length=100)
    winner = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.playing_time} {self.game.title} session on {self.date}'
    
    class Meta:
        ordering = ['date']
