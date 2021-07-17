from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from PIL import Image

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


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )
    img = models.ImageField(upload_to='images/profiles/', default='.png', blank=True, null=True)
    about = models.TextField(default=None, null=True)
    hodl = models.CharField(max_length=200, default=None, null=True)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super().save()
        image = Image.open(self.img.path)
        print('here')
        print(self.img.path)
        if image.height > 150 or image.width > 150:
            image.thumbnail((150, 150))
            image.save(self.img.path)


class Follow_community(models.Model):
    username = models.CharField(max_length=200, default=None)
    community_name = models.CharField(max_length=200,default=None)

    def __str__(self):
        return "user: {}, community name: {}".format(self.username, self.community_name)


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
    likes = models.ManyToManyField(User, blank=True,related_name='likes')
    dislikes = models.ManyToManyField(User, blank=True,related_name='dislikes')

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
    likes = models.ManyToManyField(User, blank=True,related_name='comment_likes')
    dislikes = models.ManyToManyField(User, blank=True,related_name='comment_dislikes')

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('post_list')

class InboxMessage(models.Model):
    receiver = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name = 'receiver'
        )
    sender = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name = 'sender'
        )

    subject = models.CharField(max_length=255)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    unread = models.BooleanField(default=True)

    def __str__(self):
        return "receiver:{}, sender:{}".format(self.receiver , self.sender)

    def get_absolute_url(self):
        return reverse('inbox_list')

