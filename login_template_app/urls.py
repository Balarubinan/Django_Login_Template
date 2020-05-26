from django.urls import path
from django.contrib import admin
from . import views

app_name='Login_App'
urlpatterns=[path('login/',views.login_form,name='login_page'),
             path('signup/',views.sign_up_form,name='sign_up'),
             path('check/',views.home,name='home')
             ]