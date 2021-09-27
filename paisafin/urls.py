from django.urls import path

from . import views

urlpatterns=[
    path('',views.landingpage, name='landingpage'),
    path('createaccount',views.createaccount,name='createaccount'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('index',views.index, name='index'),
    path('advertise/<str:pk>',views.advertise,name='advertise'),
    path('advdashboard',views.advdashboard,name='advdashboard'),
    path('pay/<str:pk>',views.pay,name='pay'),
    path('privacypolicy',views.privacypolicy,name='privacypolicy'),
    path('termsandcondition',views.termsandcondition,name='termsandcondition'),
    path('contactus',views.contactus,name='contactus'),
    path('update/<str:pk>',views.update,name='update'),
    path('advhistory',views.advhistory,name='advhistory'),
    path('aboutus',views.aboutus,name='aboutus'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('sell/<str:pk>',views.sell,name='sell'),
    path('withdrawmoney/<str:pk>',views.withdrawmoney,name='withdrawmoney'),
    path('report',views.report,name='report'),
    path('referearn',views.referearn,name='referearn'),
    path('advreport',views.advreport,name='advreport'),
    path('profile',views.profile,name='profile'),
    path('search',views.search,name='search'),
    path('followers',views.followers,name='followers'),
    path('like',views.like,name='like'),
    path('visit/<int:pk>/',views.visit,name='visit'),
    path('silverbazar',views.silverbazar,name='silverbazar'),
    path('paisamoney/<str:pk>',views.paisamoney,name='paisamoney'),
    path('comment',views.comment,name='comment'),
]