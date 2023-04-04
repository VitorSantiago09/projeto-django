from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    #Isso tira a nomenclatura padrão do nome da tabela que vem no admin do django quando criamos uma coluna. Com isso o nome da coluna vem com o nome que selecionamos.
    def __str__(self):
        return self.name

#Cada Model será uma tabela dentro do nosso banco de dados
class Jogo(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    genero = models.CharField(max_length=50)
    nota_metracritic = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    capa_jogo = models.ImageField(upload_to='games/covers')
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True
    )
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )
    def __str__(self):
        return self.titulo

#Podemos usar o django shell para fazer testes de inserção nas nossas tabelas.
