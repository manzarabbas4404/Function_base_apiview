
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('student_api/',views.student_api),
    path('student_api/<int:pk>',views.student_api)
    
]
