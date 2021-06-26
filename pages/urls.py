from django.urls import path
from .views import (
    HomePageView,
    PostListView,
    PostDetailView,
    search_bar,
    PostCreateView,
    PostUpdateView
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('post/list/', PostListView.as_view(), name='home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/create/', PostCreateView.as_view(), name= 'post_create'),
<<<<<<< HEAD:assignment_03/pages/urls.py
    path('post/update/', PostUpdateView.as_view(), name= 'post_update'),
    path('search/', search_bar, name='search_bar')
=======
    path('search', search_bar, name='search_bar')
>>>>>>> 0d1a359137b3431b40e3bf8b160d20b73f9ae864:pages/urls.py
]