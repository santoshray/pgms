from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail

# Create your views here.

def index(request):
    res_dict = {}
    return render(request,'index.html',context=res_dict)


def contact(request):
    res_dict = {}
    if request.method=="GET":
        return render(request,'contact.html',context=res_dict)

    if request.method=="POST":
        post_content = request.POST
        print(post_content)
        sms_email  = '+1'+post_content['phone']+'@sms.clicksend.com'
        print(sms_email)
#        subject = 'auth~comfortabode~78870A2F-4248-2D55-E1C9-65652B703319~TestMail~mycompany'
        subject = "Guest Message"
        mail_content = post_content['message']
#        send_mail(subject, mail_content, 'santosh.ray81@gmail.com', [sms_email], fail_silently=False)
        send_mail(subject, mail_content, 'noreply@comfortabode.com', [post_content['email']], fail_silently=False)

        return render(request,'contact.html',context=res_dict)
