
from .models import Community, Follow_community
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView, DetailView, FormView, ListView, UpdateView,DeleteView
    )
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import User
from django.shortcuts import render

class CommunityListView(ListView):
    model = Community 
    template_name = 'community/community.html'


class CommunityDetailView(DetailView):
    model = Community
    template_name = 'community/community_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(CommunityDetailView, self).get_context_data(*args, **kwargs)
        # community = Community.objects.get(name=context['community'])
        # username = User.objects.get(username=self.request.user)
        follow = Follow_community.objects.filter(username=self.request.user).filter(community_name=context['community'])
        if len(follow) == 1:
            follow = "True"
        else:
            follow = "False"
        context['follow'] = follow
        return context


def follow_community(request, pk, community_name):
    # temp_community = Community.objects.get(pk=pk)
    # temp_user = User.objects.get(username=request.user)     # get a 
    am_i_in_the_community = Follow_community.objects.filter(username=request.user).filter(community_name=community_name)
    if len(am_i_in_the_community) == 0 :
        new_follow = Follow_community(community_name=community_name, username=request.user)
        new_follow.save()
    else:   # unfollow
        found_id = Follow_community.objects.filter(username=request.user).filter(community_name=community_name).values('id')[0]['id']
        no_follow = Follow_community.objects.get(pk=found_id)
        no_follow.delete()
    return HttpResponseRedirect(reverse('community_detail', args=[str(pk)]))


class Followed_community(ListView):
    model = Community 
    template_name = 'community/followed.html'

    def get_context_data(self, *args, **kwargs):
        context = super(Followed_community, self).get_context_data( *args, **kwargs)
        followed = Follow_community.objects.filter(username=self.request.user)      
        list_of_followed = []
        for item in followed:
            communities = Community.objects.filter(name=item.community_name)
            list_of_followed.append(communities)
        context['followed'] = list_of_followed
        communities = Community.objects.all()
        context['communities'] = communities
        return context
        


class CommunityCreateView(CreateView):
    model = Community
    template_name = 'community/community_create.html'
    fields = ["name","topic", "description"]

    def form_valid(self, form): # can be used for LoginRequiredMixin
        form.instance.author = self.request.user
        return super().form_valid(form)


class CommunityUpdateView(UpdateView):
    model = Community
    template_name = 'community/community_update.html'
    fields = ["name","topic", "description"]


class CommunityDeleteView(DeleteView):
    model = Community
    template_name = "community/community_delete.html"
    success_url = reverse_lazy("community_list")

    def form_valid(self, form): # can be used for LoginRequiredMixin
        form.instance.author = self.request.user
        return super().form_valid(form)