from django.urls import path
from . import views
from .views import *

from DCC.settings import *
from DCC.settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static

urlpatterns = [
    path('',login.as_view(), name= 'login'),
    path('register/',views.register, name='register'),
    path('dashboard/', views.dashboard, name = 'index'),
    path('add/',views.add),
    path('show/',views.show),  
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.destroy),
    path('imageUpload/',views.uploadImage, name="uploadImage"),
    path('success/', success, name = 'success'),
    path('list_images/', display_images, name = 'display_images')
    

]
#DCC
if DEBUG:
    urlpatterns += static(STATIC_URL, document_root = STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)


