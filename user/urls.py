from django.urls import path
from . import views

#url config
urlpatterns=[
    path("",views.chinadan),
    path('notes/',views.getnote),
    path('hello/',views.bookspirit),
    path('hello/',views.chinadan),
    path('hello/book/',views.bookspirit)
]