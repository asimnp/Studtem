from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_students, name='student-home'),
    path('new/', views.new_student_form, name='student-form'),

    path('student/<int:id>/', views.single_student, name='student-one'),
    path('update/<int:id>/', views.update_student_form, name='student-update'),
    path('delete/<int:id>/', views.delete_student, name='student-delete'),
]