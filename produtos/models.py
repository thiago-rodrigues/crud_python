from __future__ import unicode_literals
from django.db import models
from django.forms import ModelForm


class Produtos(models.Model):
    nome = models.CharField(max_length=200)
    modelo = models.CharField(max_length=200)
    descricao = models.CharField(max_length=200)

    def __str__(self):
        return self.nome


class ProdutoForm(ModelForm):

    class Meta:
        model = Produtos
        fields = ['nome', 'modelo', 'descricao']
