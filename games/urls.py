from django.urls import path
from games.views import home

urlpatterns = [
    path("home/", home),
]
