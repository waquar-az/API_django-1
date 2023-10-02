from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
def home_page(request):
    
    
    
 #   return HttpResponse('<h1>this is home page</h1>')
    return render(request,'home.html')

