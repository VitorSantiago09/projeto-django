from django.shortcuts import render
from django.http import HttpResponse
from games.models import Jogo
from django.views.generic import TemplateView 


#Teste function based views
def home(request):
    #jogos = Jogo.objects.all()
    return render(request, 'games/pages/home.html')


# Create your views here.

#Teste de class based views
class Contato(TemplateView):
    template_name = "games/pages/contato.html"
