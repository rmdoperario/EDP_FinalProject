from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import StudentForm
from .models import Student

'''
def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            student = Student(
                first_name=form.cleaned_data["first_name"],
                last_name=form.cleaned_data["last_name"],
                course=form.cleaned_data["course"],
                gender=form.cleaned_data["gender"],
                age=form.cleaned_data["age"],
            )
            student.save()
            return HttpResponse(f"Thank you, {first_name}")
    else:
        form = StudentForm()
    
    context = {"form": form}
    return render(request, "student_form.html", context)
'''

def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            student = Student(
                first_name=form.cleaned_data["first_name"],
                last_name=form.cleaned_data["last_name"],
                course=form.cleaned_data["course"],
                gender=form.cleaned_data["gender"],
                age=form.cleaned_data["age"],
            )
            student.save()
            return redirect('student_table')
    else:
        form = StudentForm()
    
    context = {"form": form}
    return render(request, "student_form.html", context)

def edit_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_table')
    else:
        form = StudentForm(instance=student)
    return render(request, 'student_edit.html', {'form': form})

def student_table(request):
    students = Student.objects.all()
    context = {'students': students}
    return render(request, 'student_table.html', context)

def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    student.delete()
    return redirect('student_table')