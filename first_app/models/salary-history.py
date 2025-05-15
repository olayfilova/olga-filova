


class SalaryHistory(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='salary_records')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    calculation_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-calculation_date']

    def __str__(self):
        return f"Salary for {self.employee} - {self.calculation_date}"
