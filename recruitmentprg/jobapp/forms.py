from django import forms
from jobapp.models import Company,User,Postjob

class Companyform(forms.ModelForm):
    class Meta:
        model = Company
        fields =['cname','caddress','cphone','clicno','cphoto','cemail','cpswd']

class Userform(forms.ModelForm):
    class Meta:
        model = User
        fields =['ufirst','ulast','udob','uphone','uaadhar','uqual','uexp','ufile','upawd','uemail','ugender']

class Jobform(forms.ModelForm):
    class Meta:
        model = Postjob
        fields=['cid','jobtitle','jobdesc','jobtype','location','department','nov','tdate','edate','cpname','cpdese','email']