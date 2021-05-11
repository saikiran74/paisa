from django.urls import path

from . import views

urlpatterns=[
    path('',views.landingpage, name='landingpage'),
    path('createaccount',views.createaccount,name='createaccount'),
    path('login',views.login,name='login'),
    path('index',views.index, name='index'),
    path('withdraw',views.withdraw,name='withdraw'),
    path('advertise',views.advertise,name='advertise'),
    path('advdashboard',views.advdashboard,name='advdashboard'),
    path('privacypolicy',views.privacypolicy,name='privacypolicy'),
    path('termsandcondition',views.termsandcondition,name='termsandcondition'),
    path('contactus',views.contactus,name='contactus'),
    path('update',views.update,name='update'),
    path('advhistory',views.advhistory,name='advhistory'),
    path('aboutus',views.aboutus,name='aboutus'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('report',views.report,name='report'),
    path('referearn',views.referearn,name='referearn'),
    path('advreport',views.advreport,name='advreport'),
    path('profile',views.profile,name='profile'),
]