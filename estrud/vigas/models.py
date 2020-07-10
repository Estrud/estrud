from django.db import models


class Viga(models.Model):
    description = models.CharField(max_length=255)
    b = models.DecimalField(max_digits=5, decimal_places=2)
    h = models.DecimalField(max_digits=5, decimal_places=2)
    d = models.DecimalField(max_digits=5, decimal_places=2)
    d_linha = models.DecimalField(max_digits=5, decimal_places=2)
    limites = models.CharField(max_length=5)
    concreto = models.CharField(max_length=5)
    aco = models.CharField(max_length=5)
    esforco = models.DecimalField(max_digits=5, decimal_places=2)
    gama_f = models.DecimalField(max_digits=2, decimal_places=1)

    def __str__(self):
        return self.description
