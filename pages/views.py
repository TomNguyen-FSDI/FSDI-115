from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class HomePageView(ListView):
    model = Post
    template_name = 'home.html'

class PostListView(ListView):
    model = Post 
    template_name = 'home.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostCreateView(CreateView):
    model = Post
    template_name = 'post_create.html'
    fields = ["title", "body", "image"]

    def form_valid(self, form): # can be used for LoginRequiredMixin
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'post_update.html'
    fields = ["title", "body", "image"]


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
                if len(user_account_name) == 0:
                    context['invalid'] = "username"
                    messages.info(request, 'Username is invalid')
                else:
                    messages.info(request, 'Password is invalid')
                    context['invalid'] = "password"
        context['form'] = form
        return render(request, 'registration/login.html', context)


def search_bar(request):
    if request.method == "POST":
        if 'searched_data' in request.POST: # same as : # searched = request.POST.get('searched_data', False)
            searched = request.POST['searched_data']
            searched_results = Post.objects.filter(Q(body__contains=searched)|Q(title__contains=searched)).order_by('-id')[:7]
            return render(request, 'search_bar.html', {'searched': searched, 'searched_results': searched_results})
    return render(request, 'search_bar.html', {})