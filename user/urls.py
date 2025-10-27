from django.urls import path
from . import views

#the place that awak function and stuff like is we get into hello/book it will run the function bookscript

#url config
urlpatterns=[
    path("",views.chinadan),
    path('notes/',views.getnote),
    path("notes/<int:pk>",views.user_details),
    path("notes/seeall/",views.getnotes),
    path("notes/create",views.createnote),
    path('hello/',views.bookspirit),
    path('hello/',views.chinadan),
    path('hello/book/',views.bookspirit)
]