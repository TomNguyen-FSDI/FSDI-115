from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['comment']

    def form_valid(self, form): # can be used for LoginRequiredMixin
        form.instance.author = self.request.user
        return super().form_valid(form)