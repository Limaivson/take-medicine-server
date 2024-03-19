from django.db import models


class Medicamento(models.Model):
    nome = models.CharField(max_length=100)
    quantidade = models.IntegerField()
    horario = models.CharField(max_length=100)
    tomado = models.BooleanField(default=False)

    def __str__(self):
        return self.nome
