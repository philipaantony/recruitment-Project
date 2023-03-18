from django.db import models
from datetime import date
from django.core.validators import RegexValidator


# Create your models here.
class Company(models.Model):
    cname = models.CharField("Company Name",max_length=25)
    caddress = models.CharField("Company Address",max_length=250)
    phoneno_regex = RegexValidator(
        regex=r'^\+?1?\d{10,10}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )
    cphone = models.CharField("Company Phoneno",max_length=2, validators=[phoneno_regex])
    clicno = models.CharField("License No",max_length=25)
    cphoto = models.ImageField("License Image",upload_to='images/')
    cemail = models.EmailField("Company Email",unique=True)
    cpswd = models.CharField("Password",max_length=25)
    status = models.CharField("Application Status",default='N',max_length=20)

    def clean_phone(self):
        phone_number = self.cleaned_data.get("cphone")
        z = phonenumbers.parse(phone_number, "SG")
        if not phonenumbers.is_valid_number(z):
            raise forms.ValidationError("Number not in SG format")
        return phone_number


class User(models.Model):
    ufirst = models.CharField("First Name",max_length=25)
    ulast = models.CharField("Last Name",max_length=25)
    udob = models.DateField("Date of Brith",default=date.today)
    uphone = models.CharField("Phone No",max_length=25)
    uaadhar = models.CharField("Aadhaar No",max_length=25)
    uqual = models.CharField("Qualification",max_length=25,default=0)
    uexp = models.CharField("Work Experience",max_length=25,default=0)
    ufile = models.FileField("upload Resume",upload_to='resume/',max_length=254,default=0)
    upawd = models.CharField("Password",max_length=25)
    uemail = models.EmailField("User Email",unique=True)
    GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    )
    ugender = models.CharField("Gender",max_length=1, choices=GENDER_CHOICES)


class Postjob(models.Model):
    cid= models.IntegerField(default=0)
    jobtitle = models.CharField("Job Title",max_length=25)
    jobdesc = models.TextField("Job Description")
    jobtype = models.CharField("Job Type",max_length=25)
    location = models.CharField("Location",max_length=25)
    department = models.CharField("Department",max_length=25)
    nov = models.IntegerField("Number of Vacancy")
    tdate = models.DateField("Date of Posting",default=date.today)
    edate = models.DateField("Valid Till")
    cpname = models.CharField("Company Name",max_length=25)
    cpdese = models.TextField("Company description")
    email = models.EmailField("Email for Enquiry")
    status = models.CharField(default='Not Applied',max_length=15)



class Apply(models.Model):
    uid = models.IntegerField()
    uname = models.CharField(max_length=25, default=0)
    cid = models.IntegerField()
    cname = models.CharField(max_length=25,default=0)
    jid = models.IntegerField()
    jobtitle = models.CharField( max_length=25,default=0)
    jobtype = models.CharField(max_length=25,default=0)
    email = models.EmailField(default=0)
    status = models.CharField(max_length=25,default='NOT SELECTED')
