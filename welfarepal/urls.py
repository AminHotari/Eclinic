from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.frontpage),
    path('home' ,views.home),
    path('reg' , views.LogOrReg),
    path('contactUs' , views.Us),
    path('regestire1' , views.regPatient),
    path('regestire2' , views.regDoc),
    path('DoctorDash/<id>' , views.DoctorDash),
    path('patientDash/<id>' , views.PatientDash),
    path('login' , views.logDocAndPatient),
    path('logoutPatient' , views.logoutP),
    path('logoutDoctor' , views.logoutD)
    
   
]