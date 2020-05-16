from django.contrib import admin

from .models import Courses, Student, ClassName

admin.site.register(Student)
admin.site.register(Courses)
admin.site.register(ClassName)
