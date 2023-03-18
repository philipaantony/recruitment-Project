from django.shortcuts import render,redirect
from .models import Company,User,Postjob,Apply
from jobapp.forms import Companyform,Userform,Jobform
from django.views.generic import CreateView,ListView
from django.db.models.functions import Coalesce
from django.db.models import Max, Value
from django.http import FileResponse, Http404

def home(request):
    return render(request,"home.html")

class CompanyView(CreateView):
    template_name = "add_company.html"
    form_class = Companyform
    success_url = "/"

class CompanyList(ListView):
    template_name = "Company_list.html"
    model=Company
    context_object_name = "a"

class UserView(CreateView):
    template_name = "add_user.html"
    form_class = Userform
    success_url = "/"

class UserList(ListView):
    template_name = "user_list.html"
    model=User
    context_object_name = "a"






def login(request):
    if request.method=="POST":
        emails=request.POST.get('email')
        passwords=request.POST.get('password')
        obj= Company.objects.filter(cemail=emails,cpswd=passwords)
        obj2 = User.objects.filter(uemail=emails, upawd=passwords)
        if obj.filter(cemail=emails,cpswd=passwords).exists():

            for i in obj:
                y=i.id
                x=i.status
                cname=i.cname
                caddress=i.caddress
                request.session['email']=emails          #change after
                request.session['password']=passwords
                request.session['id']=y
                request.session['cname']=cname
                request.session['caddress'] = caddress

                if x=='A':
                    return render(request, "admin_home.html")
                elif x=='N':
                    return render(request, "underproccess_home.html")
                elif x=='AP':
                    return render(request, "company_home.html")
                elif x=='R':
                    return render(request,"rejected.html")
                else:
                    return render(request,"invalid.html")
        elif obj2.filter(uemail=emails,upawd=passwords).exists():
            for i in obj2:
                z=i.id
                y=i.ufirst
                request.session['id']=z
                request.session['ufirst'] = y
            return render(request,"user_home.html")

        else:
            return render(request,"invalid.html")
    else:
        return render(request,"login_form.html")

class JobView(CreateView):
    template_name = "company_job_form.html"
    form_class = Jobform
    success_url = "success"

class JobList(ListView):
    template_name = "user_job_list.html"
    model=Postjob
    context_object_name = "a"

def edituser(request):
    rec=User.objects.get(pk=request.session['id'])  #rec variable rcode is theid
    form=Userform(instance=rec)
    return render(request,'user_update.html',{"form":form,"id":id})


def updateuser(request):
    rtos=User.objects.get(pk=request.session['id'])
    form=Userform(request.POST,instance=rtos)
    if form.is_valid():
        form.save()
        return render(request, 'user_home.html',{"id":id})
    return render(request,'rejected.html',{"id":id})



def editcmp(request):
    rec=Company.objects.get(pk=request.session['id'])  #rec variable rcode is theid
    form=Companyform(instance=rec)
    return render(request,'company_update.html',{"form":form,"id":id})


def updatecmp(request):
    rtos=Company.objects.get(pk=request.session['id'])
    form=Companyform(request.POST,instance=rtos)
    if form.is_valid():
        form.save()
        return render(request, 'company_home.html',{"id":id})
    return render(request,'rejected.html',{"id":id})


def editadmin(request):
    rec=Company.objects.get(pk=request.session['id'])  #rec variable rcode is theid
    form=Companyform(instance=rec)
    return render(request,'admin_update.html',{"form":form,"id":id})

def updateadmin(request):
    rtos=Company.objects.get(pk=request.session['id'])
    form=Companyform(request.POST,instance=rtos)
    if form.is_valid():
        form.save()
        return render(request, 'admin_home.html',{"id":id})
    return render(request,'rejected.html',{"id":id})


def ch(request):
    a = Company.objects.filter(status='N')
    return render(request, "company_status.html",{"a":a})

def updatestatus(request,id):
    Company.objects.filter(id=id).update(status='AP')
    return render(request, "admin_home.html")

def deletestatus(request,id):
    Company.objects.filter(id=id).update(status='R')
    return render(request, "admin_home.html")

def postjob(request):
    emp=Postjob.objects.all
    return render(request, "company_job_form.html", {"emp": emp})

def postnewjob(request):
    if request.method=="POST":
        a=request.session['id']
        b=request.session['cname']
        c=request.session['caddress']
        jname = request.POST.get('jname')
        jdese = request.POST.get('jdese')
        jtype = request.POST.get('jtype')
        location = request.POST.get('location')
        dp =  request.POST.get('department')
        nov = request.POST.get('nov')
        tdate= request.POST.get('tdate')
        edate= request.POST.get('edate')
        #cn=request.POST.get('cname')
        #cd=request.POST.get('cdese')
        e = request.POST.get('email')
        va=Postjob(cid=a,jobtitle=jname, jobdesc=jdese,jobtype=jtype,location=location,department=dp,nov=nov,tdate=tdate,edate=edate,cpname=b,cpdese=c,email=e)
        va.save()
        return render(request,'company_home.html')
    else:
        return render(request,'company_job_form.html')

def deletejob(request,id):
    a = Postjob.objects.get(id=id)
    a.delete()
    return render(request, "company_home.html")


def apply(request,id):
    ab = request.session['id']
    ufirst = request.session['ufirst']
    obj = Postjob.objects.filter(id=id)
    for i in obj:
        y = i.id
        x = i.cid
        cpname = i.cpname
        jobtitle = i.jobtitle
        jobtype = i.jobtype
        email = i.email
        request.session['jid'] = y
        request.session['cid'] = x
        if Apply.objects.filter(uid=ab,jid=y).exists():
            return render(request, "user_warning.html")
        else:
            va = Apply(uid=ab,uname=ufirst,cid=x,jid=y,cname=cpname,jobtitle=jobtitle,jobtype=jobtype,email=email,status='NOT SELECTED')
            va.save()
            return render(request, "user_home.html")

def appliedjob(request):
    pk = request.session['id']
    a = Apply.objects.filter(uid=pk)
    return render(request, "user_applied_list.html", {"a": a})


def deleteappliedjob(request,id):
    a = Apply.objects.get(id=id)
    a.delete()
    return render(request, "user_home.html")


def viewpostedjobs(request):
    pk=request.session['id']
    a = Postjob.objects.filter(cid=pk)
    return render(request, "company_postedjob_list.html", {"a": a})

def viewapplicants(request):
    pk = request.session['id']            #company id
    a = Postjob.objects.filter(cid=pk)    #company id == cid in company model
    return render(request, "company_jobs_list.html", {"a": a})

def viewjobseekers(request,id):          #id denote jobid
    a = Apply.objects.filter(jid=id)
    for i in a:
        x = i.jid
        y = i.cid
        request.session['jid'] = x
        request.session['cid'] = y
    return render(request, "company_jobapplicants_list.html", {"a": a})

def userprofile(request,id):
    a=User.objects.filter(id=id)
    return render(request,"company_user_profile.html",{"a":a})


def selectuser(request,id):
    pk = request.session['jid']
    Apply.objects.filter(uid=id,jid=pk).update(status='SELECETD')
    return render(request, "company_home.html")

