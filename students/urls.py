# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_table, name='student_table'),  
    path('add/', views.add_student, name='add_student'),  
    path('edit/<int:student_id>/', views.edit_student, name='edit_student'),  
    path('delete/<int:student_id>/', views.delete_student, name='delete_student'),
    
]
