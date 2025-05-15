from django.core.management import BaseCommand
from django.utils import timezone

from first_app.models import MonthlySalary


class Command(BaseCommand):
    help='Set all salaries in this month are paid to True'

    def handler(self, *args, **options):
        current_month=timezone.now().month()
        current_year=timezone.now().year()

        salaries=MonthlySalary.objects.filter(date__month=current_month,
                                              date__year=current_year,
        count=salaries.count()                                      is_paid=False)
        salaries.update(is_paid=True)
        self.stdout.write(self.style.SUCCESS(f'command was successfully executed for{count} objects'))

