from django.db import models
from django.contrib.auth.models import User
from embed_video.fields import EmbedVideoField
from ckeditor.fields import RichTextField

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Topic(models.Model):
    category = models.ManyToManyField(Category, blank=True)
    title = models.CharField(max_length=300, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now=True, auto_created=True)

    def __str__(self):
        return self.title


class Content(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    headline = models.CharField(max_length=350)
    select = models.CharField(max_length=350, blank=True)  # mean <div id="{{select}}"> </div>

    def __str__(self):
        return self.headline


class Body(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    iframe = EmbedVideoField(blank=True)
    text = RichTextField(blank=True)

    def __str__(self):
        return str(self.content) + "'s body"


class ImagesField(models.Model):
    body = models.ForeignKey(Content, on_delete=models.CASCADE)
    img = models.ImageField(upload_to="media/")
    caption = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.caption
