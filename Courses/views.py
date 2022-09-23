from django.shortcuts import render
from .models import Course, Topic, Category, Tag
from django.views.generic import ListView, DetailView


# Create your views here.

class courseListView(ListView):
    model = Course
    template_name = 'courses/main.html'
    context_object_name = 'courses'
    extra_context = {  # other context
        'topics': Topic.objects.all,
        'tags': Tag.objects.all,
        'categories': Category.objects.all,
    }
    ordering = ['title']  # list ordering by title-name


class courseDetailView(DetailView):
    model = Course
    template_name = 'courses/course_detail.html'
    context_object_name = 'course'
    extra_context = {
        'tags': Tag.objects.all,
        'categories': Category.objects.all,
    }

class topicDetailView(DetailView):
    model = Topic
    template_name = 'courses/topic_detail.html'
    context_object_name = 'topic'
    extra_context = {
        'courses': Course.objects.all,
        'categories': Category.objects.all,
    }
# Change the CourseListView as table template