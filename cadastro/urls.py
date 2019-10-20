from django.urls import path
from .views import cadastro


urlpatterns = [
    path("home/cadastro/", cadastro, name="cadastro"),

]