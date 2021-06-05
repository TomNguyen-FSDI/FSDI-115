from django.urls import path
from . import views
from .views import (
    HomePageView,
    PostListView,
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('post/list/', PostListView.as_view(), name='home'),
    path('search', views.search_bar, name='search_bar')
]