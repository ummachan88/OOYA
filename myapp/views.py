from django.shortcuts import render
from django.http import HttpResponse

# def index(request):
   # return HttpResponse('hello')
# Create your views here.
#def home(request):
   #return render (request,'index.html')
def home(request):
   return render (request,'home.html')
