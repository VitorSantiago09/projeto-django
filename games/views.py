from django.shortcuts import render
from django.views.generic import TemplateView      
from games.models import Category
from games.serializer import CategorySerializer

#Campos que importam o rest framework para o projeto
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

#Teste function based views
def home(request):
    #jogos = Jogo.objects.all()
    return render(request, 'games/pages/home.html')


#Teste de class based views
class Contato(TemplateView):
    template_name = "games/pages/contato.html"


class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    #Torna obrigatorio a autenticação do usuario
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    #filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    #ordering_fields = ['name']
    #search_field = ['name']
    #filterset_fields = ['name']

