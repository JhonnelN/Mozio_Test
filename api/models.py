from django.db import models

# Create your models here.


class Provider(models.Model):
    name = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 150)
    phone_number = models.CharField(max_length = 50)
    language  = models.CharField(max_length = 50)
    currency = models.CharField(max_length = 10)

    def __str__(self):
        return self.name

class Area(models.Model):
    name = models.CharField(max_length = 50)
    providers_name = models.ForeignKey(Provider, on_delete=models.CASCADE, related_name="provider", null=False)
    price = models.DecimalField(max_digits = 7, decimal_places = 2)
    # Service area
    polygon = models.PolygonField()

    def __str__(self):