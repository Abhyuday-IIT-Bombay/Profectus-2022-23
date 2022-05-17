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
from .models import Resume , Make_Resume

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
        # uploaded_file = request.POST['resume']
        info = Account(name = name , email = email , contact = contact)
        info.save()

        

        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username")
            return redirect('home')

        if User.objects.filter(email=email):
            messages.error(request, "Email already registered")   

        if pass1 != pass2:
            messages.error(request, "Passwords can't be different")

        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!")
            return redirect('home')



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
            email = request.POST['email']
            loc1 = request.POST['loc1']
            loc2 = request.POST['loc2']
            seducation = request.POST['seducation']
            sseducation = request.POST['sseducation']
            graduation = request.POST['graduation']
            por = request.POST['por']
            course = request.POST['course']
            project = request.POST['project']
            skill = request.POST['skill']
            blog = request.POST['blog']
            github = request.POST['github']
            other = request.POST['other']
            resfile = Make_Resume(fname=fname, lname=lname,email=email,loc1=loc1,loc2=loc2,seducation=seducation,sseducation=sseducation,graduation=graduation,por=por,course=course,project=project,skill=skill,blog=blog,github=github,other=other)
            resfile.save()
              # Create Bytestream buffer
            buf = io.BytesIO()
            # Create a canvas
            c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
            # Create a text object
            textob = c.beginText()
            textob.setTextOrigin(inch, inch)
            textob.setFont("Helvetica", 14)


            lines =[]

            lines.append(fname)
            lines.append(lname)
            lines.append(email)
            lines.append(loc1)
            lines.append(loc2)
            lines.append(seducation)
            lines.append(sseducation)
            lines.append(graduation)
            lines.append(por)
            lines.append(course)
            lines.append(project)
            lines.append(skill)
            lines.append(blog)
            lines.append(github)
            lines.append(other)
            lines.append(" ")

            for line in lines:
                    textob.textLine(line)

            # Finish Up
            c.drawText(textob)
            c.showPage()
            c.save()
            buf.seek(0)

            # Return something
            return  FileResponse(buf, as_attachment=True, filename='resume.pdf') 
        

# def resume_list(request):
#      # Create Bytestream buffer
#         buf = io.BytesIO()
#         # Create a canvas
#         c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
#         # Create a text object
#         textob = c.beginText()
#         textob.setTextOrigin(inch, inch)
#         textob.setFont("Helvetica", 14)

#         resumes = Make_Resume.objects.all()

#         lines =[]

#         for resume in resumes:
#             lines.append(resume.fname)
#             lines.append(resume.lname)
#             lines.append(resume.email)
#             lines.append(resume.loc1)
#             lines.append(resume.loc2)
#             lines.append(resume.seducation)
#             lines.append(resume.sseducation)
#             lines.append(resume.graduation)
#             lines.append(resume.por)
#             lines.append(resume.course)
#             lines.append(resume.project)
#             lines.append(resume.skill)
#             lines.append(resume.blog)
#             lines.append(resume.github)
#             lines.append(resume.other)
#             lines.append(" ")

#         for line in lines:
# 		        textob.textLine(line)

#         # Finish Up
#         c.drawText(textob)
#         c.showPage()
#         c.save()
#         buf.seek(0)

#         # Return something
#         return FileResponse(buf, as_attachment=True, filename='resume.pdf')
    

def upload_resume(request):
    if request.method =='POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("its working")
    else:
         form = ResumeForm()
    return render(request, 'authentication/upload_resume.html',{
        'form':form
    })    

