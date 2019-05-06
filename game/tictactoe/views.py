from django.shortcuts import render
from tictactoe import models
from tictactoe.ticAI import *

# Create your views here.


Tic = {'player': '', 'computer_score':0, 'player_score':0, 'win':'',
        'Tic':theBoard, 'info': info,}


# This asign stuff into the database
def saveName(request):
    Tic['player'] = request.POST['username']
    return render(request, 'tictactoe/TttTemplate.html',{'Tic':Tic})

# This displays the homepage
def homePage(request):
    global Tic
    Tic = {'player': '', 'computer_score':0, 'player_score':0, 'win':'',
        'Tic':theBoard, 'info': info,}
    return render(request, 'tictactoe/base.html',{'Tic':Tic})

    
def gameIsPlaying(request,number):
    Tic['Tic'] = mainGame(number)
    win = Winner()
    Tic['win'] = ''
    if win == 'X':
        Tic['player_score'] +=1
        Tic['win'] = win
    elif win == 'O':
        Tic['computer_score'] +=1
        Tic['win'] = win
    return render(request, 'tictactoe/TttTemplate.html',{'Tic':Tic})

def clearScore(request):
    Tic['player_score'] = 0
    Tic['computer_score'] = 0
    return render(request, 'tictactoe/TttTemplate.html',{'Tic':Tic})