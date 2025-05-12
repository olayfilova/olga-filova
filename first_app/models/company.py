from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError


class Company(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=200)
    email=models.EmailField()
    tax_code=models.CharField(max_length=50)

    class Meta:
        verbose_name_plural='Companies'

    def save(self,*args, **kwargs):
        if not self.pk and Company.objects.exists():
            raise ValidationError("There can be only one Company")
        return super(Company, self).save(*args, **kwargs)


    def __str__(self):
        return self.name

