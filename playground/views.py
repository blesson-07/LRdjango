from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


x=1
y=2
def hello(request):
    return render(request,'hello.html',{'dic':'Paramashivam'})