from django.shortcuts import render
# from OrmApp.models import Student
# from OrmApp.forms import StudentForm
# from OrmApp.models import Movie
# from OrmApp.forms import MovieForm
# # Create your views here.
# def StudentsView(request):
#     if(request.method=="GET"):
#       data=Student.objects.all()
#       print(data)
#       stud_form=StudentForm()
#       render(request,"StudentsForm.html",{"form":stud_form,"students":data})

#     elif(request.method=="POST"):
#         stud_form=StudentForm(request.POST)
#         stud_form.save()
#         stud_form=StudentForm()
#         data=Student.objects.all()
#         print(data)
#         return render(request,"StudentsForm.html",{"form":stud_form,"students":data})

# def MovieView(request):
#   if(request.method=="GET"):
#         data=Movie.objects.all()
#         print(data)
#         mov_form=MovieForm()
#         return render(request,"MovieForm.html",{"form":mov_form,"movies":data})
#   elif(request.method=="POST"):
#          mov_form=MovieForm(request.POST)
#          mov_form.save()
#          mov_form=MovieForm()
#          data=Movie.objects.all()
#          print(data)
#          return render(request,"MovieForm.html",{"form":mov_form,"movies":data})

# def Uploadview(request):
#       form=MovieForm()
#       if request.method=="POST":
#             form=MovieForm(request.POST,request.FILES)
#             if form.is_valid():
#                   form.save()
#       return render(request,"uploadForm.html",context={'form':form})            

def ConsumeApiViews(request):
    return render(request,"ConsumeApi.html")   