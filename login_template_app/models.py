from django.db import models


class User(models.Model):
    user_name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email=models.CharField(max_length=200,primary_key=True)
    address=models.CharField(max_length=300)
    phone=models.IntegerField(default=0)

    def __str__(self):
        return str(self.user_name)+str(self.password)

    def check_passsword(self,password_given):
        return password_given==self.password


