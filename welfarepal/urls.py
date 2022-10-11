from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.frontpage),
    path('home' ,views.home),
    path('reg' , views.LogOrReg),
    path('contactUs' , views.Us),
    
   
]