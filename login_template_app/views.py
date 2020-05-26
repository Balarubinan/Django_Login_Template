from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse
from .models import User

app_name='Login_App'
def sign_up_form(request):
    return render(request, 'login_template_app/signup.html')

def login_form(request):
    if request.POST:
        try:
            q = get_object_or_404(User, pk=request.POST['email'])
            if q.password == request.POST['pswd']:
                return HttpResponse('Login Success!!')
            else:
                return render(request,'login_template_app/login.html',context={'error':'*Password Incorrect!!'})
        except Exception:
            return render(request,'login_template_app/login.html',context={'error':'*No Such User exists!!'})
    return render(request, 'login_template_app/login.html')

def home(request):
    user = User()
    if request.POST['email'] in User.objects.values_list('email', flat=True).distinct():
        return render(request,'login_template_app/signup.html',context={'error':'*User aldready exists!!'})
    else:
        user.user_name = request.POST['name']
        if request.POST['pswd1'] != request.POST['pswd2']:
            return render(request,'login_template_app/signup.html',context={'error':'*Entered passwords do not match!!'})
        user.password = request.POST['pswd1']
        user.address = ""
        user.email = request.POST['email']
        user.phone = request.POST['phone']
        user.save()
        return HttpResponse('User Sign Up Success!!')
