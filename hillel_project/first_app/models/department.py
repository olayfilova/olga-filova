from django.db import models
from django.utils.functional import cached_property
from django.utils.translation import gettext_lazy as _


class Department(models.Model):
    name = models.CharField(verbose_name=_("Департамент"), max_length=200)
    parent_department = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)

    @cached_property
    def position_count(self):
        return self.position_set.filter(is_active=True).count()

    def __str__(self):
        return self.name