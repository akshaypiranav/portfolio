from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
from .models import Projects,ResumeModel
# Create your views here.
def index(request):
    if request.method=="POST":
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        contact=request.POST['contact']
        message=request.POST['message']
        print(firstname,lastname,email,contact,message)
        sender_email = "akshaypiranavb@gmail.com"
        receiver_email = "akshaypiranavb@gmail.com"
        subject = "Request Call"
        body = "Customer Detail :"+'\n'+str(firstname)+" "+str(lastname)+'\n'+'Email : '+str(email)+'\n'+"Contact Number : "+str(contact)+"\n"+"Customer Message : "+str(message)

        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject

        message.attach(MIMEText(body, "plain"))

        smtp_server = "smtp.gmail.com" 
        smtp_port = 587  
        smtp_username = "akshaypiranavb@gmail.com"  
        smtp_password = "ddld flec vggd ovve"

        try:
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()  
                server.login(smtp_username, smtp_password)
                server.sendmail(sender_email, receiver_email, message.as_string())
                messages.success(request, 'Email Sent Successfully')

        except Exception as e:
            print(f"Error sending email: {e}")
            messages.success(request,'Check Your Network Connection')

    return render(request,"index.htm")


def projects(request):
    projects=Projects.objects.all()

    return render(request,"projects.htm",{"project":projects})

def resume(request):
    if request.method=="POST":
        resume = get_object_or_404(ResumeModel, pk=1)
        response = HttpResponse(resume.resume_file.read(), content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{resume.resume_file.name}"'

        return response
    return redirect("/")


def notfound(request,value):
    return render(request,"404.htm")