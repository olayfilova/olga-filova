from django.contrib import admin

from .models import Employee, Department, Position


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('username', 'email',  'position', 'hire_date')


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent_department')


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ("title", "is_manager", "is_active")