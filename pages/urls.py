from django.urls import path
from .views import homePageView, home, boilerplate, mapa, missao


urlpatterns = [
    path("home/", home, name="home"),
    path("", home, name="home"),
    path("boilerplate/", boilerplate, name="home"),
    path("map", mapa, name="mapa"),
    path("home/map", mapa, name="mapa"),
    path("missao", missao, name="missao"),
    path("home/missao", missao, name="missao")

]
