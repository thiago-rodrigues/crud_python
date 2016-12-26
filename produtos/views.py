from django.shortcuts import render
from django.views import View
from login.views import AuthView


class IndexView(AuthView):

    def get(self, request):
        return render(request, 'produtos/index.html')


class CadastroView(AuthView):

    def get(self, request):
        return render(request, 'produtos/cadastro.html')
