from multiprocessing import context
from tokenize import Special
from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages 
from .models import *
import bcrypt

def frontpage(request):
    return render(request,"MainPage.html")


def logDocAndPatient(request):
    email=request.POST['email']
    password=request.POST['password']
    if email in Doctor.objects.email.all():
        if Doctor.objects.filter(email = email):
            doctor=Doctor.objects.get(email = email)
            if bcrypt.checkpw(password.encode(), doctor.password.encode()): #dr.password == password:
                request.session['fname']=doctor.First_Name
                request.session['reglog']=False #False indicates login while True indicates Register
                request.session['drid']=doctor.id
                return redirect("/dashboard")
            else:
                messages.error(request,"password is not valid")
    elif email in Patient.objects.email.all():
        if Patient.objects.filter(email = email):
            patient=Patient.objects.get(email = email)
            if bcrypt.checkpw(password.encode(), patient.password.encode()): #patient.password == password:
                request.session['fname']=patient.First_Name
                request.session['reglog']=False #False indicates login while True indicates Register
                request.session['patientid']=patient.id
                return redirect("/dashboard")
            else:
                messages.error(request,"password is not valid")
        else:
            messages.error(request,"email is not found")
        return render(request,"LoginRegistration")
    else:
            messages.error(request,"email is not found")
            return render(request,"LoginRegistration")

# Patient Registration 
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
    age=request.POST['age']
    password=request.POST['password'] 
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode() 
    request.session['firstname']= firstname
    request.session['reglog']= True
    patient=Patient.objects.create(First_Name=firstname, Last_Name=lastname,email=email, password=pw_hash, Personal_ID=id, Marital_Status=Status, Gender=Gender)
    request.session['patientid']= patient.id ###
    return redirect("/patientdashboard")

# Dr Registration 
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
    request.session['firstname']= firstname
    request.session['reglog']= True
    thisDoctor=Doctor.objects.create(firstname=firstname,lname=lastname,email=email,password=pw_hash,MedicalNumber=MedicalNumber,Certificate=Certificate,Location=Location,Specialization=Specialization,Experience=Experience,Phone_Number=Phone_Number)
    request.session['drid']= thisDoctor.id
    return redirect("/drdashboard")

    
def specialization(request,special):
    locations=Doctor.objects.Location.all()
    thislocation=request.POST['location']
    doctors=Doctor.objects.filter(Specialization=special,Location=thislocation)
    context={
        'drs':doctors,
        'locations':locations
    }
    return render(request,"specialization.html",context)

def appointments(request):
    thisdoctor=Doctor.objects.get(id=request.session['drid'])
    myappointments=appointments.objects.filter(doctor=thisdoctor)
    context={
        'myappointments':myappointments
    }
    return render(request,"dr_dashboard.html",context)

def pappointments(request):
    thispatient=Patient.objects.get(id=request.session['patientid'])
    myappointments=appointments.objects.filter(patient=thispatient)
    context={
        'myappointments':myappointments
    }
    return render(request,"patient_dashboard.html",context) 

def profile(request,id):
    thisdoctor=Doctor.objects.get(id=request.session['drid'])
    drs=Doctor.objects.filter(Specialization=thisdoctor.Specialization)
    thispatient=Patient.objects.get(id=id)
    profile=thispatient.Profile.filter(doctor=drs)    #We used a filter based on array of doctors with specific specialization error might happen
    context={
        'profile':profile
    }
    return render(request,"patientprofile.html",context)