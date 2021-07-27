from django import forms
from django.contrib import messages
from django.contrib.auth import (
    authenticate, 
    login, 
    update_session_auth_hash
    )
from django.contrib.auth.forms import (
    AuthenticationForm, 
    UserCreationForm, 
    PasswordChangeForm
    )
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.db.models import Q, Count
from django.shortcuts import redirect, render, get_object_or_404, get_list_or_404
from django.template import loader
from django.urls import reverse_lazy, reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.views.generic import (
    CreateView, 
    DetailView, 
    FormView, 
    ListView, 
    UpdateView,
    DeleteView,
    View
    )
from .models import Post, Comment, Community, InboxMessage, Profile
from .forms import CommentForm
from django.http import HttpResponseRedirect

class AddLike(View):
    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)

        disliked = False

        for dislike in post.dislikes.all():
            if dislike == request.user:
                disliked = True
                break

        if disliked:
            post.dislikes.remove(request.user)

        liked = False

        for like in post.likes.all():
            if like == request.user:
                liked = True
                break

        if not liked:
            post.likes.add(request.user)

        if liked:
            post.likes.remove(request.user)

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)


class AddDislike(View):
    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)

        liked = False

        for like in post.likes.all():
            if like == request.user:
                liked = True
                break

        if liked:
            post.likes.remove(request.user)

        disliked = False

        for dislike in post.dislikes.all():
            if dislike == request.user:
                disliked = True
                break

        if not disliked:
            post.dislikes.add(request.user)

        if disliked:
            post.dislikes.remove(request.user)

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)

class AddCommentLike(View):
    def post(self, request, pk, *args, **kwargs):
        comment = Comment.objects.get(pk=pk)

        disliked = False

        for dislike in comment.dislikes.all():
            if dislike == request.user:
                disliked = True
                break

        if disliked:
            comment.dislikes.remove(request.user)

        liked = False

        for like in comment.likes.all():
            if like == request.user:
                liked = True
                break

        if not liked:
            comment.likes.add(request.user)

        if liked:
            comment.likes.remove(request.user)

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)

class AddCommentDislike(View):
    def post(self, request, pk, *args, **kwargs):
        comment = Comment.objects.get(pk=pk)

        liked = False

        for like in comment.likes.all():
            if like == request.user:
                liked = True
                break

        if liked:
            comment.likes.remove(request.user)

        disliked = False

        for dislike in comment.dislikes.all():
            if dislike == request.user:
                disliked = True
                break

        if not disliked:
            comment.dislikes.add(request.user)

        if disliked:
            comment.dislikes.remove(request.user)

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)

class PostsByLikesView(ListView):
    model = Post
    template_name = 'post_likes.html'


    def get_context_data(self, **kwargs):
        context = super(PostsByLikesView, self).get_context_data(**kwargs)
        post = Post
        liked_order = post.objects.annotate(like_count=Count('likes')).order_by('-like_count')
        communities = Community.objects.all()
        if self.request.user.pk is None:
            pass
        else:
            find_user = User.objects.get(pk=self.request.user.pk)
            find_profile = Profile.objects.filter(user=find_user)    
            if len(find_profile) == 0:
                create_profile =  Profile(user=find_user)
                create_profile.save()
                create_profile.refresh_from_db()
            find_profile = Profile.objects.get(user=User.objects.get(pk=self.request.user.id))
            context['profile_id'] = find_profile.id
            
        context["liked_order"] = liked_order
        context['communities'] = communities
        return context


class PostListView(ListView):
    model = Post
    template_name = 'home.html'
    paginate_by = 2

    def get_context_data(self, *args, **kwargs):
        context = super(PostListView, self).get_context_data(*args, **kwargs)
        if self.request.user.pk is None:
            pass
        else:
            find_user = User.objects.get(pk=self.request.user.pk)
            find_profile = Profile.objects.filter(user=find_user)    
            if len(find_profile) == 0:
                create_profile =  Profile(user=find_user)
                create_profile.save()
                create_profile.refresh_from_db()
            find_profile = Profile.objects.get(user=User.objects.get(pk=self.request.user.id))
            context['profile_id'] = find_profile.id
        context['communities'] = Post.community_all.all()
        return context


class HomeListView(PostListView):
    template_name = 'landing_page.html'


class CommunityListView(ListView):
    model = Community 
    template_name = 'community/community.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super(PostDetailView, self).get_context_data(*args, **kwargs)
        # gets comment model and create a list by likes starting with highest number
        comments = Comment
        liked_order = comments.objects.annotate(like_count=Count('likes')).order_by('-like_count')
        # Tracks if post is liked or disliked by user
        post_info = get_object_or_404(Post, id=self.kwargs['pk'])

        liked = False
        if post_info.likes.filter(id=self.request.user.id).exists():
            liked = True

        disliked = False
        if post_info.dislikes.filter(id=self.request.user.id).exists():
            disliked = True
        context['communities'] = Post.community_all.all()
        context["liked_order"] = liked_order
        context["liked"] = liked
        context["disliked"] = disliked
        return context

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
    fields = ["community","title", "body", "image"]


class CommentUpdateView(UpdateView):
    model = Comment
    template_name = 'comment_update.html'
    fields = ["comment"]

    def get_success_url(self):
        # capture that 'pk' as postid and pass it to 'reverse_lazy()' function
        postid=self.kwargs['id']
        return reverse_lazy('post_detail', args=str(postid))

class CommentDeleteView(DeleteView):
    model = Comment
    template_name = "comment_delete.html"
    
    def get_success_url(self):
        # capture that 'pk' as postid and pass it to 'reverse_lazy()' function
        postid=self.kwargs['id']
        return reverse_lazy('post_detail', args=str(postid))

    def form_valid(self, form): # can be used for LoginRequiredMixin
        form.instance.author = self.request.user
        return super().form_valid(form)


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
            search_result_for_community = Community.objects.filter(Q(name__contains=searched)|Q(topic__contains=searched)|Q(description__contains=searched)).order_by('id')[:5]
            search_result_for_post = Post.objects.filter(Q(body__contains=searched)|Q(title__contains=searched)).order_by('-id')[:5]
            context = {}
            context['searched'] = searched
            context['searched_results_post'] = search_result_for_post
            context['searched_results_community'] = search_result_for_community
            return render(request, 'search_bar.html', context)
    return render(request, 'search_bar.html', {})