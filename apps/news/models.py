from distutils.command.upload import upload
from tabnanny import verbose
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()    
    image = models.ImageField(upload_to = "news_image/")
    created = models.DateTimeField(auto_now_add=True)

    def str__(self):
        return self.title 

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ('-created', )