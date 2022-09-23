"""SIM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import home
from Courses.views import courseListView, courseDetailView, topicDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='index'),
    path('courses/', courseListView.as_view(), name='courses'),
    path('courses/id=<int:pk>/', courseDetailView.as_view(), name="course_detail"),
    path('courses/<str:pk>/', topicDetailView.as_view(), name="topic_detail"),

]
