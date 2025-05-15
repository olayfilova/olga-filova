from django import forms
#from django.contrib.gis.gdal import field
from django.forms import ChoiceField

from first_app.models import Employee, Company, Student, Leave
import calendar
from datetime import date

from first_app.common.enums import WorkDayEnum


class LeaveForm(forms.ModelForm):
    class Meta:
        model = Leave
        fields = ['employee', 'start_date', 'end_date', 'leave_type']

        widgets = {
            'employee': forms.Select(attrs={'class': 'form-select'}),
            'start_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'end_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'leave_type': forms.Select(attrs={'class': 'form-select'}),
        }



    def clean_employee(self):
        employee = self.cleaned_data.get('employee')
        if not employee:
            raise forms.ValidationError("Employee selection is required")
        return employee

    def clean(self):
        cleaned_data = super().clean()
        employee = cleaned_data.get('employee')
        leave_type = cleaned_data.get('leave_type')

        if employee and leave_type:
            if leave_type == 'SICK':
                sick_days_count = Leave.objects.filter(
                    employee=employee,
                    leave_type='SICK'
                ).count()

                if sick_days_count>=5:
                    raise forms.ValidationError("Employee has exceeded the maximum limit of 5 sick days")

        if leave_type == "HOLIDAY":
            holiday_days_count = Leave.objects.filter(
                employee=employee,
                leave_type = 'HOLIDAY'
            ).count()

            if holiday_days_count >=3:
                raise forms.ValidationError("Employee has exceeded the maximum limit of 3 holiday days")


        return cleaned_data



class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields=('username', 'first_name', 'last_name', 'email','position', 'salary')
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


            if calendar.weekday(today.year, today.month, day)>=5:
                self.fields[field_name]=ChoiceField(label=f'{day} - {weekday_name}',
                                                   # choices=[(0, '0'), (8, '8')])
                                                   choices=[(WorkDayEnum.WEEKEND.name, WorkDayEnum.WEEKEND.value)],
                                                    initial=WorkDayEnum.WEEKEND.value)
            else:
                self.fields[field_name]=ChoiceField(label=f'{day} - {weekday_name}',
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
    class Meta:
        model = Student
        fields=('first_name', 'last_name', 'email','phone_number')



