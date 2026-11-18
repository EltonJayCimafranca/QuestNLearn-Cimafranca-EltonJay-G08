from django.shortcuts import render
from django.contrib.auth.decorators import (
    login_required,
    user_passes_test
)


def is_admin(user):
    return user.is_superuser or user.role == 'admin'


def is_student(user):
    return user.role == 'student' and not user.is_superuser


@login_required
@user_passes_test(is_student, login_url='login')
def student_dashboard(request):
    return render(
        request,
        'dashboard/student_dashboard.html'
    )


@login_required
@user_passes_test(is_admin, login_url='login')
def admin_dashboard(request):
    return render(
        request,
        'dashboard/admin_dashboard.html'
    )