from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from authentication.models import Account
import pandas as pd
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
from .forms import ResumeForm
from .models import Resume , Make_Resume ,Apply

from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

# Create your views here.


def home(request):
    

    return render(request, "authentication/index.html")

def signup(request):

    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        name = request.POST['name']
        email = request.POST['email']
        contact = request.POST['contact']
        roll = request.POST['roll']
        department = request.POST['department']
        year = request.POST['year']
        request.session['name'] = name
        request.session['roll'] = roll

        # uploaded_file = request.POST['resume']

        info = Account(name = name , email = email , contact = contact, roll= roll,department =department, year=year)
        info.save()

        global rollvalue
        def rollvalue():
            return roll

        global value
        def value():
            return name

       

        

        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username")
            return redirect('signup')

        if User.objects.filter(email=email):
            messages.error(request, "Email already registered")   
            return redirect('signup')

        if pass1 != pass2:
            messages.error(request, "Passwords can't be different")
            return redirect('signup')


        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!")
            return redirect('signup')

        else:
            myuser = User.objects.create_user(username, email, pass1)
            myuser.first_name = name
            myuser.save()
            messages.success(request, "Your Account has been created successfully!")
            return redirect('login')
    return render(request, "authentication/signup.html")

def login(request):

    if request.method == "POST":
        username = request.POST['username']   
        pass1 = request.POST['pass1'] 

        user = authenticate(username=username, password = pass1)

        if user is not None:
            auth_login(request, user)
            name = user.first_name
                 
            return render(request, 'authentication/index.html', {'name':name})
        
        else:
            messages.error(request, "Bad Connection")
            return redirect('home')

            

    return render(request, "authentication/login.html")

def logout(request):
    auth_logout(request)
    messages.success(request, "Logged Out Successfully!")

    return redirect('home')

def details(request):
        return render(request, "authentication/details.html")
    

def export_data_to_excel(request):
    objs = Account.objects.all()
    data =[]

    for obj in objs:
        data.append({
            "Name": obj.name,
            "Email":obj.email,
            "Contact":obj.contact
        })

    pd.DataFrame(data).to_excel('output.xlsx')
    return JsonResponse({
        'status':200
    })
counter = 0



def resume(request):    
        if request.method =="POST":
            fname = request.POST['fname']
            lname = request.POST['lname']
            department = request.POST['department']
            roll = request.POST['roll']
            year = request.POST['year']
            startyear = request.POST['startyear']
            endyear = request.POST['endyear']
            cpi = request.POST['cpi']
            board12 = request.POST['board12']
            college = request.POST['college']
            year12 =request.POST['year12']
            cpi12 = request.POST['cpi12']
            board10 = request.POST['board10']
            school = request.POST['school']
            year10 =request.POST['year10']
            cpi10 = request.POST['cpi10']
            ptitle1 = request.POST['ptitle1']
            p1start = request.POST['p1start']
            p1end = request.POST['p1end']
            p1info = request.POST['p1info']
            ptitle2 = request.POST['ptitle2']
            p2start = request.POST['p2start']
            p2end = request.POST['p2end']
            p2info = request.POST['p2info']
            ptitle3 = request.POST['ptitle3']
            p3start = request.POST['p3start']
            p3end = request.POST['p3end']
            p3info = request.POST['p3info']
            proj1 = request.POST['proj1']
            proj1start = request.POST['proj1start']
            proj1end = request.POST['proj1end']
            proj1info = request.POST['proj1info']
            proj2 = request.POST['proj2']
            proj2start = request.POST['proj2start']
            proj2end = request.POST['proj2end']
            proj2info = request.POST['proj2info']
            proj3 = request.POST['proj3']
            proj3start = request.POST['proj3start']
            proj3end = request.POST['proj3end']
            proj3info = request.POST['proj3info']
            techskill = request.POST['techskill']
            activity1start = request.POST['activity1start']
            activity1end = request.POST['activity1end']
            activity1info = request.POST['activity1info']
            
            activity2start = request.POST['activity2start']
            activity2end = request.POST['activity2end']
            activity2info = request.POST['activity2info']
            
            activity3start = request.POST['activity3start']
            activity3end = request.POST['activity3end']
            activity3info = request.POST['activity3info']

            resfile = Make_Resume(fname=fname, lname=lname,department=department,roll=roll,year=year,startyear=startyear,endyear=endyear,cpi=cpi,board12=board12,college=college,year12=year12,cpi12=cpi12,board10=board10,school=school,year10=year10,cpi10=cpi10,ptitle1=ptitle1,ptitle2=ptitle2,ptitle3=ptitle3,p1start=p1start,p2start=p2start,p3start=p3start,p1end=p1end,p2end=p2end,p3end=p3end,p1info=p1info,p2info=p2info,p3info=p3info,proj1=proj1,proj2=proj2,proj3=proj3,proj1start=proj1start,proj2start=proj2start,proj3start=proj3start,proj1end=proj1end,proj2end=proj2end,proj3end=proj3end,proj1info=proj1info,proj2info=proj2info,proj3info=proj3info,activity1start=activity1start,activity2start=activity2start,activity3start=activity3start,activity1end=activity1end,activity2end=activity2end,activity3end=activity3end,activity1info=activity1info,activity2info=activity2info,activity3info=activity3info,techskill=techskill)
            resfile.save()
            
            data ={
                'fname':fname,
                'lname':lname,
                'department':department,
                'roll':roll,'year':year,'startyear':startyear,'endyear':endyear,'cpi':cpi,'board12':board12,'college':college,'year12':year12,'cpi12':cpi12,'board10':board10,'school':school,'year10':year10,'cpi10':cpi10,'ptitle1':ptitle1,'ptitle2':ptitle2,'ptitle3':ptitle3,'p1start':p1start,'p2start':p2start,'p3start':p3start,'p1end':p1end,'p2end':p2end,'p3end':p3end,'p1info':p1info,'p2info':p2info,'p3info':p3info,'proj1':proj1,'proj2':proj2,'proj3':proj3,'proj1start':proj1start,'proj2start':proj2start,'proj3start':proj3start,'proj1end':proj1end,'proj2end':proj2end,'proj3end':proj3end,'proj1info':proj1info,'proj2info':proj2info,'proj3info':proj3info,'activity1start':activity1start,'activity2start':activity2start,'activity3start':activity3start,'activity1end':activity1end,'activity2end':activity2end,'activity3end':activity3end,'activity1info':activity1info,'activity2info':activity2info,'activity3info':activity3info,'techskill':techskill
                
                
            }
            global val
            def val():
                return data
            # Return something
            return  render(request, 'authentication/upload_resume.html' ,{
                'fname':fname,
                'lname':lname,
                'department':department,
                'roll':roll,'year':year,'startyear':startyear,'endyear':endyear,'cpi':cpi,'board12':board12,'college':college,'year12':year12,'cpi12':cpi12,'board10':board10,'school':school,'year10':year10,'cpi10':cpi10,'ptitle1':ptitle1,'ptitle2':ptitle2,'ptitle3':ptitle3,'p1start':p1start,'p2start':p2start,'p3start':p3start,'p1end':p1end,'p2end':p2end,'p3end':p3end,'p1info':p1info,'p2info':p2info,'p3info':p3info,'proj1':proj1,'proj2':proj2,'proj3':proj3,'proj1start':proj1start,'proj2start':proj2start,'proj3start':proj3start,'proj1end':proj1end,'proj2end':proj2end,'proj3end':proj3end,'proj1info':proj1info,'proj2info':proj2info,'proj3info':proj3info,'activity1start':activity1start,'activity2start':activity2start,'activity3start':activity3start,'activity1end':activity1end,'activity2end':activity2end,'activity3end':activity3end,'activity1info':activity1info,'activity2info':activity2info,'activity3info':activity3info ,'techskill':techskill
            })
        


def upload_resume(request):
    if request.method =='POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"Resume Submitted Succesfully!")
            return render(request,'authentication/upload_resume.html')
    else:
         form = ResumeForm()
    return render(request, 'authentication/upload_resume.html',{
        'form':form
    })    

# importing the necessary libraries
from django.views.generic import View
from .forms import html_to_pdf 

#Creating a class based view
class GeneratePdf(View):
     def get(self, request, *args, **kwargs):
        
        data = val()
        # getting the template
        pdf = html_to_pdf('authentication/generate_resume.html',data)
         
         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')

def back(request):
    return render(request ,"authentication/index.html")

def apply(request):
    if request.method == 'POST':
        name = request.session['name'] 
        roll = request.session['roll'] 
        pref1 = request.POST['pref1']
        pref2 = request.POST['pref2']
        pref3 = request.POST['pref3']
        applyinfo= Apply(name = name , roll=roll,pref1=pref1,pref2=pref2,pref3=pref3)
        applyinfo.save()
        return render(request ,"authentication/index.html")

    




        

