from django.shortcuts import redirect, render
from django.views.generic import CreateView, DeleteView, UpdateView
from .forms import GameSessionForm
from .models import Game


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def games_index(request):
    games = Game.objects.all()
    return render(request, 'games/index.html', {
        'games': games
    })

def games_detail(request, game_id):
    game = Game.objects.get(id=game_id)
    session_form = GameSessionForm()
    return render(request, 'games/detail.html', {
        'game': game,
        'session_form': session_form
    })

def add_session(request, game_id):
    form = GameSessionForm(request.POST)
    if form.is_valid():
        new_session = form.save(commit=False)
        new_session.game_id = game_id
        new_session.save()
    return redirect('games_detail', game_id=game_id)

class GameCreate(CreateView):
    model = Game
    fields = '__all__'
    template_name = 'games/create.html'

class GameUpdate(UpdateView):
    model = Game
    fields = '__all__'
    template_name = 'games/create.html'

class GameDelete(DeleteView):
    model = Game
    success_url = '/games'
