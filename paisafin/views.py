from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Destination,all,Contactus,Update
# Create your views here.
def landingpage(request):
    return render(request,'landingpage.html')
# creating account page
def createaccount(request):
    if request.method=='POST':
        username= request.POST['username']
        first_name= request.POST['first_name']
        last_name= request.POST['last_name']
        email= request.POST['email1']
        email2=request.POST['email2']
        #email2= request.POST['email2']
        #countrycode= request.POST['countrycode']
        #number= request.POST['number']
        #number2= request.POST['number2']
        password1= request.POST['password1']
        password2= request.POST['password2']
        #address= request.POST['address']
        #country= request.POST['country']
        #language= request.POST['language']
        #type=request.POST['type']

        #user=User.objects.create_user(username='username',password=password1,email=email,first_name=first_name,number=number,number2=number2,address=address,country=country,countrycode=countrycode,language=language,type=type)
        if password1==password2:
            if(User.objects.filter(username=username).exists()):
                messages.info(request,'Username already exist')
                return render(request,'createaccount.html')
            elif(User.objects.filter(email=email).exists()):
                messages.info(request,'email already exist')
                return render(request,'createaccount.html')
            else:
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                myname=email
                #stroing to other table
                postto=all()
                postto.username= request.POST['username']
                postto.email=request.POST['email1']
                postto.email2=request.POST['email2']
                postto.password=request.POST['password1']
                postto.first_name= request.POST['first_name']
                postto.last_name= request.POST['last_name']
                postto.save()
                return render(request,'sign-in.html')
                print('user created')
        else:
            messages.info(request,'password did not matched')
            return render(request,'createaccount.html')
        return redirect('/')
        
    else:
        return render(request,'createaccount.html')

# creating signin page
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        print(username)
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('index')
            #return redirect("/")

        else:
            messages.info(request,'invalid email and password')
            return redirect('login')
    else:
        return render(request,'sign-in.html')
#creating index page
def index(request):
    dest=Destination.objects.all()
    return render(request, 'index.html',{'dest':dest})
#creating withdraw page
def withdraw(request):
    return render(request,'withdraw.html')
#contactus
def contactus(request):
    if request.method=='POST':
        con=Contactus()
        con.name=request.POST['contactusname']
        con.email=request.POST['contactusemail']
        con.issue=request.POST['contactusissue']
        con.save()
        return redirect('index')
    else:
        print("not coming")
        return render(request,'contactus.html')
# creating advertise page
def advertise(request):
    if request.method=='POST':
        postad=Destination()
        postad.header= request.POST['header']
        postad.url=request.POST['url']
        postad.description=request.POST['description']
        postad.type=request.POST['type']
        postad.silver=request.POST['silver']
        postad.silverclick=request.POST['silverclick']
        postad.silverimpression=request.POST['silverimpression']
        postad.money=request.POST['money']
        postad.moneyclick=request.POST['moneyclick']
        postad.moneyimpression=request.POST['moneyimpression']
        #userad=Destination(header=header,url=url,description=description,type=type,free=free,silver=silver,silverclick=silverclick,silverimpression=silverimpression,money=money,moneyclick=moneyclick,moneyimpression=moneyimpression)
        postad.save()
        return redirect('index')
    else:
        print("not coming")
        return render(request,'advertise.html')
def advdashboard(request):
    if request.method=='POST':
        
        return redirect('index')
    else:
        balance=all.objects.all()
        return render(request, 'advertisedashboard.html',{'balance':balance})
        return render(request,'advertisedashboard.html')

#terms and conditions
def termsandcondition(request):
    return render(request,'termsandcondition.html')
#privacy Policy
def privacypolicy(request):
    return render(request,'privacypolicy.html')

# Update profile
def update(request):
    return render(request,'update.html')


def update(request):
    if request.method=="POST":
        update=Update()
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        requiredemail=request.POST.get('email')
        optionalemail=request.POST.get('optemail')
        countrycode=request.POST.get('countrycode')
        firstnumber=request.POST.get('firstnumber')
        secondnumber=request.POST.get('secondnumber')
        enterpassword=request.POST.get('enterpassword')
        reenterpassword=request.POST.get('reenterpassword')
        address=request.POST.get('address')
        country=request.POST.get('country')
        language=request.POST.get('language')
        Type=request.POST.get('type')
        interest=request.POST.get('interest=request')
        interest=request.POST.get('interest=request')
        interest=request.POST.get('interest=request')
        interest=request.POST.get('interest=request')
        website=request.POST.get('website')
        facebook=request.POST.get('facebook')
        instagram=request.POST.get('instagram')
        twitter=request.POST.get('twitter')
        pinterest=request.POST.get('pinterest')
        youtube=request.POST.get('youtube')
        update.firstname=firstname
        update.lastname=lastname
        update.requiredemail=requiredemail
        update.optionalemail=optionalemail
        update.countrycode=countrycode
        update.firstnumber=firstnumber
        update.secondnumber=secondnumber
        update.enterpassword=enterpassword
        update.address=address
        update.country=country
        update.language=language
        update.Type=Type
        update.save()
        return redirect('profile')
    else:
        return render(request,'update.html')



# advertiser history 
def advhistory(request):
    hist=Destination.objects.all()
    return render(request, 'advhistory.html',{'hist':hist})
# about us of settings
def aboutus(request):
    return render(request,'aboutus.html')
def dashboard(request):
    return render(request,'paisadashboard.html')
def report(request):
    return render(request,'paisareport.html')
def referearn(request):
    return render(request,'referearn.html')
def advreport(request):
    return render(request,'advreport.html')
def profile(request):
    return render(request,'profile.html')