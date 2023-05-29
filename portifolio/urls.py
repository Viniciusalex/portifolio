from django.contrib import admin
from django.urls import path
from portifolio.views import index, sobreMim, apresentacao, conteudo


urlpatterns = [
    path('apresentacao', apresentacao, name='apresentacao'),
    path('sobreMim', sobreMim, name='sobreMim'),
    path('', index, name='index'),
    path('conteudo', conteudo, name='conteudo'),
]
