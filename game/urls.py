from django.urls import path

from game.views import HomeView,MathGameView,AnagramGameView, GameScoreView,record_score


app_name="game"
urlpatterns = [
    path('',HomeView.as_view(),name='homepage'),
    path('math-game/',MathGameView.as_view(),name='math-game'),
    path('anagram-game/',AnagramGameView.as_view(),name='anagram-game'),
    path('record-score/',record_score,name='record-score'),
    path('game-scores/',GameScoreView.as_view(),name='game-scores'),
]
