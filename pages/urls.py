from django.urls import path
from .views import (
    HomePageView,
    PostListView,
    PostDetailView,
    search_bar,
    PostCreateView,
    PostUpdateView,
    login_page,
    PasswordResetView,
    change_password,
    AddCommentView
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('post/list/', PostListView.as_view(), name='home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/create/', PostCreateView.as_view(), name= 'post_create'),
    path('post/update/<int:pk>/', PostUpdateView.as_view(), name= 'post_update'),
    path('search/', search_bar, name='search_bar'),
    path('account/login', login_page, name='login'),
    path('account/password_reset/', PasswordResetView.as_view(), name="password_reset"),
    path('account/password_change/', change_password, name="password_change"),
    path('post/<int:pk>/comment/', AddCommentView.as_view(), name="add_comment")
]