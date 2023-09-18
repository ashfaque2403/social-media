from django.urls import path
from .views import PostListView,PostDetailView,PostEditView,PostDeleteView,CommentDeleteView,ProfileView,ProfileEditView,AddFollower,RemoveFollower,AddLikes,AddDislike,UserSearch,ListFollowers,PostNotification,FollowNotification

urlpatterns = [
    path('',PostListView.as_view(),name='post-list'),
    path('post/<int:pk>',PostDetailView.as_view(),name='post-detail'),
    path('post/edit/<int:pk>',PostEditView.as_view(),name='post-edit'),
    path('post/delete/<int:pk>',PostDeleteView.as_view(),name='post-delete'),
    path('post/<int:post_pk>/comment/delete/<int:pk>/',CommentDeleteView.as_view(),name='comment-delete'),
    path('post/<int:pk>/like',AddLikes.as_view(),name='likes'),
    path('post/<int:pk>/dislike',AddDislike.as_view(),name='dislike'),
    path('profile/<int:pk>',ProfileView.as_view(),name='profile'),
    path('profile/<int:pk>/followers/',ListFollowers.as_view(),name='list-followers'),
    path('profile/edit/<int:pk>',ProfileEditView.as_view(),name='profile-edit'),
    path('profile/<int:pk>/followers/add',AddFollower.as_view(),name='add-followers'),
    path('profile/<int:pk>/followers/remove',RemoveFollower.as_view(),name='remove-followers'),
    path('search/',UserSearch.as_view(),name='profile-search'),
    path('notification/<int:notification_pk>/post/<int:post_pk>',PostNotification.as_view(),name='post-notification'),
    path('notification/<int:notification_pk>/profile/<int:profile_pk>',FollowNotification.as_view(),name='follow-notification'),


]
