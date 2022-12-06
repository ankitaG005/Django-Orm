from django.db import models

# Create your models here.
# class Student(models.Model):
#     student_name=models.CharField(max_length=100)
#     qualification=models.CharField(max_length=100)
#     city=models.CharField(max_length=100)

# class Movie(models.Model):
#     file=models.FileField(upload_to='OrmApp/static/documents/')
#     image=models.ImageField(upload_to='OrmApp/static/images/')  
#     #class Meta:
    #    db_table="tblmovies"

class Customer(models.Model):
    customer_name=models.CharField(max_length=100)
    mobile_number=models.CharField(max_length=100)
    email_id=models.CharField(max_length=100)
    city_name=models.CharField(max_length=100)
    class Meta:
        db_table="tblCustomer"
        ordering=["customer_name"]    
