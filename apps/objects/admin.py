from django.contrib import admin
from apps.objects import models

# Register your models here.
class ObjectImageAdmin(admin.TabularInline):
    model = models.ObjectsImages
    extra = 1

class ObjectsAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']
    inlines = [ObjectImageAdmin]

admin.site.register(models.Objects, ObjectsAdmin)