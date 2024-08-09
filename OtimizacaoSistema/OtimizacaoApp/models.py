from django.db import models

# Create your models here.

class Produto(models.Model):
    tipo = models.CharField(max_length=100, null=False, blank=False)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    sexo = models.CharField(max_length=1, null=True, blank=True)
    tamanho = models.CharField(max_length=3, null=False, blank=False)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.tipo

