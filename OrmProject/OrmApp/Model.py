from django.db import models

# Create your models here.
class Student(models.Model):
    student_name=models.CharField(max_length=100)
    qualification=models.CharField(max_length=100)
    percentage=models.IntegerField()
    class Meta:
        db_table="tblstudent"
        ordering=["student_name"]
    def __str__(self):
        return self.student_name    