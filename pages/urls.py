from django.urls import path
from .views import homePageView, home, boilerplate, whats_signup, cadastro, mapa, missao


urlpatterns = [
    path("home/", home, name="home"),
    path("", home, name="home"),
    path("whatsapp/", whats_signup, name="whats"),
    path("cadastro/", cadastro, name="cadastro"),
    path("map", mapa, name="mapa"),
    path("missao", missao, name="missao"),


]
