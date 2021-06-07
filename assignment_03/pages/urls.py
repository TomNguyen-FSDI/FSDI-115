from django.urls import path
from .views import (
    HomePageView,
    PostListView,
    search_bar
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('post/list/', PostListView.as_view(), name='home'),
    path('search', search_bar, name='search_bar')
]