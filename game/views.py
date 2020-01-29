from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from game.models import Game, Player


def dfs(request, pk):
    game = Game.objects.get(pk=pk)
    users = Player.objects.all()
    data = {
        'game': game
    }
    if request.method == 'POST':
        game.dfs = int(request.POST.get('rsp'))
        if game.atk == game.dfs:
            game.result = 3
            for user in users:
                if game.attacker == user.name or game.defender == user.name:
                    user.draw += 1
        elif game.atk - game.dfs == 1 or game.atk - game.dfs == -2:
            game.result = 1
            for user in users:
                if game.attacker == user.name:
                    user.win += 1
                    break
                if game.defender == user.name:
                    user.lose += 1
                    break
        else:
            game.result = 2
            for user in users:
                if game.attacker == user.name:
                    user.lose += 1
                    break
                if game.defender == user.name:
                    user.win += 1
                    break
        game.save()
        return redirect(reverse('dfs_fin', kwargs={'pk': game.pk}))
    return render(request, 'game/dfs.html', data)


def dfs_list(request, username):
    all_game = Game.objects.all()
    games = []
    for game in all_game:
        if game.defender == username and not game.result:
            games.append(game)

    data = {
        "games": games
    }
    return render(request, 'game/dfs_list.html', data)


def dfs_fin(request, pk):
    game = Game.objects.get(pk=pk)
    data = {
        "game": game
    }
    return render(request, 'game/dfs_fin.html', data)

