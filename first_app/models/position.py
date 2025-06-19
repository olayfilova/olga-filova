from django.db import models

class Position(models.Model):
    title=models.CharField(max_length=50)
    is_manager=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    department=models.ForeignKey('Department', on_delete=models.CASCADE)
    monthly_rate=models.IntegerField(default=0)
    # Removing the problematic salary field

    def __str__(self):
        return f'{self.title}({self.department})'

