from django.urls import path
from django.urls.resolvers import URLPattern
from api import views

urlpatterns = [
    path('student/', views.StudentList.as_view()),
]    