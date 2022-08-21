from django.shortcuts import render
from .models import Course, Topic, Category, Tag
# Create your views here.
def courses(request):
    context = {
        'courses': Course.objects.all,
        'topics': Topic.objects.all,
        'tags': Tag.objects.all,
        'categories': Category.objects.all
    }
    return render(request, 'courses/main.html', context)