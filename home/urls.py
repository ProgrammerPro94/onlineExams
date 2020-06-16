from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('start_test/', views.start_test),
    path('', views.home),
    path('logout/', views.logout_user),
    path('login/', views.login_user),
    path('register/', views.register_user),
    path('make_test/', views.make_test),
    path('test_info/', views.test_info),
    path('results/', views.result_display),
    path('delete_test/', views.delete_test)
]