from django.views.generic import TemplateView
import json
from django.http import JsonResponse
from game.models import GameScore

class HomeView(TemplateView):
    template_name = "home.html"
class MathGameView(TemplateView):
    template_name = "math-game.html"
class AnagramGameView(TemplateView):
    template_name = "anagram-game.html"
    def dispatch(self, request, *args, **kwargs):
        print("AnagramGameView is loading")
        return super().dispatch(request, *args, **kwargs)
class GameScoreView(TemplateView):
    template_name = "games-score.html"
    def get_context_data(self, **kwargs):
        context = super(GameScoreView, self).get_context_data(**kwargs)
        context['anagram_scores'] = GameScore.objects.filter(game__exact='ANAGRAM').order_by('-score')
        context['math_scores'] = GameScore.objects.filter(game__exact='MATH').order_by('-score')
        return context

def record_score(request):
    data = json.loads(request.body)
    user_name = data.get('user_name')
    game = data.get('game')
    score = data.get('score')

    new_score = GameScore.objects.create(
                user_name=user_name,
                game=game,
                score=score
            )
    new_score.save()
    
    response = {
        "success":True
    }

    return JsonResponse(response)

