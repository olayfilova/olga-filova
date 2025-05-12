from django.db import models
from .course import Course


class Student(models.Model):
    class Meta:
        db_table = 'it_students'

    #id = models.IntegerField(primary_key=True)
    first_name = models.TextField(max_length=100)
    last_name = models.TextField(max_length=100)
    completed_lessons = models.IntegerField()
    birth_date = models.DateField()
    avatar = models.ImageField(upload_to='avatars')
    email = models.EmailField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    phone_number=models.CharField(max_length=115, blank=True, null=True)


    def __str__(self):
        return f'{self.first_name} {self.last_name}({self.course})'
