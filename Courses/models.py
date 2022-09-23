from django.db import models
from django.contrib.auth.models import User
from embed_video.fields import EmbedVideoField
from ckeditor.fields import RichTextField
from django.urls import reverse
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
    title = models.CharField(max_length=150)
    coast = models.ForeignKey(User, on_delete=models.CASCADE) # mg mg
    slug = models.CharField(blank=False, max_length=200)
    date = models.DateTimeField(auto_now=True, auto_created=True)
    # updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Topic(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    headline = models.CharField(max_length=200, blank=False)
    contents = RichTextField()
    category = models.ManyToManyField(Category, related_name="category", blank=True)
    tag = models.ManyToManyField(Tag, related_name="tag", blank=True)
    image = models.ImageField(null=True, blank=True, upload_to="topics/%Y_%m_%s/")
    topic_id = models.SlugField(max_length=350, blank=False)
    code_field = models.TextField(blank=True)
    youtube_link = EmbedVideoField(name="Youtube_Link ", blank=True)

    # def get_absolute_url(self):
    #     return reverse("course_detail", kwargs={"slug": self.topic_id})
    def __str__(self):
        return self.headline



