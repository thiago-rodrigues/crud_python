from django.shortcuts import render
from login.views import AuthView
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Produtos


class IndexView(AuthView):

    def get(self, request):
        return render(request, 'produtos/index.html')


class CadastroView(AuthView):

    def get(self, request):
        return render(request, 'produtos/cadastro.html')

    def post(self, request):
        novo_produto = Produtos()
        novo_produto.nome = request.POST['nome']
        novo_produto.modelo = request.POST['modelo']
        novo_produto.descricao = request.POST['descricao']
        novo_produto.save()
        messages.add_message(request, messages.INFO,
                             'Produto cadastrado com sucesso!')
        return HttpResponseRedirect('/produtos/cadastro/')


class ListaView(AuthView):

    def get(self, request):
        lista_produtos = Produtos.objects.order_by('nome')
        return render(request, 'produtos/listar.html',
                      {'lista_produtos': lista_produtos})
