from django.urls import path
from .views import homePageView, home, boilerplate, whats_signup, mapa, missao


urlpatterns = [
    path("home/", home, name="home"),
    path("", home, name="home"),
    path("boilerplate/", boilerplate, name="home"),
    path("whatsapp/", whats_signup, name="whats"),
    path("missao", missao, name="missao"),
]
