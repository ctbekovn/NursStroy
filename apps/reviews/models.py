from tabnanny import verbose
import venv
from django.db import models

# Create your models here.
class Rewiew(models.Model):
    comment = models.TextField()
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    image = models.ImageField(upload_to = "client_image")

    def __str__(self):
        return self.comment

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = ('-id',)