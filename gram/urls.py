from . import views
from django.urls import path, re_path

urlpatterns = [
    path('', views.index, name='gram-landing'),
    path('register/',views.register, name='registration'),
]