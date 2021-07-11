from django.contrib import admin
from .models import Employee

admin.site.site_header  =  "Skillup Rest Api"  
admin.site.site_title  =  "Skillup Rest Api"
admin.site.index_title  =  "Skiilup Rest Api Details"

# Register your models here.
admin.site.register(Employee)