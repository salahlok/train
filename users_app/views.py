from django.shortcuts import render, redirect
from .forms import CustomRegisterForm
from django.contrib import messages
from django.http import HttpResponse


def register(request):
    if request.method == "POST":
        register_form = CustomRegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, ("New User Created, Log to get started"))
            return redirect('register')

    else:
        register_form = CustomRegisterForm()
        return render(request, 'register.html', {'register_form': register_form})
