from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.frontpage),
    path('logreg', views.logreg),
    path('specialization/<str:>',views.specialization)
]