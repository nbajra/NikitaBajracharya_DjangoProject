from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    #name = "Nikita Bajracharya"
    return render(request, 'index.html',{})
