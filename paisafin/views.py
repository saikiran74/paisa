from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Comments, Destination,All,Contactus, Silverbazar
from .forms import AllForm, DestinationForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

'''
def followers(request):
    follow=get_object_or_404(All,username=request.POST.get('post_id'))
    if follow.followers.filter(id=request.user.id).exists():
        follow.followers.remove(request.user)
    else:
        follow.followers.add(request.user)
    return redirect("index")
'''


def comment(request):
    if(request.method=="POST"):
        temp=Comments()
        temp.username=request.user.username
        temp.user_id=request.user.id
        temp.comment=request.POST['text']
        temp.post_id=request.POST.get('destid')
        temp.save()
        '''comment=get_object_or_404(Destination,userid=request.POST.get('destid'))
        comment.comments.add(request.user)'''
        return redirect('index')
    return render(request,'index.html')


























def silverbazar(request):
    tmp=Silverbazar.objects.all()[::-1]
    return render(request,'silverbazar.html',{'tmp':tmp})

def paisamoney(request,pk):
    pass



def pay(request,pk):
    all=All.objects.get(username=pk)
    all.moneybalance=all.moneybalance + int(request.POST['amount'])
    all.silverbalance=all.silverbalance + int(request.POST['silver'])*10
    all.save()
    return redirect('advdashboard')

def sell(request,pk):
    if request.method=='POST':
        all=All.objects.get(username=pk)
        tmp=Silverbazar()
        if all.mysilvers >= int(request.POST['totalsilvers']):
            tmp.username=request.user.username
            tmp.user_id=request.user.id
            tmp.silver=request.POST['totalsilvers']
            tmp.costpersilver=request.POST['amount']
            tmp.total_cost=(int(request.POST['amount']))*(int(request.POST['totalsilvers']))
            all.mysilvers= all.mysilvers - int(request.POST['totalsilvers'])
            all.save()
            tmp.save()
        else:
            return redirect('dashboard')
        return redirect('index')
    else:
        return render(request,'paisadashboard.html')
    
def withdrawmoney(request,pk):
    if request.method=='POST':
        all=All.objects.get(username=pk)
        if all.mymoney >= int(request.POST['totalamount']):
            all.mymoney= all.mymoney - int(request.POST['totalamount'])
            all.save()
            return redirect(index)
        else:
            return redirect(dashboard)
    else:
        return render(request,'paisadashboard.html')




def visit(request,pk):
    visiter=get_object_or_404(Destination,id=pk)
    all=All.objects.get(username=request.user.username)
    if visiter.clicks.filter(id=request.user.id).exists():
        print("User already exist in clicks")
    else:
        print("User not exist")
        visiter.total_clicks=visiter.total_clicks+1
        if visiter.money >= visiter.moneyclick:
            all.mymoney = all.mymoney + visiter.moneyclick
            visiter.money = visiter.money - visiter.moneyclick 
        elif visiter.money > 0 and visiter.money < visiter.moneyclick:
            all.mymoney = all.mymoney + visiter.money
            visiter.money = visiter.money-visiter.money
        else:
            all.mymoney = all.mymoney
            visiter.money = visiter.money
        if visiter.silver >= visiter.silverclick :
            all.mysilvers = all.mysilvers + visiter.silverclick
            visiter.silver = visiter.silver - visiter.silverclick
        elif visiter.silver > 0 and visiter.silver < visiter.silverclick :
            all.mysilvers = all.mysilvers + visiter.silver
            visiter.silver = visiter.silver - visiter.silver
        else:
            all.mysilvers = all.mysilvers
            visiter.silver = visiter.silver

        all.save()
        visiter.clicks.add(request.user)
    visiter.total_visiters=visiter.total_visiters+1
    visiter.save()
    return redirect(request.POST.get('post_url'))
        
def followers(request):
    follow=get_object_or_404(All,username=request.POST.get('post_id'))
    if follow.followers.filter(id=request.user.id).exists():
        follow.followers.remove(request.user)
    else:
        follow.followers.add(request.user)
    return redirect("index")

def search(request):
    if request.method == 'POST':
        searchedtext=request.POST['search']
        searchresult=Destination.objects.filter(header__contains=searchedtext)
        return render(request,'searchpage.html',{'searchedtext':searchedtext,'searchresult':searchresult})

def like(request): 
    post=get_object_or_404(Destination,id=request.POST.get('post_id'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    #return HttpResponseRedirect(reverse('like',args=[str(pk)]))
    return redirect('index')
    #return HttpResponseRedirect(post.get_absolute_url())


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
                postto=All()
                postto.user_id=request.user.id
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
#logout
def logout(request):
    auth.logout(request)
    return redirect('/')
#creating index page
#def index(request):
#    dest=Destination.objects.all()[::-1]
#   return render(request, 'index.html',{'dest':dest})

def index(request):
    dest=Destination.objects.all()[::-1]
    all=All.objects.all()
    comment=Comments.objects.all()[::-1]
#    for like in dest.likes.all():
#       if like is request.user:
#           is_like=True
#           break
    context={
        'dest':dest,
        'all':all,
        'comments':comment
    }
    return render(request, 'index.html',context)


# creating advertise page
@login_required
def advertise(request,pk):
    initial_values={
        'username':request.user.username,
    }
    form=DestinationForm()
    all=All.objects.get(username=pk)
    if request.method=='POST':
        all=All.objects.get(username=pk)
        form=DestinationForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            if all.moneybalance >= int(instance.money) and all.silverbalance >= int(instance.silver):
                all.ads=all.ads+1
                all.moneybalance=all.moneybalance-int(instance.money)
                #Todo here is add validation that check instance.moeny is exist or not
                all.silverbalance=all.silverbalance-int(instance.silver)
                all.save()
                instance.save()
                return redirect('index')
            else:
                return redirect('advdashboard')
        
    else:
        form=DestinationForm(initial=initial_values)
        context={'form':form}
        return render(request,'advertise.html',context)
    
    '''if request.method=='POST':
        all=All.objects.get(username=pk)
        postad=Destination()
        postad.user_id=request.user.id
        postad.username=request.user.username
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
        if all.moneybalance >= int(postad.money) and all.silverbalance >= int(postad.silver):
            all.ads=all.ads+1
            all.moneybalance=all.moneybalance-int(postad.money)
            all.silverbalance=all.silverbalance-int(postad.silver)
            postad.save()
            all.save()
            return redirect('index')
        else:
            return redirect('advdashboard')
    else:
        print("not coming")
        return render(request,'advertise.html')
'''



#contactus
def contactus(request):
    if request.method=='POST':
        con=Contactus()
        con.user=request.user
        con.user_id=request.user.id
        con.name=request.POST['contactusname']
        con.email=request.POST['contactusemail']
        con.issue=request.POST['contactusissue']
        con.save()
        return redirect('index')
    else:
        return render(request,'contactus.html')

    '''form=ContactusForm()
    if request.method=='POST':
        contact=Contactus.objects.get(pk=id)
        form=ContactusForm(request.POST or None,instance=contact)
        if form.is_valid():
            form.save()
            return redirect('index')
            print("true")
        else:
            print("not working")
    else:
        contact = Contactus.objects.get(pk=id)
        return render(request, 'contactus.html', contact)'''

def advdashboard(request):
    balance=All.objects.all()
    return render(request, 'advertisedashboard.html',{'balance':balance})

#terms and conditions
def termsandcondition(request):
    return render(request,'termsandcondition.html')
#privacy Policy
def privacypolicy(request):
    return render(request,'privacypolicy.html')

# Update profile
def update(request):
    return render(request,'update.html')


def update(request,pk):
    all = All.objects.get(username=pk)
    form=AllForm(instance=all)
    if request.method=='POST':
        form=AllForm(request.POST,instance=all)
        if form.is_valid():
            form.save()
            return redirect('profile')

    context={'form':form}
    return render(request,'update.html',context)





# advertiser history 
def advhistory(request):
    hist=Destination.objects.all()[::-1]
    return render(request, 'advhistory.html',{'hist':hist})
# about us of settings
def aboutus(request):
    return render(request,'aboutus.html')
def dashboard(request):
    balance=All.objects.all()
    return render(request,'paisadashboard.html',{'balance':balance})
def report(request):
    return render(request,'paisareport.html')
def referearn(request):
    return render(request,'referearn.html')
def advreport(request):
    post=Destination.objects.all()
    return render(request,'advreport.html',{'post':post})
def profile(request):
    all=All.objects.all()
    return render(request,'profile.html',{'all':all})


