from django.views.generic import ListView
from django.db.models import Count
from .models import Post, Community

class TrendingListView(ListView):
    model = Post
    template_name = 'trending/trending_list.html'

    def get_queryset(self):
        """return the highest vote count within the last 7 days"""
        from datetime import datetime, timedelta
        list_current = Post.objects.filter(date__gte=datetime.now()-timedelta(days=7)).annotate(like_count=Count('likes')).order_by('-like_count')
        if len(list_current) < 7:
            list_current = Post.objects.order_by('-date').annotate(like_count=Count('likes')).order_by('-like_count')
        return list_current
  
    def get_context_data(self, *args, **kwargs):
        context = super(TrendingListView, self).get_context_data(**kwargs)
        communities = Community.objects.all()
        context['communities'] = communities
        return context