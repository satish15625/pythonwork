
from django import forms  
from .models import *
#emp form

from dccApi.models import Employee  
class EmployeeForm(forms.ModelForm):  
    class Meta:  
        model = Employee 
        fields = ('id','eid', 'ename', 'eemail','econtact') 

        labels = {
            'eid':('Employee Id'),'ename':('Employee Name'),'eemail':('Employee Email'),'econtact':('Employee Contact')
        }

class UploadForm(forms.ModelForm):  
    class Meta:  
        model = UploadImages 
        fields = ['name', 'image_Img'] 

        