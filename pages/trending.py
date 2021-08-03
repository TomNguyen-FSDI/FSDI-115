from django.views.generic import ListView
from django.db.models import Count
from .models import Post, Community

class TrendingListView(ListView):
    model = Post
    template_name = 'trending/trending_list.html'
    # paginate_by = 2

    def get_queryset(self):
        """return the highest vote count within the last 7 days"""
        from datetime import datetime, timedelta
        most_current_record = Post.objects.latest('date')
        print(most_current_record)
        list_current = Post.objects.filter(date__gte=most_current_record.date-timedelta(days=7)).annotate(like_count=Count('likes')).order_by('-like_count')
        # if len(list_current) < 7:
            # list_current = Post.objects.annotate(like_count=Count('likes')).order_by('-date','-like_count')
        return list_current

    def get_context_data(self, *args, **kwargs):
        context = super(TrendingListView, self).get_context_data(**kwargs)
        communities = Community.objects.all()
        context['communities'] = communities
        return context