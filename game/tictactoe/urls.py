
from django.urls import path, include
from tictactoe import views


urlpatterns = [
    path('',views.homePage, name='home_page'),
    path('playing/<int:number>/',views.gameIsPlaying, name='game_is_playing'),
    path('savename/',views.saveName, name='save_name'),
    path('clearscore/',views.clearScore, name='clear_score'),
]
