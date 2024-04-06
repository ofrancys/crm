from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now 

# Create your models here.

class Cliente(models.Model):
    cnpj = models.CharField(max_length=18)
    razao_social = models.CharField(max_length=96)
    name = models.CharField(max_length=96)
    number = models.CharField(max_length=96)
    date_lastsell = models.DateField(default=now)
    #sell = models.BooleanField()
    #class Meta:
        #ordering: ['-date']

class Pedido(models.Model):
    representada = models.CharField(max_length=18)
    valor_frete = models.FloatField(max_length=96)
    valor_itens = models.FloatField(max_length=96)
   

