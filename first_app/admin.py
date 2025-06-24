from django.contrib import admin
from .models import Employee, Department, Position
from django.contrib import admin
from .models import Student, Course, Company


# Register your models here.


def connect_to_db():
    pass


class DbConnection:
    obj=None
    def __new__(cls, *args, **kwargs):
        if cls.obj is None:
            return cls.obj
        else:
            super().__new__()

    def __init__(self):
        DbConnection.obj=self
        connect_to_db()


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display=('username', 'position', 'email', 'hire_date')

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display=('name', 'parent_department')


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display=('title', 'is_manager', 'is_active')




@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone_number']  # adjust fields as needed
    search_fields = ['first_name', 'last_name', 'phone_number']

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'tax_code']

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'learning_plan']


