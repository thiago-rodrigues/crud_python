from django.conf.urls import url
from . import views


app_name = 'produtos'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^cadastro/$', views.CadastroView.as_view(), name='cadastro'),
    url(r'^listar/$', views.ListaView.as_view(), name='listar'),
    url(r'^excluir/(?P<id_produto>[0-9]+)/$',
        views.ExcluiProduto.as_view(), name='excluir'),
    url(r'^editar/(?P<id_produto>[0-9]+)/$',
        views.EditaProduto.as_view(), name='editar'),
]
