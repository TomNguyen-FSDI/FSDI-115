
from .models import Community
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView, DetailView, FormView, ListView, UpdateView,DeleteView
    )

class CommunityListView(ListView):
    model = Community 
    template_name = 'community/community.html'


class CommunityDetailView(DetailView):
    model = Community
    template_name = 'community/community_detail.html'


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