from rest_framework import generics
from OrmApp.models import *
from OrmApp.Model import *
from OrmApp.serializers import *

class CustomerApiViews(generics.ListCreateAPIView):
    queryset=Customer.objects.all()
    serializer_class=CustomerSerializers

class StudentApi(generics.ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers   
