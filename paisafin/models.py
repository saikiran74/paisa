from django.db.models.base import Model
from django.db.models.fields import CharField, DateTimeField
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
'''from ckeditor.fields import RichTextField'''
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class Comments(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    username=models.CharField(max_length=400,default='None')
    comment=models.CharField(max_length=1000,default='None')
    Date=models.DateTimeField(auto_now_add=True)
    post_id=models.IntegerField(blank=True,default=0)
    def __str__(self) -> str:
        return super().__str__()



class Destination(models.Model):
    #id is create automatically.
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    username=models.CharField(max_length=100,default='None')
    header=models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    description = RichTextUploadingField(blank=False,null=True)
    #silver= models.BooleanField(default=False)
    free=models.BooleanField(default=True)
    silver=models.IntegerField(default=0,blank=False, null=True)
    silverclick=models.IntegerField(default=0)
    silverimpression=models.IntegerField(default=0)
    money=models.IntegerField(default=0)
    moneyclick=models.IntegerField(default=0)
    moneyimpression=models.IntegerField(default=0)
    silver_banus=models.IntegerField(default=0)
    money_banus=models.IntegerField(default=0)
    likes=models.ManyToManyField(User,related_name="likes")
    views=models.IntegerField(default=0,blank=True,null=True)
    comments=models.IntegerField(default=0,blank=True,null=True)
    shares=models.IntegerField(default=0,blank=True,null=True)
    total_clicks=models.IntegerField(default=0)
    clicks=models.ManyToManyField(User,related_name="clicks")
    total_visiters=models.IntegerField(default=0)
    impressions=models.ManyToManyField(User,related_name="impressions")
    comments=models.ManyToManyField(Comments,related_name="comments",default=0)
    def get_absolute_url(self):
        return reverse('app:item',kwargs={'pk:self.pk'})

class Country(models.Model):
    country_name=models.CharField(max_length=200)
    def __str__(self):
        return self.country_name
class Type(models.Model):
    type=models.CharField(max_length=100)
    def __str__(self):
        return self.type
class Language(models.Model):
    language=models.CharField(max_length=100)
    def __str__(self):
        return self.language


class All(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    username=models.CharField(max_length=100,default='None')
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    email=models.EmailField(max_length=254)
    email2=models.EmailField(max_length=254,null=True)
    password=models.TextField(null=True)
    number=models.IntegerField(null=True)
    number2=models.IntegerField(null=True)
    address=models.TextField(max_length=500,null=True)
    country=models.ForeignKey(Country,on_delete=models.CASCADE,null=True)
    language=models.ForeignKey(Language,on_delete=models.CASCADE,null=True)
    moneybalance=models.IntegerField(default=0)
    silverbalance=models.IntegerField(default=0)
    mymoney=models.IntegerField(default=0)
    mysilvers=models.IntegerField(default=0)
    bonus=models.IntegerField(default=1000)
    brandname=models.CharField(max_length=100,null=True)
    website=models.CharField(max_length=100,null=True)
    facebook=models.CharField(max_length=100,null=True)
    instagram=models.CharField(max_length=100,null=True)
    twitter=models.CharField(max_length=100,null=True)
    pinterest=models.CharField(max_length=100,null=True)
    youtube=models.CharField(max_length=100,null=True)
    ads=models.IntegerField(default=0)
    followers=models.ManyToManyField(User,related_name="followers",default=0)
    likes=models.CharField(max_length=100,default=0)
    rating=models.CharField(max_length=100,default=0)
    
    type=models.ForeignKey(Type,on_delete=models.CASCADE,null=True)
    
class Contactus(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    username=models.CharField(max_length=100,default='None')
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    issue=models.CharField(max_length=1000)

class Silverbazar(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    username=models.CharField(max_length=250,default='None')
    silver=models.IntegerField(default=0)
    costpersilver=models.IntegerField(default=0)
    total_cost=models.IntegerField(default=0)

