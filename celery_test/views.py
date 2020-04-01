from django.shortcuts import render, HttpResponse
from .tasks import test_save



# Create your views here.
def index(request, n=None):
    if n:
        test_save.delay(n)
    return HttpResponse('ok2')    
