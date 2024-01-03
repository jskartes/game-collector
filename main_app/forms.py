from django.forms import ModelForm, DateField
from .models import GameSession


class GameSessionForm(ModelForm):
    class Meta:
        model = GameSession
        fields = ['date', 'playing_time', 'winner']
