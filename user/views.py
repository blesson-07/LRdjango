from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


x=1
y=2
def chinadan(request):
    return render(request,'hello.html',{'dic':'Paramashivam'})
    

def bookspirit(request):
    return render(request,'user/book.html')    
