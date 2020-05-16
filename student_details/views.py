from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Student
from .forms import StudentForm

# new_student_form
def new_student_form(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'New student account created!')
            return redirect('student-home')
    else:
        form = StudentForm()

    return render(request, 'student_details/s_form.html', {'form': form})


# all_students
def all_students(request):
    students = Student.objects.all().order_by('-date')
    context = {'students': students}

    return render(request, 'student_details/s_home.html', context)

# single_student
def single_student(request, id):
    student = Student.objects.get(pk=id)
    context = {'student': student}

    return render(request, 'student_details/s_one.html', context)


def delete_student(request, id):
    student = Student.objects.get(pk=id)
    student.delete()
    messages.info(request, 'Student account deleted!')


    return redirect('student-home')


# update_student_form
def update_student_form(request, id):
    student = Student.objects.get(pk=id)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.warning(request, 'Student account updated!')
            return redirect('student-home')
    else:
        form = StudentForm(instance=student)

    return render(request, 'student_details/s_form.html', {'form': form})