from django.urls import path
from .views import  home, mapa, missao
from .views import home, whats_signup, missao, estatistica


urlpatterns = [
    path("home/", home, name="home"),
    path("", home, name="home"),
    path("map", mapa, name="mapa"),
    path("whatsapp/", whats_signup, name="whats"),
    path("missao/", missao, name="missao"),
    path("estatistica/", estatistica, name="estatistica")
]
