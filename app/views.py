from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from app.crud import Crud


def login(request):

    return render (request,'login.html')


def entrar(request):
    data={}
    data['projeto'] = 'OliotaFlix'

    login = request.GET.get('login_email', '')
    senha = request.GET.get('login_senha', '')
    tabela = Crud(
        user='postgres',
        password='postgres',
        host='127.0.0.1',
        dbname='MariaFlix',
        table='usuarios',
        port='5432',
        primarykey='login'
    )
    tabela.connect()
    usuario = tabela.find(primaryKey_value=login)
    if usuario is None:
        data['erro']='Usuario não encontrado'
        return render(request, 'login.html',data)
    else:
        if usuario[0]['senha'] != senha:
            data['erro'] = 'Senha incorreta'
            return render(request, 'login.html',data)
        else:
            data['usuario']= usuario


    #context ={'usuario': usuario[0]['login']}#ler de um dict
    #context ={'usuario': tabela.select_all_json()}
    return render (request, 'home.html', data)
