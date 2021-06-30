
from .models import Community
from django.views.generic import (
    CreateView, DetailView, FormView, ListView, UpdateView,DeleteView
    )

class CommunityListView(ListView):
    model = Community 
    template_name = 'community/community.html'