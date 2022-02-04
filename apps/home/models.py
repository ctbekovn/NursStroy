from django.db import models

# Create your models here.
class Setting(models.Model):
    title = models.CharField(max_length=150)
    logo = models.ImageField(blank=True,upload_to='images/')
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    address = models.CharField(blank=True,max_length=100)
    phone = models.CharField(blank=True,max_length=15)
    email = models.CharField(blank=True,max_length=50)
    
    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = "Настройка"
        verbose_name_plural = "Настройки"
        