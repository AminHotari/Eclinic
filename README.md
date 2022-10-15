# **IPEKYOLU** 

## Table of Contents
* [Run Localy](#run-localy)
* [Abstract](#abstract)
* [Main Page](#main-page)
* [Home Page](#home-page)
* [Contact Us Page](#contact-us-page)
* [Login and Registration](#login-and-registration)
* [Doctor Dashboard Page](#doctor-dashboard-page)
* [Patient Dashboard Page](#patient-dashboard-page)
* [CheckBox Page](#checkbox-page)
* [Patient Diagnosis Page](#patient-diagnosis-page)
* [Specialize Page](#specialize-page)
* [Available Appointments Page](#available-appointments-page)
* [Technologies Used](#technologies-used)
* [Done by](#done-by)
* [Superviser](#superviser)

## Run Localy

```python manage.py runserver``` then navigate to  [127.0.0.1:8000](https://localhost:8000).
## **Abstract:**
#### *Our project is a website for booking online to clinic and a doctor that will make it easy for the patient to navigate through different clinics that are in website.The website navegation bar contains Home, Registration, Login, and Contact Us. After choose the clinic, the patient can see all doctors are in it with each free time for each doctor that mentioned by a doctor .The patients can add an appointment if they log in.They will also have the chance to knew their diagnosis ,and they also have the chance to cancel any appointment (AJAX working in this button).The doctors have to update diagnosis of patient in the patient diagnosis page to knew the status diagnosis of that patient. All the pages in our website aregoing to be responsive.*
## Main Page:
* Features:
     *  Mainpage have a navigation bar contains a route to (Home),(Registration), (Login), and (Contact Us).
     *  Users are able to see what clinics avilable in website, if they press on home on top of the navigation bar.
     *  Users are able to contact us, if they press on contact us on top of the navigation bar.
   ### Main Page Preview:
   ![play]
## Home Page:
* Features:
     *  Display types of clinics in our website.
     *  Users are able to see what a doctors had a free time , if they press on book here button.
     *  Homepage have a navigation bar contains a route to (Registration), (Login), and (Contact Us). 
   ### Home Page Preview:
   ![1]()
   
## Contact Us Page:
* Features:
     *  Display our contacts.
     * Contactuspage have a navigation bar contains a route to (Home) (Registration), and (Login).
   ### Contact Us Preview:
   ![1]()

## Login and Registration:
* Features
    *	Users are able to register:
    *	Users will not be able to register with two different accounts with same email.
    *	Username must contain 2 characters at least.
    *	Password must contain at least 8 characters.
    *	Passwords are encrypted.
    *	Validations are done in real time
    *	User information are saved in session, so they don’t need to log in again.
    * User will be able to login.
    *	User is only able to login with a valid password and email.
    *	User should be saved in session when registered successfully.
  ### Login/Register Preview
  ![3]()
  
## Doctor Dashboard Page:
* Features
   * The doctor dashboard page can be viewed when a doctor login.
   * The doctor dashboard page include an appointments that doctor have. 
   * If doctor click on confirm that mean he is confirm the appointment.
   * Edit button send to a page let doctor add which time free for him.
   * If doctor click on show send him to patient diagnosis page who's make an appointment. 
   * Logout button redirect to main page.  
  ### Doctor Dashboard Preview
  ![2]()
## Patient Dashboard Page:
* Features
   * The patient dashboard page can be viewed when a patient login.
   * The patient dashboard page include an appointments that patient have. 
   * If patient click on cancel button that mean he is cancel the appointment.
   * Add new appointment button send to home page if the patient need to book a new appointment. 
   * Logout button redirect to main page.  
  ### Patient Dashboard Preview
  ![2]()
## CheckBox Page:
* Features
   * The CheckBox page display days with time.
   * The doctor can book which day and time free for him.
   * When click on book sessions button add the choosen day and time to specialize page.
   * Back button redirect to doctor dashboard page. 
   * Logout button redirect to main page.  
  ### CheckBox Preview
  ![2]()
## Patient Diagnosis Page:
* Features
   * The patient diagnosis page display all patient diagnostics if patient loged in.
   * If doctor loged in can add his diagnosis to the patient diagnostics by click on update button.
   * Back button redirect to doctor dashboard page. 
   * Logout button redirect to main page.  
  ### Patient Diagnosis Preview
  ![2]()
## Specialize Page:
* Features
   * The specialize page display all doctors available for book.
   * The select options contain locations of doctors.
   * When click on search button display all doctors available in choosen location.
   * Back to clinics button send to home page.
   * Registration and Login button send to login and registration page.
   * Book button send to available appointments page if patient loged in,if not send to login and registration page.
  ### Specialize Preview
  ![2]()
## Available Appointments Page:
* Features
   * The available appointments page display all doctors free time.
   * Home button in navigation bar send to home page.
   * When click on back button in navigation bar send to specialize page.
  ### Available Appointments Preview
  ![2]()
  
## Technologies Used:
- python - version 3.10.7.
- Django - version 2.2.4.
- bootstrap - version 4.5.3.
- jQuery and AJAX.

  ![Technologies](https://user-images.githubusercontent.com/75543501/121818529-7417b600-cc90-11eb-97b0-59ebfe43f47c.png)

## Done by:
- Abdalfattah Hasanat. 
- Ra'd Abdallah.  
- Sura Qalalwa.
- Amin Hotari.

## Superviser:
- Amin Eid.
- Fatima Harahsheh.

