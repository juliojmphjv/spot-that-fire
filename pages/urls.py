from django.urls import path
from .views import home, whats_signup, missao


urlpatterns = [
    path("home/", home, name="home"),
    path("", home, name="home"),
    path("whatsapp/", whats_signup, name="whats"),
    path("missao", missao, name="missao"),
]
