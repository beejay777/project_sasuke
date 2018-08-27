from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    name = "Uchiha Sasuke"

    return render(request, 'base.html', context={"name": name})
