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
#Aqui importamos a routers pra poder 
from rest_framework import routers

from games.views import CategoryView

router = routers.DefaultRouter()
router.register('api-auth', CategoryView)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("home/", home),
    path("contato/", Contato.as_view()),
    path('', include(router.urls)),
]

#Isso serve para poder ver a imagem quando clicarmos nela dentro do site.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
