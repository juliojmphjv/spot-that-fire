from django.urls import path
from .views import homePageView, HelloWord


urlpatterns = [
    path("", HelloWord, name="home")


]
