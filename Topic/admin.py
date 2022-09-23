from django.contrib import admin
from . import models


# Register your models here.
admin.site.register(models.Category)
admin.site.register(models.Body)
admin.site.register(models.ImagesField)
admin.site.register(models.Topic)

# class AdminInlineContent(admin.TabularInline):
#     model = models.Content
#
#
# class AdminInlineImgField(admin.StackedInline):
#     model = models.ImagesField
#     parent_model = AdminInlineContent
#
#
# class AdminInlineBody(admin.StackedInline):
#     model = models.Body
#     parent_model = AdminInlineContent
#
#
# @admin.register(models.Topic)
# class AdminTopic(admin.ModelAdmin):
#     inlines = [
#         AdminInlineContent
#     ]
