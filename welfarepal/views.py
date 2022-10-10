from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages 
from .models import *
import bcrypt

def frontpage(request):
    return render(request,"frontpage")


def logDoc(request):
    email=request.POST['email']
    password=request.POST['password']
    if Doctor.objects.filter(email = email):
        doctor=Doctor.objects.get(email = email)
        if bcrypt.checkpw(password.encode(), doctor.password.encode()): #User.password == password:
            request.session['fname']=doctor.First_Name
            request.session['reglog']=False #False indicates login while True indicates Register
            request.session['userid']=doctor.id
            return redirect("/dashboard")
        else:
            messages.error(request,"password is not valid")
    else:
        messages.error(request,"email is not found")
    return render(request,"LoginRegistration")


def logPatient(request):
    email=request.POST['email']
    password=request.POST['password']
    if Patient.objects.filter(email = email):
        patient=Patient.objects.get(email = email)
        if bcrypt.checkpw(password.encode(), patient.password.encode()): #User.password == password:
            request.session['fname']=patient.First_Name
            request.session['reglog']=False #False indicates login while True indicates Register
            request.session['userid']=patient.id
            return redirect("/dashboard")
        else:
            messages.error(request,"password is not valid")
    else:
        messages.error(request,"email is not found")
    return render(request,"LoginRegistration")


def regPatient(request):
    errors = Patient.objects.Patient_validator(request.POST)
    email=request.POST['email'] 
    if Patient.objects.filter(email = email):
        errors['email1'] = "already existed email address!"
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")

    firstname=request.POST['firstname']
    lastname=request.POST['lastname']
    id=request.POST['ID']
    Gender=request.POST['gender']
    Status=request.POST['marital']
    password=request.POST['password'] 
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode() 
    request.session['fname']= firstname
    request.session['reglog']= True
    patient=Patient.objects.create(First_Name=firstname, Last_Name=lastname, password=pw_hash, Personal_ID=id, Marital_Status=Status, Gender=Gender)
    request.session['Patientid']= patient.id

    return redirect("/dashboard")


def regDoc(request):
    errors = Doctor.objects.Doctor_validator(request.POST)
    email=request.POST['email'] 
    if Doctor.objects.filter(email = email):
        errors['email1'] = "already existed email address!"
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")

    firstname=request.POST['firstname']
    lastname=request.POST['lastname']
    password=request.POST['password'] 
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode() 
    Certificate=request.POST['Certificate']
    Location=request.POST['Location']
    Specialization=request.POST['Specialization']
    MedicalNumber=request.POST['id']
    Experience=request.POST['Experience']
    Phone_Number=request.POST['Phone_Number']
    request.session['fname']= firstname
    request.session['reglog']= True
    thisDoctor=Doctor.objects.create(fname=firstname,lname=lastname,email=email,password=pw_hash,MedicalNumber=MedicalNumber,Certificate=Certificate,Location=Location,Specialization=Specialization,Experience=Experience,Phone_Number=Phone_Number)
    request.session['Doctorid']= thisDoctor.id

    return redirect("/dashboard")





