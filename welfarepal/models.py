from django.db import models
import re

class DrManager(models.Manager):
    def Doctor_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['firstname']) < 2:
            errors["firstname"] = "first name should be at least 2 characters"


        if len(postData['lastname']) < 2:
            errors["lastname"] = "last name should be at least 2 characters"


        if not postData['file'] :
            errors["certificate"] = "certificate was not uploaded"

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['email'] = "Invalid email address!"

        if len(postData['ID']) != 8:
            errors["desc"] = "Your ID does not seem to be correct"

        if len(postData['password']) < 8:
            errors["desc"] = "password should be at least 8 characters"

        if postData['password']!=postData['cpassword']:
            errors["password"] = "Password and its confirmation does not match"   

        return errors

class PatientManager(models.Manager):
    def Patient_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['firstname']) < 2:
            errors["firstname"] = "first name should be at least 2 characters"


        if len(postData['lastname']) < 2:
            errors["lastname"] = "last name should be at least 2 characters"


        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['email'] = "Invalid email address!"

        if len(postData['ID']) != 8:
            errors["desc"] = "Your ID does not seem to be correct"

        if len(postData['password']) < 8:
            errors["desc"] = "password should be at least 8 characters"

        if postData['password']!=postData['cpassword']:
            errors["password"] = "Password and its confirmation does not match"   

        return errors



class Doctor(models.Model):
    First_Name = models.CharField(max_length=45)
    Last_Name = models.CharField(max_length=45)
    password=models.CharField(max_length=255)
    Certificate = models.CharField(max_length=45)
    Location = models.CharField(max_length=45)
    Specialization = models.CharField(max_length=45)
    Experience = models.DateTimeField()
    Phone_Number = models.IntegerField()
    MedicalNumber=models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=DrManager()


class Patient(models.Model):
    First_Name = models.CharField(max_length=45)
    Last_Name = models.CharField(max_length=45)
    password=models.CharField(max_length=255)
    Personal_ID = models.CharField(max_length=45)
    Marital_Status = models.CharField(max_length=45)
    Gender = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=PatientManager()
    #

class Profile(models.Model):
    Diagnosis=models.CharField(max_length=45)
    Medicines=models.CharField(max_length=45)
    Description=models.CharField(max_length=45)
    Examinations=models.FileField()
    patient = models.ForeignKey(Patient, related_name="profiles", on_delete = models.CASCADE)
    doctor = models.ForeignKey(Doctor, related_name="profiles", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Appointments(models.Model):
    vacancies=models.DateTimeField()
    clinic=models.CharField(max_length=45)
    clinic_phone=models.IntegerField()
    patient = models.ForeignKey(Patient, related_name="appointments", on_delete = models.CASCADE)
    doctor = models.ForeignKey(Doctor, related_name="appointments", on_delete = models.CASCADE)    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)