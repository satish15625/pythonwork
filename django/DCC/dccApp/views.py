from django.shortcuts import render, redirect
from django.http import HttpResponse
from dccApp.forms import * 
from dccApi.models import Employee  
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth  #user login auth
from django.views import View

#login page 
#DCC Dashboard
   
class login(View):

    #get function load the page 
    def get(self, request):
        return render(request, 'dashboard/login.html')
    
    #post function submit the Login Form
    def post(self,request):
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                request.session.set_expiry(1000)
                return redirect('/dashboard')
            else:
                messages.info(request,'invalid User name or Password Please try Again')
                return redirect('login')
        else:
            return render(request,'dashboard/login.html')
   
@login_required(login_url='/')
def register(request):

    return render(request, 'dashboard/register.html')
    
@login_required(login_url='/')
def dashboard(request):

    return render(request, 'dashboard/index.html')

@login_required(login_url='/')
def add(request):
    if request.method == "POST":  
        form = EmployeeForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = EmployeeForm()  
    return render(request,'dashboard/add.html',{'form':form})  

@login_required(login_url='/')
def show(request):  
    employees = Employee.objects.all()  
    return render(request,"dashboard/show.html",{'employees':employees})  

@login_required(login_url='/')
def edit(request, id):  
    employee = Employee.objects.get(id=id)  
    return render(request,'dashboard/edit.html', {'employee':employee})  

@login_required(login_url='/')
def update(request, id):  
    employee = Employee.objects.get(id=id)  
    form = EmployeeForm(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'employee': employee})  

@login_required(login_url='/')
def destroy(request, id):  
    employee = Employee.objects.get(id=id)  
    employee.delete()  
    return redirect("/show")



@login_required(login_url='/')
def uploadImage(request):

    if request.method == 'POST': 
        form = UploadForm(request.POST, request.FILES) 
  
        if form.is_valid(): 
            form.save() 
            return redirect('success') 
    else: 
        form = UploadForm() 
    
    return render(request,'dashboard/uploadImage.html',{'form' : form})

def success(request): 
    return HttpResponse('successfully uploaded')



def display_images(request): 
  
    if request.method == 'GET': 
  
        # getting all the objects of hotel. 
        images = UploadImages.objects.all()
        print("Satish",images)
        return render(request, 'dashboard/imagesList.html',{'all_images' : images})



