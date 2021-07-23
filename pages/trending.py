from django.views.generic import ListView
from django.db.models import Count
from .models import Post

class TrendingListView(ListView):
    model = Post
    template_name = 'trending/trending_list.html'

    def get_queryset(self):
        """return the highest vote count within the last 7 days"""
        from datetime import datetime, timedelta
        list_current = Post.objects.filter(date__gte=datetime.now()-timedelta(days=7)).annotate(like_count=Count('likes')).order_by('-like_count')
        return list_current