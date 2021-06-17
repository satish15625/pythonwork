from django.urls import path
#import for django statci file lib.
from django.conf import settings
from django.conf.urls.static import static
from mainApp import views

urlpatterns = [
    path('', views.home, name='index'),
    path('shop/', views.shop, name='shop'),
    path('course/', views.course, name='course'),
    path('blog1/', views.blog1, name='blog1'),
    path('singal/', views.singal, name='singal'),
    path('blog4/', views.blog4, name='blog4'),
    path('marketing/', views.marketing, name='marketing'),
    path('development/', views.development, name='development'),
    path('business/', views.business, name='business'),
    path('maths/', views.maths, name='maths'),
    path('about/', views.about, name='about'),
    path('course1/', views.course1, name='course'),
    path('course2/', views.course2, name='course'),
    path('course3/', views.course3, name='course'),
    path('course4/', views.course4, name='course'),
    path('course5/', views.course5, name='course'),
    path('video/', views.video, name='video'),
    path('faq/', views.faq, name='faq'),
    path('tems/', views.tems, name='tems'),
    

    ]  

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#for debug folder is exist or not if not create new file in media folder 
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
