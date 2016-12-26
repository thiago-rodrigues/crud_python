from django.conf.urls import url
from . import views


app_name = 'produtos'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^cadastro/$', views.CadastroView.as_view(), name='cadastro')
]
