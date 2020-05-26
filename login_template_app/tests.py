from django.test import TestCase
from django.urls import reverse

from .models import User

#  write more test so that you can finsih this project
# try to deploy this project

def create_object():
    r=User()
    r.email='test@gmail.com'
    r.password='test'
    r.phone='9629902359'
    r.user_name='test'
    return r

class login_view_tests(TestCase):
    def test_login_with_pass(self):
        '''To check if the user is correctly redirected to the next page afetr login'''
        q = create_object()
        q.save()
        res = self.client.post(reverse('Login_App:login_page'), data={'email':q.email,'pswd':q.password})
        self.assertQuerysetEqual(User.objects.all(), ['<User: testtest>'])
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, 'Success')

    def test_login_with_wrng_pass(self):
        '''To check if the Login viiew returns the write response for incorrect password'''
        q=create_object()
        q.save()
        res=self.client.post(reverse('Login_App:login_page'),data={'email':q.email,'pswd':'notqpass'})
        self.assertContains(res,'Incorrect')

    def test_view_available(self):
        '''To chceck if the inital view is available ie the login view'''
        res=self.client.get(reverse('Login_App:sign_up'))
        self.assertEqual(res.status_code,200)

    def test_signup_correct_creds(self):
        '''To check the response of the server to mismatched passwords in signup page'''
        data_dict={'email':'just@gmail.com','pswd1':'just','pswd2':'just','name':'Bala','address':'Justa demo address',
                   'phone':'1234567890'}
        res=self.client.post(reverse('Login_App:home'),data=data_dict)
        self.assertEqual(res.status_code,200)
        self.assertQuerysetEqual(User.objects.all(),['<User: Balajust>'])

    def test_signup_passwrod_mismatch(self):
        '''to check thee output if the signup form gets passwrod which dont match as input'''
        data_dict = {'email': 'just@gmail.com', 'pswd1': 'notjust', 'pswd2': 'just', 'name': 'Bala',
                     'address': 'Justa demo address',
                     'phone': '1234567890'}
        res=self.client.post(reverse('Login_App:home'),data=data_dict)
        self.assertEqual(res.status_code,200)
        self.assertQuerysetEqual(User.objects.all(),[])

class model_User_tests(TestCase):
    def test_str(self):
        '''checks if inbuild string method works fine'''
        q=create_object()
        self.assertEqual(q.__str__(),'testtest')