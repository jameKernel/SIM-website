from django.db import models
from django.contrib.auth.models import User
from embed_video.fields import EmbedVideoField
from ckeditor.fields import RichTextField
from django.utils.text import slugify  # auto slug
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
    category = models.ManyToManyField(Category, related_name='courses', blank=True)
    coast = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.CharField(blank=True, max_length=200)
    date = models.DateTimeField(auto_now=True, auto_created=True)

    def save(self, *args):
        self.slug = slugify(self.title)
        super(Course, self).save()

    def __str__(self):
        return self.title


class Topic(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    headline = models.CharField(max_length=200, blank=False)
    contents = RichTextField()
    category = models.ManyToManyField(Category, related_name='topic', blank=True)
    image = models.ImageField(null=True, blank=True, upload_to="topics/%Y_%m_%s/")
    order = models.IntegerField(blank=False, null=True)
    slug = models.SlugField(blank=True)
    # youtube_link = EmbedVideoField(name="Youtube_Link ", blank=True)
    # embed_Video = models.URLField()

    def save(self, *args):
        self.slug = slugify(self.headline)
        print(self.slug)
        super(Topic, self).save()

    def __str__(self):
        return self.headline



