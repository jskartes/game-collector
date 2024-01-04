from django.shortcuts import redirect, render
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from .forms import GameSessionForm
from .models import EventVenue, Game


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
    venue_id_list = game.venues.all().values_list('id')
    excluded_venues = EventVenue.objects.exclude(id__in=venue_id_list)
    session_form = GameSessionForm()
    return render(request, 'games/detail.html', {
        'game': game,
        'session_form': session_form,
        'venues': excluded_venues
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
    fields = ['title', 'players', 'playing_time', 'complexity']
    template_name = 'games/create.html'

class GameUpdate(UpdateView):
    model = Game
    fields = ['title', 'players', 'playing_time', 'complexity']
    template_name = 'games/create.html'

class GameDelete(DeleteView):
    model = Game
    success_url = '/games'

class EventVenueList(ListView):
    model = EventVenue

class EventVenueDetail(DetailView):
    model = EventVenue

class EventVenueCreate(CreateView):
    model = EventVenue
    fields = '__all__'

class EventVenueUpdate(UpdateView):
    model = EventVenue
    fields = '__all__'

class EventVenueDelete(DeleteView):
    model = EventVenue
    success_url = '/venues'

def include_venue(request, game_id, venue_id):
    Game.objects.get(id=game_id).venues.add(venue_id)
    return redirect('games_detail', game_id=game_id)

def exclude_venue(request, game_id, venue_id):
    Game.objects.get(id=game_id).venues.remove(venue_id)
    return redirect('games_detail', game_id=game_id)
