from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Destination(models.Model):
    #id is create automatically.
    header=models.CharField(max_length=100)
    url=models.TextField()
    description= models.TextField()
    type= models.CharField(max_length=25)
    #silver= models.BooleanField(default=False)
    free=models.BooleanField(default=True)
    silver=models.IntegerField(default=0,blank=True, null=True)
    silverclick=models.IntegerField()
    silverimpression=models.IntegerField()
    money=models.IntegerField()
    moneyclick=models.IntegerField()
    moneyimpression=models.IntegerField()

class all(models.Model):
    username=models.CharField(max_length=100)
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    email=models.TextField()
    email2=models.TextField()
    password=models.TextField()
    moneybalance=models.IntegerField(default=0)
    silverbalance=models.IntegerField(default=0)
    mybalance=models.IntegerField(default=0)

class Contactus(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    issue=models.CharField(max_length=1000)



class Update(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    requiredemail=models.EmailField(max_length=100)
    optionalemail=models.EmailField(max_length=100)
    countrycode=models.CharField(max_length=100)
    firstnumber=models.CharField(max_length=100)
    secondnumber=models.CharField(max_length=100)
    enterpassword=models.TextField()
    address=models.CharField(max_length=500)
    country=(('India'),('Canada'),('italy'))
    country=models.CharField(max_length=100)
    language=(('telugu'),('hindi'),('English'))
    language=models.CharField(max_length=100)
    Type=(('Advertiser'),('Viewer'),('Both'))
    Type=models.CharField(max_length=50)
    interest=models.BooleanField("games",default=False)
    interest=models.BooleanField("technologies",default=False)
    interest=models.BooleanField("socialmedia",default=False)
    interest=models.BooleanField("product",default=False)
    website=models.CharField(max_length=100)
    facebook=models.CharField(max_length=100)
    instagram=models.CharField(max_length=100)
    twitter=models.CharField(max_length=100)
    pinterest=models.CharField(max_length=100)
    youtube=models.CharField(max_length=100)
