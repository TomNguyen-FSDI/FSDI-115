
from .models import InboxMessage
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView, DetailView, FormView, ListView, UpdateView,DeleteView
    )
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import User
from django.shortcuts import render

class InboxListView(ListView):
    model = InboxMessage 
    template_name = 'inbox/inbox_list.html'

    def get_queryset(self):
        return super().get_queryset().filter(receiver=self.request.user).order_by("-timestamp")


class InboxSentView(ListView):
    model = InboxMessage
    template_name = 'inbox/inbox_sent.html'

    def get_queryset(self):
        return super().get_queryset().filter(sender=self.request.user).order_by("-timestamp")


class InboxDetailView(DetailView):
    model = InboxMessage
    template_name = 'inbox/inbox_detail.html'

    # def get_context_data(self, **kwargs):
    #     context = super(CommunityDetailView, self).get_context_data(**kwargs)
    #     # community = Community.objects.get(name=context['community'])
    #     # username = User.objects.get(username=self.request.user)
    #     follow = Follow_community.objects.filter(username=self.request.user).filter(community_name=context['community'])
    #     if len(follow) == 1:
    #         follow = "True"
    #     else:
    #         follow = "False"
    #     context['follow'] = follow
    #     return context


# def follow_community(request, pk, community_name):
#     # temp_community = Community.objects.get(pk=pk)
#     # temp_user = User.objects.get(username=request.user)     # get a 
#     am_i_in_the_community = Follow_community.objects.filter(username=request.user).filter(community_name=community_name)
#     if len(am_i_in_the_community) == 0 :
#         new_follow = Follow_community(community_name=community_name, username=request.user)
#         new_follow.save()
#     else:   # unfollow
#         found_id = Follow_community.objects.filter(username=request.user).filter(community_name=community_name).values('id')[0]['id']
#         no_follow = Follow_community.objects.get(pk=found_id)
#         print(no_follow)
#         no_follow.delete()

#     return HttpResponseRedirect(reverse('community_detail', args=[str(pk)]))



class InboxCreateView(CreateView):
    model = InboxMessage
    template_name = 'inbox/inbox_create.html'
    fields = ["receiver","subject", "message"]

    def form_valid(self, form): # can be used for LoginRequiredMixin
        form.instance.sender = self.request.user
        return super().form_valid(form)



# class CommunityUpdateView(UpdateView):
#     model = Community
#     template_name = 'community/community_update.html'
#     fields = ["name","topic", "description"]


# class CommunityDeleteView(DeleteView):
#     model = Community
#     template_name = "community/community_delete.html"
#     success_url = reverse_lazy("community_list")

#     def form_valid(self, form): # can be used for LoginRequiredMixin
#         form.instance.author = self.request.user
#         return super().form_valid(form)