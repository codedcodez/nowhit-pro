from django.shortcuts import render, redirect
from django.contrib import messages

from .models import UserProfile

from .forms import UserForm, UserProfileForm


def register(request):

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            
            messages.success(request, "Your registration was successful")

            return redirect('login')

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }

    return render(request, 'miners_account/register.html', context)
