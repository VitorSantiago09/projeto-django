from unicodedata import category
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

#Cada Model será uma tabela dentro do nosso banco de dados
class Jogos(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    genero = models.CharField(max_length=50)
    nota_metracritic = models.IntegerField()
    capa_jogo = models.ImageField(upload_to='games/covers')
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True
    )
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )

