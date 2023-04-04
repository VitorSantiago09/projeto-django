from django.urls import path
from .views import home, Contato


urlpatterns = [
    path("home/", home),
    path("contato/", Contato.as_view())
]
