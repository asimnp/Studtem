from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'father_name', 'mother_name', 'phone', 'class_name', 'course_enroll']


    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.fields['class_name'].empty_label = "Select Class"
        self.fields['course_enroll'].empty_label = "Select Course"