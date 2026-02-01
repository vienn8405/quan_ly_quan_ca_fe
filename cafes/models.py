from django.db import models

# Create your models here.
class CafeShop(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name