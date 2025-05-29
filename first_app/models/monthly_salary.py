from django.db import models



class MonthlySalary(models.Model):
    date=models.DateField()
    salary=models.IntegerField()
    bonus=models.IntegerField(null=True, blank=True)
    employee=models.ForeignKey('Employee', on_delete=models.DO_NOTHING)
    is_paid=models.BooleanField(default=False)

###
class CalculateMonthSalaryRate:
    def __init__(self, employee):
        self.employee = employee
        self.base_rate = employee.position.monthly_rate  # Make sure this exists

    def calculate_salary(self, days_dict):
        # Your calculation logic here
        # Example:
        working_days = sum(1 for day_type in days_dict.values() if day_type == 'WORK')
        total_days = len(days_dict)

        if total_days == 0:
            return 0

        daily_rate = self.base_rate / 30  # assuming 30 days month
        calculated_salary = daily_rate * working_days

        return round(calculated_salary, 2)

    def save_salary(self, amount, date):
        # If you have a SalaryHistory model:
        SalaryHistory.objects.create(
            employee=self.employee,
            amount=amount,
            effective_date=date
        )
###


# class SalaryHistory(models.Model):
#     employee = models.ForeignKey('Employee', on_delete=models.CASCADE, related_name='salary_history')
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     effective_date = models.DateField()
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         ordering = ['-effective_date']
