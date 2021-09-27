from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.

def landingpage(request):
    return render(request,'landingpage.html')

def createaccount(request):
    if request.method=='POST':
        username= request.POST['username']
        first_name= request.POST['first_name']
        last_name= request.POST['last_name']
        email= request.POST['email1']
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
                return render(request,'sign-in.html')
                print('user created')
        else:
            messages.info(request,'password did not matched')
            return render(request,'createaccount.html')
        return redirect('/')
        
    else:
        return render(request,'createaccount.html')

#signin
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,'index.html')
            #return redirect("/")

        else:
            messages.info(request,'invalid email and password')
            return redirect('login')
    else:
        return render(request,'sign-in.html')
