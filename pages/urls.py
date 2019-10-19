from django.urls import path
from .views import homePageView, home, boilerplate


urlpatterns = [
    path("home/", home, name="home"),
    path("", home, name="home"),
    path("boilerplate/", boilerplate, name="home"),

]
