from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import user
from .serializers import user_serializer


from django.http import HttpResponse
# Create your views here.

#here we keep the logic and the function and stuff

def chinadan(request):

    return render(request,'hello.html',{'dic':'Paramashivam'})
    

def bookspirit(request):
    return render(request,'user/book.html')    

#giving one input  manualy and seeing it
@api_view (['GET'])
def getnote(request):
    serializer = user_serializer(data={"note": 3, "date": "hello"})
    serializer.is_valid()  # optional for static data
    return Response(serializer.data)

#to see all the items in the database
@api_view (['GET'])
def getnotes(request):
    notes = user.objects.all() #getting all the data from the model (the DB ) user
    serializer = user_serializer(notes,many = True)
    #serializer.is_valid()  # optional for static data
    return Response(serializer.data)

@api_view(['POST'])
def createnote(request):
    serializer = user_serializer(data = request.data )
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
