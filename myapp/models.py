from django.db import models


# Create your models here.
class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=200)


class ContactData(models.Model):
    name= models.CharField(max_length=200)
    Contact_no= models.CharField(max_length=200)
