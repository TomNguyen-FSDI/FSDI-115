from django.urls import path
from .community import (
    CommunityListView, 
    CommunityCreateView, 
    CommunityDetailView, 
    CommunityUpdateView, 
    CommunityDeleteView,
    follow_community
    )
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
    AddCommentView, 
    PostDeleteView, 
    LikeView
    )

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('search/', search_bar, name='search_bar'),
    path('account/login', login_page, name='login'),
    path('account/password_reset/', PasswordResetView.as_view(), name="password_reset"),
    path('account/password_change/', change_password, name="password_change"),
    path('community/list/', CommunityListView.as_view(), name='community_list'),
    path('community/create/', CommunityCreateView.as_view(), name='community_create'),
    path('community/follow/<int:pk>/<str:community_name>/', follow_community, name='follow_community'),
    path('community/<int:pk>/', CommunityDetailView.as_view(), name='community_detail'),
    path('community/update/<int:pk>/', CommunityUpdateView.as_view(), name= 'community_update'),
    path('community/<int:pk>/delete/', CommunityDeleteView.as_view(), name="community_delete"),
    path('community/<int:pk>/delete/', CommunityDeleteView.as_view(), name="community_delete"),
    path('post/list/', PostListView.as_view(), name='home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/create/', PostCreateView.as_view(), name= 'post_create'),
    path('post/update/<int:pk>/', PostUpdateView.as_view(), name= 'post_update'),
    path('post/<int:pk>/comment/', AddCommentView.as_view(), name="add_comment"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="post_delete"),
    path('like/<int:pk>/', LikeView, name='like_post'),
]