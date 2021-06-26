<<<<<<< HEAD:assignment_03/pages/views.py
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post
from django.db.models import Q

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

class PostUpdateView(UpdateView):
    model = Post
    template_name = 'post_update.html'
    fields = ["title", "body", "image"]

def search_bar(request):
    if request.method == "POST":
        if 'searched_data' in request.POST: # same as : # searched = request.POST.get('searched_data', False)
            searched = request.POST['searched_data']
            searched_results = Post.objects.filter(Q(body__contains=searched)|Q(title__contains=searched)).order_by('-id')[:7]
            return render(request, 'search_bar.html', {'searched': searched, 'searched_results': searched_results})
=======
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from django.db.models import Q

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

def search_bar(request):
    if request.method == "POST":
        if 'searched_data' in request.POST: # same as : # searched = request.POST.get('searched_data', False)
            searched = request.POST['searched_data']
            searched_results = Post.objects.filter(Q(body__contains=searched)|Q(title__contains=searched)).order_by('-id')[:7]
            return render(request, 'search_bar.html', {'searched': searched, 'searched_results': searched_results})
>>>>>>> 0d1a359137b3431b40e3bf8b160d20b73f9ae864:pages/views.py
    return render(request, 'search_bar.html', {})