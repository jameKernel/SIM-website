from django.contrib import admin
from .models import Course, Category, Topic, Tag
# Register your models here.

admin.site.register(Category)
admin.site.register(Tag)

class AdminInlineTopic(admin.TabularInline):
    model = Topic
@admin.register(Course)
class adminCourse(admin.ModelAdmin):

    inlines = [
        AdminInlineTopic
    ]