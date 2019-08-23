from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def hi(request):
    return render(request, 'home.html',{'name': 'Murali..'} )
    # return HttpResponse('Hello World')

def add(request):

    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    res = val1 + val2

    return render(request, 'result.html', {'result':res, 'number1': val1, 'number2':val2})