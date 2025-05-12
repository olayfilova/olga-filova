from django.db.models.functions import Lower
from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponse
from first_app.models import Department, Position


def homework_querysets(request):
    departments_with_managers= Department.objects.filter(positions__is_manager=True).order_by("name").distinct()

    active_positions_count= Position.objects.filter(is_active=True).count()
    print(f"Active positions count: {active_positions_count}")

    combined_positions= Position.objects.filter(Q(is_active=True)| Q(department__name='HR')).distinct()

    dept_names_with_managers=Department.objects.filter(positions__is_manager=True).values('name').distinct()

    sorted_positions=Position.objects.order_by(Lower('title'), 'title').values('title', 'is_active')

    context={
        'departments_with_managers': departments_with_managers,
        'active_positions_count': active_positions_count,
        'combined_positions': combined_positions,
        'dept_names_with_managers': dept_names_with_managers,
        'sorted_positions': sorted_positions,

    }

    return render(request, 'querysets_results.html', context)