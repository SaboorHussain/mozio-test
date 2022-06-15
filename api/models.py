# from django.db import models
from django.contrib.gis.db import models
from django.utils.translation import gettext as _
# Create your models here.


class Provider(models.Model):

    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    currency = models.CharField(max_length=50)

    class Meta:
        verbose_name = _("Provider")
        verbose_name_plural = _("Providers")

    def __str__(self):
        return self.name


class ServiceArea(models.Model):

    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    location = models.PolygonField()

    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("ServiceArea")
        verbose_name_plural = _("ServiceAreas")

    def __str__(self):
        return self.name
