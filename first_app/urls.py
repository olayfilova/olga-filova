from django.urls import path
from first_app.views import func_views, generic_views



urlpatterns=[
    # path('employees/', func_views.employee_list, name='employee_list'),
    path('employees/', generic_views.EmployeeListView.as_view(), name='employee_list'),
    # path('employees_1/', func_views.employee_list, name='employee_list'),
    # path('employees_2/', func_views.employee_list, name='employee_list'),
    # path('employees_3/', func_views.employee_list, name='employee_list'),
    # path('employees/update/<int:pk>', func_views.employee_update, name='employee_update'),
    path('employees/update/<int:pk>', generic_views.EmployeeUpdateView.as_view(), name='employee_update'),
    path('employees/delete/<int:pk>', func_views.employee_delete, name='employee_delete'),
    #path('employees/', func_views.employee_list, name='employee_list'),

    path('companies/', func_views.company_list, name='company_list'),
    path('companies/create/', func_views.company_create, name='company_create'),
    path('companies/update/<int:pk>/', func_views.company_update, name='company_update'),
    path('students/', func_views.student_list, name='student_list'),
    path('students/update/<int:pk>', func_views.student_update, name='student_update'),
    path('students/create/<int:pk>', func_views.student_create, name='student_create'),
    path('students/delete/<int:pk>', func_views.student_delete, name='student_delete'),
    path('querysets/', func_views.queryset, name='queryset'),
    path('salary_calculator/', generic_views.SalaryCalculatorView.as_view(), name='salary_calc')
]