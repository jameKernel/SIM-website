from django.db import models
from django.contrib.auth.models import User
# from embed_video.fields import EmbedVideoField
# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(name="Course Title", max_length=150)
    coast = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.CharField(name="Course ID", blank=False, max_length=200)
    date = models.DateTimeField(auto_now=True, auto_created=True)

    def __str__(self):
        return self.name


class Topic(models.Model):
    course = models.ForeignKey(Course, related_name="Course_title", on_delete=models.CASCADE)
    headline = models.CharField(max_length=200, blank=False)
    contents = models.TextField()
    image = models.ImageField(null=True, blank=True, upload_to="topics/%Y_%m_%s/")
    tags = models.ManyToManyField(Tag)
    slug = models.SlugField(name="Topic ID", max_length=350, blank=False)
    code_field = models.TextField(blank=True)
    #embedvd_link = models.EmbedVideoField(blank=True)

    def __str__(self):
        return self.headline

