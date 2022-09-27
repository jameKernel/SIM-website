import requests
from requests import request
from django.shortcuts import render
from .models import Course, Topic, Category, Tag
from django.views.generic import ListView, DetailView
from django.views.generic.list import MultipleObjectMixin
from django.core.paginator import Paginator
# Create your views here.


class courseListView(ListView):
    model = Course
    metaclass = request
    template_name = 'courses/course_list.html'
    context_object_name = 'courses'
    paginate_by = 1
    queryset = None  # Course.objects.filter(category__name="Programming Language")
    extra_context = {  # other context
        'topics': Topic.objects.all,
        'tags': Tag.objects.all,
        'categories': Category.objects.all,
    }
    ordering = ['title']  # list ordering by title-name

    def get_queryset(self):
        self.queryset = Course.objects.filter(category__name=self.request.GET.get('q'))
        return self.queryset
    # def get_context_data(self, **kwargs):
    #     object_list = Course.objects.filter(category__name=self.queryset)
    #     context = super(courseListView, self).get_context_data(object_list=object_list, **kwargs)
    #     context['course'] = object_list
    #     print(context)
    #     return context

class courseDetailView(DetailView, MultipleObjectMixin):
    model = Course
    template_name = 'courses/course_detail.html'
    context_object_name = 'course'
    paginate_by = 1
    extra_context = {
        'categories': Category.objects.all,
    }

    # For Pagination from other object to detail_view_object
    def get_context_data(self, **kwargs):
        object_list = Topic.objects.filter(course=self.get_object() if self.get_object() != None else '')
        context = super(courseDetailView, self).get_context_data(object_list=object_list, **kwargs)
        print(context)
        return context


class topicDetailView(DetailView):
    model = Topic
    template_name = 'courses/topic_detail.html'
    context_object_name = 'topic'
    extra_context = {
        'topics': Topic.objects.all,
        'courses': Course.objects.all,
        'categories': Category.objects.all,
    }

