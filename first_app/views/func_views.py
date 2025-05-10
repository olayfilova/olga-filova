from django.db.models import Q
from django.urls import reverse
from first_app.models import Employee, Company, Student
from django.shortcuts import render, redirect, get_object_or_404

from first_app.forms import CompanyForm, EmployeeForm, StudentForm

#from first_app.models import company, student


def employee_list(request):
    employees=Employee.objects.all()
    search= request.GET.get('search')
    if search:
        employees=employees.filter(Q(first_name__icontains=search)
                                   | (Q(last_name__icontains=search))
                                   | Q(position__title__icontains=search))


    #all_employees=Employee.objects.filter().filter()
    # all_employees=Employee.objects.filter()
    # x=Employee.objects.filter()
    # y=Employee.objects.filter()
    # all_employees.filter()
    # all_employees.first()
    # all_employees.count()
    #return all_employees
    #return render(request, 'employee_list.html', {'employees': all_employees})
    context={
        "page_title": "...: Employee list",
        "employees": employees
    }
    return render(request, 'employee_list.html', context=context)

def employee_update(request, pk):
    employee=get_object_or_404(Employee, pk=pk)
    if request.method=="POST":
        form=EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect(reverse('employee_list'))
        return render(request, 'employee_update.html', {'form': form})
    else:
        form=EmployeeForm(instance=employee)
        return render(request, 'employee_update.html', {'form': form})


def employee_delete(request, pk):
    employee=get_object_or_404(Employee, pk=pk)
    if request.method=='POST':
        employee.delete()
        return redirect(reverse('employee_list'))
    return render(request, 'employee_confirm_delete.html', {'employee': employee})


def company_list(request):
    companies = Company.objects.all()
    return render(request, 'company_list.html', {'companies': companies})


def company_create(request):
    if request.method == "POST":
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('company_list.html'))
        return render(request, 'company_form.html', {'form': form})
    else:
        form = CompanyForm()
        return render(request, 'company_form.html', {'form': form})


def company_update(request, pk):
    company = get_object_or_404(Company, pk=pk)
    if request.method == "POST":
        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
            return redirect(reverse('company_list.html'))
        return render(request, 'company_form.html', {'form': form})
    else:
        form = CompanyForm(instance=company)
        return render(request, 'company_form.html', {'form': form})




def student_list(request):
    student = Student.objects.all()
    search = request.GET.get('search')
    if search:
        student = student.filter(Q(first_name__icontains=search)
                                     | (Q(last_name__icontains=search))
                                     | Q(email__icontains=search))
    return render(request, 'student_list.html', {'student': student})

def student_create(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('student_list'))
        return render(request, 'student_form.html', {'form': form})
    else:
        form = CompanyForm()
        return render(request, 'student_form.html', {'form': form})

def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect(reverse('student_list'))
        return render(request, 'student_form.html', {'form': form})
    else:
        form = CompanyForm(instance=student)
        return render(request, 'student_form.html', {'form': form})



def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect(reverse('student_list'))
    return render(request, 'student_confirm_delete.html', {'student': student})