from django.shortcuts import render
from django.views.generic import TemplateView 

# Create your views here.

#Teste function based views
def home(request):
    #jogos = Jogo.objects.all()
    return render(request, 'games/pages/home.html')


#Teste de class based views
class Contato(TemplateView):
    template_name = "games/pages/contato.html"
