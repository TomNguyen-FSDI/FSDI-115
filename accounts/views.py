from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from pages.models import Profile


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


    def form_invalid(self, form):
        return redirect_invalid_logic(self.request, form)
    

    def form_valid(self, form): 
        email_in_db = User.objects.filter(email=form.data['email'])
        if len(email_in_db) > 0:
            return redirect_invalid_logic(self.request, form)
        return super().form_valid(form)


def redirect_invalid_logic(request, form):
    username_in_db = User.objects.filter(username=form.data['username'])
    email_in_db = User.objects.filter(email=form.data['email'])
    context = {}
    context['form'] = form
    if len(username_in_db) > 0:
        context['invalid_user'] = "username"            # used to show that invalid is user
        context['username'] = form.data['username']     # used for placeholder
    if len(email_in_db) > 0:
        context['invalid_email'] = "email"              #used to show that invalid is email
        context['email'] = form.data['email']           # used for placeholder
    return render(request, 'registration/signup.html', context)
    