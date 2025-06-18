from django.db import models

class Position(models.Model):
    title=models.CharField(max_length=50)
    is_manager=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    department=models.ForeignKey('Department', on_delete=models.CASCADE)
    # salary=models.IntegerField(default=0)
    # salary = models.ForeignKey('Employee', on_delete=models.DO_NOTHING, related_name='salary')

    def __str__(self):
        return f'{self.title}({self.department})'

