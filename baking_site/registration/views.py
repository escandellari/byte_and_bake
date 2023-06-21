from typing import Any, Optional

# from django.contrib.auth.forms import UserChangeForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.db import models
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .forms import EditProfileForm, PasswordChangingForm, SignUpForm


class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = "registration/registration.html"
    success_url = reverse_lazy("login")


class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = "registration/edit_profile.html"
    success_url = reverse_lazy("home")

    def get_object(self):
        return self.request.user


class PasswordsChangeView(PasswordChangeView):
    # form_class = PasswordChangeForm
    form_class = PasswordChangingForm
    success_url = reverse_lazy("passwordSuccess")


def passwordSuccess(request):
    return render(request, "registration/password_success.html", {})
