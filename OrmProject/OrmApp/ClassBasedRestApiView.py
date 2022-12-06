from OrmApp.Model import *
from OrmApp.models import *
from OrmApp.serializers import *
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status

class StudentClassApiView(APIView):
    def get(self,request,pk,format=None):
        student=Student.objects.get(pk=pk)
        serializers=StudentSerializers(student)
        return Response(serializers.data)

    def delete(self,request,pk,format=None):
        student=Student.objects.get(pk=pk)
        student.delete()
        return Response({"msg":"Deleted Successfully"})       

    def put(self,request,pk,format=None):
        student=Student.objects.get(pk=pk)
        serializers=StudentSerializers(student,data=request.data)
        if(serializers.is_valid()):
            serializers.save()
            return Response(serializers.data)  
        else:
            return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)         

class StudentAllClassApiView(APIView):
    def get(self,request,format=None):
        students=Student.objects.all()
        serializers=StudentSerializers(students,many=True)
        return Response(serializers.data)   

    def post(self,request,format=None):
        # student=Student.objects.get()
        serializers=StudentSerializers(data=request.data)
        if(serializers.is_valid()):
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)  
    
        
    


                 




