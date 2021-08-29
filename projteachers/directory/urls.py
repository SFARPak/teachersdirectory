from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.index, name ='index'),
    path('form/', views.form, name ='form'),
    path('bulk-upload/', views.bulk_upload, name='bulk_upload'),
    path('teacher-profile/', views.teacher_profile, name='teacher_profile'),
    path('teacher-add/', views.teacher_add, name='teacher_add'),
    path('teacher/<str:slug>', views.teacher_profile, name='teacher_profile'),
    path('teacher/<str:slug>/edit/', views.teacher_update, name='teacher_update'),
    path('teacher/<str:slug>/delete/', views.teacher_delete, name='teacher_delete'),
    path('login/', views.login_view, name ='login_view'),
    path('register/', views.register_view, name ='register_view'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    ]