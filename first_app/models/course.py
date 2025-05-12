from django.db import models


class Course(models.Model):
    name=models.CharField(max_length=100)
    description =models.TextField(max_length=1000)
    learning_plan=models.TextField(blank=True, null=True)





