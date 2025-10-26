from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import user
from .serializers import user_serializer


from django.http import HttpResponse
# Create your views here.


def chinadan(request):
    return render(request,'hello.html',{'dic':'Paramashivam'})
    

def bookspirit(request):
    return render(request,'user/book.html')    

@api_view (['GET'])
def getnote(request):
    serializer = user_serializer(data={"note": 3, "date": "hello"})
    serializer.is_valid()  # optional for static data
    return Response(serializer.data)