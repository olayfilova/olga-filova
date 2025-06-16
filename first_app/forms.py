from django import forms
#from django.contrib.gis.gdal import field
from django.forms import ChoiceField

from first_app.models import Employee, Company, Student
import calendar
from datetime import date

from first_app.common.enums import WorkDayEnum


class EmployeeForm(forms.ModelForm):
    class Meta():
        model = Employee
        fields=('username', 'first_name', 'last_name', 'email','position')
        #fields=('username', 'first_name', 'last_name', 'position', 'email', 'phone_number', 'salary', 'hire_date', 'projects')

class SalaryForm(forms.Form):
    employee=forms.ModelChoiceField(queryset=Employee.objects.all())
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        today=date.today()
        week_day, num_days=calendar.monthrange(today.year, today.month)
        for day in range(1,num_days+1):
            day_coord=today.year, today.month, day
            weekday=calendar.weekday(*day_coord)
            weekday_name=calendar.day_name[weekday]

            #field_name=f'day_{day}, {weekday_name}'
            field_name=f'day_{day}'


            if calendar.weekday(today.year, today.month)>=5:
                self.field[field.name]=ChoiceField(label=f'{day} - {weekday_name}',
                                                   # choices=[(0, '0'), (8, '8')])
                                                   choices=[(WorkDayEnum.WEEKEND.name, WorkDayEnum.WEEKEND.value)],
                                                    initial=WorkDayEnum.WEEKEND.value)
            else:
                self.field[field.name]=ChoiceField(label=f'{day} - {weekday_name}',
                                                   choices=[(option.name, option.value) for option in WorkDayEnum],
                                                   # choices=[(WorkDayEnum.WORKING_DAY.name, WorkDayEnum.WORKING_DAY.value),
                                                   #          (WorkDayEnum.VACATION.name, WorkDayEnum.VACATION.value),
                                                   #          (WorkDayEnum.SICK_DAY.name, WorkDayEnum.SICK_DAY.value),
                                                   #          (WorkDayEnum.UNPAID_DAY.name, WorkDayEnum.UNPAID_DAY.value)],
                                                    initial=WorkDayEnum.WORKING_DAY.value)


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'address', 'email', 'tax_code']


class StudentForm(forms.ModelForm):
    class Meta():
        model = Student
        fields=('first_name', 'last_name', 'email','phone_number')