from django.urls import path
from .profile import (
    profileDetailView,
    ProfileUpdateView
)
from .trending import TrendingListView
from .inbox import (
    InboxCreateView,
    InboxListView,
    InboxSentView,
    InboxDetailView,
    InboxDeleteView,
)
from .community import (
    CommunityListView, 
    CommunityCreateView, 
    CommunityDetailView, 
    CommunityUpdateView, 
    CommunityDeleteView,
    follow_community,
    Followed_community 
    )
from .views import ( 
    PostListView,
    PostsByLikesView, 
    PostDetailView, 
    search_bar, 
    PostCreateView, 
    PostUpdateView, 
    login_page, 
    PasswordResetView, 
    change_password,
    AddCommentView, 
    PostDeleteView, 
    CommentUpdateView,
    CommentDeleteView,
    AddLike,
    AddDislike,
    AddCommentLike,
    AddCommentDislike,

    )

urlpatterns = [
    path('', PostListView.as_view(), name='home2'),
    path('search/', search_bar, name='search_bar'),
    path('account/login', login_page, name='login'),
    path('account/password_reset/', PasswordResetView.as_view(), name="password_reset"),
    path('account/password_change/', change_password, name="password_change"),
    path('community/list/', CommunityListView.as_view(), name='community_list'),
    path('community/create/', CommunityCreateView.as_view(), name='community_create'),
    path('community/follow/<int:pk>/<str:community_name>/', follow_community, name='follow_community'),
    path('community/follow/', Followed_community.as_view(), name='followed_community'),
    path('community/<int:pk>/', CommunityDetailView.as_view(), name='community_detail'),
    path('community/update/<int:pk>/', CommunityUpdateView.as_view(), name= 'community_update'),
    path('community/<int:pk>/delete/', CommunityDeleteView.as_view(), name="community_delete"),
    path('trending/list/', TrendingListView.as_view(), name='trending_list'),
    path('inbox/create/', InboxCreateView.as_view(), name='inbox_create'),
    path('inbox/list/', InboxListView.as_view(), name='inbox_list'),
    path('inbox/sent/', InboxSentView.as_view(), name='inbox_sent'),
    path('inbox/<int:pk>/', InboxDetailView.as_view(), name='inbox_detail'),
    path('inbox/<int:pk>/delete/', InboxDeleteView.as_view(), name='message_delete'),
    path('profile/<int:pk>/', profileDetailView, name='profile_detail'),
    path('profile/update/<int:pk>/', ProfileUpdateView.as_view(), name='profile_update'),
    path('post/list/', PostListView.as_view(), name='home'),
    path('post/list/likes/', PostsByLikesView.as_view(), name='post_likes'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/create/', PostCreateView.as_view(), name= 'post_create'),
    path('post/update/<int:pk>/', PostUpdateView.as_view(), name= 'post_update'),
    path('post/<int:pk>/comment/', AddCommentView.as_view(), name="add_comment"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="post_delete"),
    path('comment/update/<int:pk>/post/<int:id>/', CommentUpdateView.as_view(), name='comment_update'),
    path('comment/delete/<int:pk>/post/<int:id>/', CommentDeleteView.as_view(), name='comment_delete'),
    path('post/<int:pk>/like/', AddLike.as_view(), name='like'),
    path('post/<int:pk>/dislike/', AddDislike.as_view(), name='dislike'),
    path('comment/<int:pk>/like/', AddCommentLike.as_view(), name='comment_like'),
    path('comment/<int:pk>/dislike/', AddCommentDislike.as_view(), name='comment_dislike'),
]