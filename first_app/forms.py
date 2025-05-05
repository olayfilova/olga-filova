from django import forms

from first_app.models import Employee, Company, Student




class EmployeeForm(forms.ModelForm):
    class Meta():
        model = Employee
        fields=('username', 'first_name', 'last_name', 'email','position')
        #fields=('username', 'first_name', 'last_name', 'position', 'email', 'phone_number', 'salary', 'hire_date', 'projects')


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'address', 'email', 'tax_code']


class StudentForm(forms.ModelForm):
    class Meta():
        model = Student
        fields=('first_name', 'last_name', 'email','phone_number')