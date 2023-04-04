from django.contrib import admin
from games.models import Category, Jogo

# Register your models here.

#Registramos os models aqui para que eles apareçam na parte de admin do django para futuras edições

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Jogo)
class JogosAdmin(admin.ModelAdmin):
    pass

