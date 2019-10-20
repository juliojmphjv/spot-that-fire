from django.db import models

# Create your models here.

class Usuarios(models.Model):

    nome = models.CharField(max_length=255, blank=False)
    telefone = models.CharField(max_length=22, blank=False)
    email = models.EmailField(max_length=90, blank=False)
    cep = models.CharField(max_length=50, blank=False)
    cidade = models.CharField(max_length=100, blank=False)
    iptu = models.CharField(max_length=100, blank=False)