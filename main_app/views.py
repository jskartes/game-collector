from django.shortcuts import render


games = [
    {
        'title': 'Arkham Horror LCG',
        'players': '1-2+',
        'playing_time': '60-120 min',
        'complexity': 3.53
    },
    {
        'title': 'Gloomhaven',
        'players': '1-4',
        'playing_time': '60-120 min',
        'complexity': 3.9
    },
    {
        'title': 'War of the Ring',
        'players': '2-4',
        'playing_time': '120 min',
        'complexity': 3.84
    }
]


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def games_index(request):
    return render(request, 'games/index.html', {
        'games': games
    })
