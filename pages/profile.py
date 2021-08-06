from django.contrib.auth.models import User
from django.shortcuts import render, Http404
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    CreateView, DetailView, FormView, ListView, UpdateView,DeleteView
    )
from .models import Profile, Community

def profileDetailView(request, pk): # note that pk needs to be the same name as <int:pk>
    context = {}
    find_user = User.objects.get(pk=pk)
    try:
        profile = Profile.objects.get(user=find_user)
    except Profile.DoesNotExist:
        raise Http404("Profile does not exist")
    context['profile'] = profile
    context['communities'] = Community.objects.all()
    return render(request, 'profile/profile_detail.html', context)


class ProfileUpdateView(UpdateView):
    model = Profile
    template_name = 'profile/profile_update.html'
    fields = ['hodl', 'about', 'img']

    def get_success_url(self):
        pk = self.request.user.id
        return reverse("profile_detail", kwargs={"pk":pk})


