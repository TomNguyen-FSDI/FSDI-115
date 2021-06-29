from django import forms
from django.contrib import messages
from django.contrib.auth import (
    authenticate, login, update_session_auth_hash
    )
from django.contrib.auth.forms import (
    AuthenticationForm, UserCreationForm, PasswordChangeForm
    )
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.db.models import Q
from django.shortcuts import redirect, render
from django.template import loader
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.views.generic import (
    CreateView, DetailView, FormView, ListView, UpdateView,DeleteView
    )
from .models import Post, Comment, Community
from .forms import CommentForm


class HomePageView(ListView):
    model = Post
    template_name = 'home.html'

class PostListView(ListView):
    model = Post 
    template_name = 'home.html'


class CommunityListView(ListView):
    model = Community 
    template_name = 'community/community.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostCreateView(CreateView):
    model = Post
    template_name = 'post_create.html'
    fields = ["community","title", "body", "image"]

    def form_valid(self, form): # can be used for LoginRequiredMixin
        form.instance.author = self.request.user
        return super().form_valid(form)

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'

    def get_success_url(self):
          # capture that 'pk' as postid and pass it to 'reverse_lazy()' function
          postid=self.kwargs['pk']
          return reverse_lazy('post_detail', args=str(postid))

    def form_valid(self, form):
        form.instance.post = Post.objects.get(pk=self.kwargs.get("pk"))
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'post_update.html'
    fields = ["title", "body", "image"]


class PostDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form): # can be used for LoginRequiredMixin
        form.instance.author = self.request.user
        return super().form_valid(form)


def login_page(request):
    form = AuthenticationForm()
    context = {}
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            user_account_name = User.objects.filter(username=username)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                if len(user_account_name) == 0:         # user doesn't exist
                    context['username'] = "Username"    # set placehold to Username
                    context['invalid'] = "username"
                    messages.info(request, 'Username is invalid')
                else:                                   # user is right but password is wrong
                    messages.info(request, 'Password is invalid')
                    context['invalid'] = "password"
                    context['username'] = user_account_name.get()
        context['form'] = form
        return render(request, 'registration/login.html', context)


class PasswordResetForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["email"]


class PasswordResetView(FormView):
    form_class = PasswordResetForm
    success_url = reverse_lazy('password_reset_done')
    template_name = 'registration/password_reset_form.html'
    
    def form_valid(self, form): 
        email_in_db = User.objects.filter(email=form.data['email'])

        if len(email_in_db) == 0:
            return self.redirect_invalid_password_change(form)
        
        user= User.objects.filter(Q(email=form.data['email'])).first()
        c = {
            'email': form.data['email'],
            'domain': self.request.META['HTTP_HOST'],
            'site_name': self.request.META['HTTP_HOST'],
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'user': user,
            'token': default_token_generator.make_token(user),
            'protocol': self.request.scheme,
        }
        email_template_name='registration/password_reset_email.html'
        subject = "Reset Your Password"
        email = loader.render_to_string(email_template_name, c)
        send_mail(subject, email, 'webmaster@localhost' , [form.data['email']], fail_silently=False)
        return super().form_valid(form)

    def redirect_invalid_password_change(self, form):
        context = {}
        context['form'] = form
        context['invalid'] = "email"
        context['email'] = form.data['email']
        return render(self.request, 'registration/password_reset_form.html', context)


def change_password(request):
    context = {}
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            return redirect('password_change_done')
        else:
            context['invalid'] = "password"         # marks in the template that there was a problem
    else:
        form = PasswordChangeForm(request.user)
    context['form'] = form
    return render(request, 'registration/password_change_form.html', context)


def search_bar(request):
    if request.method == "POST":
        if 'searched_data' in request.POST: # same as : # searched = request.POST.get('searched_data', False)
            searched = request.POST['searched_data']
            searched_results = Post.objects.filter(Q(body__contains=searched)|Q(title__contains=searched)).order_by('-id')[:7]
            context = {}
            context['searched'] = searched
            context['searched_results'] = searched_results
            return render(request, 'search_bar.html', context)
    return render(request, 'search_bar.html', {})