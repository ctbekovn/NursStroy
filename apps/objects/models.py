from tabnanny import verbose
from django.db import models

# Create your models here.
class Objects(models.Model):
    title = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    image = models.ImageField(upload_to = "objects_image/")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = "Объект"
        verbose_name_plural = "Объекты"
        ordering = ('-created', )