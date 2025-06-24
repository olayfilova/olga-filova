from django.db import models

from first_app.models import Employee


class Leave(models.Model):
    LEAVE_TYPES = (
        ('VACATION', 'vacation'),
        ('SICK_DAY', 'sick_day'),
        ('WEEKEND', 'weekend'),
        ('UNPAID_DAY', 'unpaid_day'),
        ('HOLIDAY', 'holiday')
    )

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    leave_type = models.CharField(max_length=10, choices=LEAVE_TYPES)

    def __str__(self):
        return f'{self.employee} - {self.leave_type} ({self.start_date} to {self.end_date})'
