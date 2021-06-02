from django.urls import path
from .views import (
    HomePageView,
    PostListView,
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('post/list/', PostListView.as_view(), name='home')
]