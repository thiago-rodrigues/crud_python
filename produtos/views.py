from django.shortcuts import render, get_object_or_404
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


class EditaProduto(AuthView):

    def get(self, request, id_produto):
        produto = get_object_or_404(Produtos, pk=id_produto)
        return render(request, 'produtos/editar.html', {'produto': produto})

    def post(self, request, id_produto):
        produto = get_object_or_404(Produtos, pk=id_produto)
        produto.nome = request.POST['nome']
        produto.modelo = request.POST['modelo']
        produto.descricao = request.POST['descricao']
        produto.save()
        messages.add_message(request, messages.INFO,
                             'Produto atualizado com sucesso!')
        return HttpResponseRedirect('/produtos/cadastro/')


class ExcluiProduto(AuthView):

    def get(self, request, id_produto):
        produto = get_object_or_404(Produtos, pk=id_produto)
        try:
            produto.delete()
        except (KeyError, produto.DoesNotExist):
            messages.add_message(request, messages.INFO,
                                 'Erro ao excluir produto.')

        return HttpResponseRedirect('/produtos/listar/')
