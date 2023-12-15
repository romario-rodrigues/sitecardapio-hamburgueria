from django.db import models

# Create your models here.
class Produto(models.Model):
    descricao = models.TextField(null=False, blank=False)
    preco = models.FloatField(null=False, blank=False)

    def __str__(self):
        return self.descricao