from django.db.models.signals import pre_save
from django.dispatch import receiver
from first_app.models import Department


@receiver(pre_save, sender=Department)
def capitalize_department_name(sender, instance, **kwargs):
    if instance.name:
        instance.name = instance.name.capitalize()