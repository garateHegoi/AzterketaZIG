from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone

# Create your models here.
class Kotxea(models.Model):
    id = models.AutoField(primary_key=True)
    izena = models.CharField(max_length=50)
    marka = models.CharField(max_length=100)
    data = models.CharField(max_length=50)
    def __str__(self):
        return u'%s'%self.izena


class Pertsona(models.Model):
    id =  models.AutoField(primary_key=True)
    izena = models.CharField(max_length=50)
    abizena = models.CharField(max_length=50)
    id_kotxea =  models.ForeignKey(Kotxea, on_delete=models.CASCADE)

    def __str__(self):
        return u'%s'%self.id_kotxea + u'%s'%self.id