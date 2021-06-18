from django.contrib import admin
from django.contrib.auth.models import Group
from dccApi.models import *
# Register your models here.

admin.site.site_header = "DCC APP ADMIN"

# Register your models here.
admin.site.register(Employee)
admin.site.register(Person)
admin.site.register(UploadImages)
