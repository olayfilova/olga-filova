from django.core.management.base import BaseCommand
from first_app.models.employee import Employee
from django.db import transaction
import logging

logger=logging.getLogger(__name__)

class Command(BaseCommand):
    help='sets all the employees to active status(is_active=True)'

    def add_arguments(self, parser):
        parser.add_argument(
            '--dry-run',
            action='store_true',
            help='run the command in the dry mode',
        )

    def handle(self, *args, **options):
        try:
            with transaction.atomic():
                inactive_count=Employee.objects.filter(is_active=False).count()


                if inactive_count==0:
                    self.stdout.write(self.style.SUCCESS('No inactive employees found./n All employees are already active. No changes needed.'))
                    return

                if options['dry-run']:
                    self.stdout.write(self.style.WARNING('dry run: would activate{inactive_count} employees')
                                      )
                    return
                updated=Employee.objects.filter(is_active=False).update(is_active=True)
                self.stdout.write(self.style.SUCCESS(f'successfully activated{updated} employees')
                                  )
                logger.info(f'activated employees: {updated}')

        except Exception as e:
            self.stdout.write(self.style.ERROR(f' error activating employees:{str(e)}')
                             )

            logger.error(f'error activating employee command:{str(e)}')
            raise e