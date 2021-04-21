from django.urls import path
from .views import *
# this is the views.py file within this directory

urlpatterns = [
    path("", index, name="index"),
    path('show/<str:name>', show, name="show")
]
