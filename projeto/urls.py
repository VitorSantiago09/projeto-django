"""
URL configuration for projeto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from games.views import home, Contato
from games.views import CategoryView
#Aqui importamos a routers pra poder ditar a rota do endpoint da API
from rest_framework import routers


#Registra a rota api-auth como sendo a rota que recebera a CategoryView, sendo onde acontecerá o CRUD
router = routers.DefaultRouter()
router.register('api-auth', CategoryView)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("home/", home),
    path("contato/", Contato.as_view()),
    #Define a rota "" como sendo a rota onde sera renderizada a pagina inicial da api e onde fica o endpoint para que o front possa fazer a requisição
    path('', include(router.urls)),
]


#Isso serve para poder ver a imagem quando clicarmos nela dentro do site.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

