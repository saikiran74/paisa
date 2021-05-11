from django.urls import path

from . import views

urlpatterns=[
    path('',views.landingpage, name='landingpage'),
    path('createaccount',views.createaccount,name='createaccount'),
    path('login',views.login,name='login')
]