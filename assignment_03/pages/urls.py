from django.urls import path
from .views import (
    HomePageView,
    PostListView,
    PostDetailView,
    search_bar
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('post/list/', PostListView.as_view(), name='home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('search', search_bar, name='search_bar')
]