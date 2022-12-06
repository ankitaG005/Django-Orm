from rest_framework import serializers
from OrmApp.Model import *
from OrmApp.models import *

class CustomerSerializers(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields=("customer_name","mobile_number","email_id","city_name")

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=("id","student_name","qualification","percentage")        