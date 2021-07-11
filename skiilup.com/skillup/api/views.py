# views.py
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.response import Response
from .serializers import UserSerializer, RegisterSerializer
from .serializers import EmpSerializer
from rest_framework.response import Response
from rest_framework import authtoken

from .models import Employee



# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": authtoken.objects.create(user)[1]
        })


class EmpViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all().order_by('name')
    serializer_class = EmpSerializer