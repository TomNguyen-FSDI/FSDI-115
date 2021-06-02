from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView
# from .forms import CustomUserCreationForm
from django.contrib.auth.forms import UserCreationForm


class SignUpView(CreateView):
    # form_class = CustomUserCreationForm
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

