
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


class InboxCreateView(CreateView):
    model = InboxMessage
    template_name = 'inbox/inbox_create.html'
    fields = ["receiver","subject", "message"]

    def form_valid(self, form): # can be used for LoginRequiredMixin
        form.instance.sender = self.request.user
        return super().form_valid(form)

class InboxDeleteView(DeleteView):
    model = InboxMessage
    template_name = "inbox/message_delete.html"
    success_url = reverse_lazy("inbox_list")

