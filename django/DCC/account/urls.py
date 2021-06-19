'''
File name : urls.py
Author : Satish Kumar 
Description :  urls.py is used for make url pattern for make page connection and redirection.
'''

from django.urls import path
from .import views 
from .views import login
urlpatterns = [
    # path("register", views.register ,name="register"),
    path('login',login.as_view(), name= 'login'),
    path("logout",views.logout, name="logout"),
    path("register",views.register, name="register"),
    path("password",views.password,name="password")

]