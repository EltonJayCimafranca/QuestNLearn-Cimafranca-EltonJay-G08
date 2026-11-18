from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import views as auth_views

from .forms import RegistrationForm, ProfileForm


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Your QuestNLearn account has been created!'
            )
            return redirect('login')

    else:
        form = RegistrationForm()

    return render(request, 'accounts/register.html', {
        'form': form
    })


class CustomLoginView(auth_views.LoginView):

    template_name = 'accounts/login.html'

    def get_success_url(self):
        user = self.request.user

        if user.is_superuser or user.role == 'admin':
            return '/dashboard/admin/'

        return '/dashboard/student/'


@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(
            request.POST,
            instance=request.user
        )

        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Profile updated successfully!'
            )
            return redirect('profile')

    else:
        form = ProfileForm(instance=request.user)

    return render(request, 'accounts/profile.html', {
        'form': form
    })