#from django.shortcuts import render
from django.http import HttpResponse
#from symbol import return_stmt

def index(request):
    return HttpResponse('Главная страница')

def group_posts(request, group):
    return HttpResponse(f'Текущая группа {group}')
