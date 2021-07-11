from django.urls import include, path
from rest_framework import routers
from . import views
from rest_framework.routers import DefaultRouter
from .views import RegisterAPI
router = routers.DefaultRouter()
router.register(r'emp', views.EmpViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('register/', RegisterAPI.as_view(), name='register'),
]