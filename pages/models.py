from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

class Community(models.Model):
    name = models.CharField(max_length=200, unique=True)
    topic = models.CharField(max_length=600)
    description = models.TextField()
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        default=None
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('community_detail', args=[str(self.id)])


class Follow_community(models.Model):
    username = models.CharField(max_length=200, default=None)
    community_name = models.CharField(max_length=200,default=None)


class Post(models.Model):
    community = models.ForeignKey(
        Community, 
        on_delete=models.CASCADE, 
        related_name='posts', 
        null=True                 
        )
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(), 
        on_delete=models.CASCADE,
        default=None
    )
    date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    image = models.ImageField(upload_to='images/', default='.png', blank=True)
    likes = models.ManyToManyField(User, related_name='post_likes')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])


class Comment(models.Model):
    post = models.ForeignKey(
        Post, 
        on_delete=models.CASCADE,
        related_name='comments'                     # name the attribute for django tags
        )
    comment = models.CharField(max_length=540)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('post_list')


class InboxMessage(models.Model):
    receiver = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    sender = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    subject = models.CharField(max_length=255)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    unread = models.BooleanField(default=True)