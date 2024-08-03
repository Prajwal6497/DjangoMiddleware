from django.shortcuts import render, HttpResponse
from django.template.response import TemplateResponse

# Create your views here.
def home(request):
    print('From View')
    return HttpResponse('This is Home Page')

def excep(request):
    print('View Func')
    res = 10/0
    return HttpResponse('This is Excep View Page')

def user(request):
    print('I am User View')
    data = {'name': 'Prajwal'}
    return TemplateResponse(request, 'blog/user.html', data)
