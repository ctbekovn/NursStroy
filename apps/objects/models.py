from django.db import models

# Create your models here.
class Objects(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    floors = models.PositiveBigIntegerField(default=1)
    start = models.CharField(max_length=250)
    over = models.CharField(max_length=250)
    price = models.PositiveBigIntegerField(default=0)
    address = models.CharField(max_length=100)
    STATUS_OBJECT = (
        ('Строится', 'Строится'),
        ('Сдан в эксплуатацию', 'Сдан в эксплуатацию'),
    )
    status = models.CharField(choices=STATUS_OBJECT, max_length=255, default='Строится')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = "Объект"
        verbose_name_plural = "Объекты"
        ordering = ('-created', )

class ObjectsImages(models.Model):
    object = models.ForeignKey(Objects, on_delete=models.CASCADE, related_name="object_image")
    image = models.ImageField(upload_to = "objects_image/")