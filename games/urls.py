from django.urls import path
from .views import home, Contato, CategoryView


urlpatterns = [
    path("home/", home),
    path("contato/", Contato.as_view()),
    path('api-auth', CategoryView.as_view()),
    
]
