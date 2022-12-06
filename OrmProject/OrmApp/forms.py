from django.forms import ModelForm
from OrmApp.models import Student
from OrmApp.models import Movie
class StudentForm(ModelForm):
    class Meta:
        Model=Student
        # fields="__all__"
        fields=["student_name","qualification","city"]

class MovieForm(ModelForm):
    class Meta:
        model=Movie
        fields=["file","image"]    