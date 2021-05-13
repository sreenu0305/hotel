from boto import auth
from boto.gs.user import User
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from reciepe.models import Reciepe
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def login_page(request):
    return render(request, 'reciepe/login.html')


def register(request):
    return render(request, 'reciepe/register.html')


def savedetails(request):
    User.objects.raw('create user(username vachar(40),password varchar(30),email varchar(50))')
    # User.objects.create_user(username=request.POST['username'], password=request.POST['password'],
    #                          email=request.POST['email'])
    return HttpResponseRedirect('/reciepe/')


def validate(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect('/reciepe/list/')

    else:
        return HttpResponse("<html><h1>invalid username or password </h1></html>")


def list(request):
    # reciepies = Reciepe.objects.all()
    reciepies = Reciepe.objects.raw('select * from reciepe_reciepe')
    return render(request, 'reciepe/list.html', {'reciepe': reciepies})


def save(request):
    # Reciepe.objects.raw('create('reciepe_name varchar(40),ingridiants varchar(200),process varchar(200),images varchar)')
    Reciepe.objects.create(reciepe_name=request.POST['name'], ingridiants=request.POST['ingridiants'],
                           process=request.POST['process'], images=request.FILES['image'])
    return HttpResponseRedirect('/reciepe/list/')


def create(request):
    return render(request, 'reciepe/create.html')


def details(request, id):
    user = request.user
    reciepe=Reciepe.objects.raw('select * from reciepe_reciepe where id=id')
    # reciepe = Reciepe.objects.get(id=id)
    return render(request, 'reciepe/details.html', {'reciepe': reciepe, 'user': user})


def delete(request, id):
    Reciepe.objects.raw('delete from reciepe_reciepe where id=id')
    Reciepe.objects.get(id=id).delete()
    return HttpResponseRedirect('/reciepe/list/')


def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/reciepe/')
