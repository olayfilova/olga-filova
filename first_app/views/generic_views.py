import logging
import datetime

from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.cache import cache
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy
from django.views.generic import ListView, FormView, DeleteView, CreateView, UpdateView, DetailView

from first_app.forms import EmployeeForm, SalaryForm
from first_app.models import Employee
from first_app.salary_calculator import CalculateMonthSalaryRate
from first_app.my_utils import is_user_superuser
from first_app.mixins import UserIsAdminMixin

from django.views.generic import TemplateView
from first_app.models import Company



logger = logging.getLogger('default')


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            company = Company.objects.first()
            context['company_logo'] = company.logo if company and company.logo else None
        except Company.DoesNotExist:
            context['company_logo'] = None
        return context


class EmployeeListView(ListView):
    model=Employee
    template_name='first_app/employee_list.html'
    context_object_name='employees'

    def get_queryset(self):
        queryset=super().get_queryset()
        search=self.request.GET.get('search', '')

        if search:
            queryset=queryset.filter(Q(first_name__icontains=search)
                                       | (Q(last_name__icontains=search))
                                       | Q(position__title__icontains=search))
        return queryset


class EmployeeCreateView(UserIsAdminMixin, CreateView):
    model=Employee
    form_class=EmployeeForm
    template_name='first_app/employee_form.html'
    success_url=reverse_lazy('employee_list')

    # def test_funk(self):
    #     return is_user_superuser(self.request.user)

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.warning(self.request, "Employee creates successfully")
        return response

    def form_invalid(self, form):
        messages.error(self.request, gettext_lazy("employee_create_error"))
        return super().form_invalid(form)


class EmployeeUpdateView(UserIsAdminMixin, UpdateView):
    model=Employee
    form_class=EmployeeForm
    template_name='first_app/employee_form.html'
    success_url=reverse_lazy('employee_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Employee updated successfully")
        return response

    def form_invalid(self, form):
        messages.error(self.request, gettext_lazy("employee_update_error"))
        return super().form_invalid(form)


class EmployeeDeleteView(UserIsAdminMixin, DeleteView):
    model=Employee
    template_name='first_app/employee_confirm_delete.html'
    success_url=reverse_lazy('employee_list')

    # def test_funk(self):
    #     return is_user_superuser(self.request.user)


class EmployeeDetailsView(UserIsAdminMixin, DetailView):
    model = Employee
    template_name = "first_app/employee_details.html"


    def get_object(self, queryset=None):
        e_id = self.kwargs.get("pk")
        employee = cache.get(f"employee_{e_id}")
        if not employee:
            logger.warning(f"Employee {e_id} NOT IN CACHE")
            employee = get_object_or_404(Employee, pk=e_id)
            cache.set(f"employee_{e_id}", employee, timeout=60)
        else:
            logger.info(f"Employee {e_id} WAS IN CACHE")

        return employee





# class SalaryCalculatorView(UserPassesTestMixin, FormView):
#     template_name='salary_calculator.html'
#     form_class=SalaryForm
#     success_url=reverse_lazy('salary_calculator')
#
#     def test_func(self):
#         #return is_user_superuser()
#         return is_user_superuser(self.request.user)
#
#     # def form_valid(self, form):
#     #     days_dict=form.cleaned_data
#     #     salary=CalculateMonthSalaryRate(days_dict)
#     #     return super().form_valid(form)
#
#
#     def get(self, request, *args ,**kwargs):
#         form=self.form_class()
#         # context=super().get_context_data(**kwargs)
#         # context['salary']=salary
#         # return context
#         return render(request, self.template_name, {'form': form})
#
#     def form_valid(self, form):
#         cleaned_data=form.cleaned_data
#         employee=cleaned_data.get('employee')
#
#         calc=CalculateMonthSalaryRate(employee=employee)
#         #days={day: day_type for day, day_type in cleaned_data.items() if day not in ['employee', 'csrfmiddlewaretoken']}
#         days={day: day_type for day, day_type in cleaned_data.items() if day.startswith('day_')}
#
#         salary=calc.calculate_salary(days_dict=days)
#         calc.save_salary(salary, datetime.date.today())
#
#
#         return render(request=self.request,
#                       template_name=self.template_name,
#                       context={'form': form, 'calculated_salary': salary})



class SalaryCalculatorView(UserIsAdminMixin, FormView):
    template_name = "salary_calculator.html"
    form_class = SalaryForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, context={'form': form})


    def form_valid(self, form):
        cleaned_data = form.cleaned_data
        employee = cleaned_data.get("employee")


        calc = CalculateMonthSalaryRate(employee=employee)
        days = {day: day_type for day, day_type in cleaned_data.items() if day.startswith("day_")}

        salary = calc.calculate_salary(days_dict=days)
        calc.save_salary(salary, datetime.date.today())
        return render(
            request=self.request,
            template_name=self.template_name,
            context={'form': form, 'calculated_salary': salary}
        )


