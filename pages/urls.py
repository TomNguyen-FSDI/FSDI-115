from django.urls import path
from .views import (
    HomePageView,
    PostListView,
    PostDetailView,
    search_bar,
    PostCreateView,
    PostUpdateView,
    login_page
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('post/list/', PostListView.as_view(), name='home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/create/', PostCreateView.as_view(), name= 'post_create'),
    path('post/update/', PostUpdateView.as_view(), name= 'post_update'),
    path('search/', search_bar, name='search_bar'),
    path('account/login', login_page, name='login'),
]