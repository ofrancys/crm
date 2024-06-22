from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now 

class Cliente(models.Model):
    cnpj = models.CharField(max_length=96)
    razao_social = models.CharField(max_length=96)
    name = models.CharField(max_length=96)
    number = models.CharField(max_length=96)
    date_lastsell = models.DateField(default=now)

class Pedido(models.Model):
    representada = models.CharField(max_length=18)
    valor_frete = models.FloatField(max_length=96)
    valor_itens = models.FloatField(max_length=96)
   
class Produto(models.Model):
    cod = models.CharField(max_length=18)
    descricao = models.CharField(max_length=96)
    medida = models.CharField(max_length=96)
    quantidade = models.FloatField(max_length=18)
    vlr_un = models.FloatField(max_length=96)
    vlr_total = models.FloatField(max_length=96)

class Representada(models.Model):
    cnpj = models.CharField(max_length=18)
    razao = models.CharField(max_length=96)
    contato = models.CharField(max_length=96)
    numero = models.FloatField(max_length=18)
    endereco = models.CharField(max_length=96)

class Representante(models.Model):
    cnpj = models.BigIntegerField()
    cpf = models.BigIntegerField()
    fullName = models.CharField(max_length=96)
    numero = models.IntegerField()
    endereco = models.CharField(max_length=96)
    vendas = models.FloatField(max_length=18)
    ticket = models.FloatField(max_length=96)
    totalVendas = models.FloatField(max_length=18)
   