
from django import template
from pages.models import (
    InboxMessage, Post, Comment, Profile
    )
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User


register = template.Library()


@register.filter(name="placeholder")
def html_placeholder(field, args=None):
    if args == None:
        return field
    field.field.widget.attrs.update({ "placeholder": args })
    return field

@register.filter(name="value")
def html_value(field, args=None):
    if args == None:
        return field
    field.field.widget.attrs.update( { "value": args })
    return field


@register.filter(name="hidden")
def style_hidden(field):
    field.field.widget.attrs.update( { "style": "display:none;" })
    return field


@register.simple_tag
def unread_message(request):
    unread = InboxMessage.objects.filter(receiver=request.user, unread=True).count()
    return unread

@register.filter(name="style_width_100")
def style_width_100(field):
    field.field.widget.attrs.update({"style":"width:100%;"})
    return field

@register.filter(name="red_border")
def red_border(field):
    field.field.widget.attrs.update({"style":"border:1px solid red;"})
    return field

@register.simple_tag
def set_unread_message(pk):
    item = InboxMessage.objects.get(pk=pk)
    item.unread = False
    item.save()
    return None

@register.simple_tag
def get_dislikes(pk, request):
    post_info = get_object_or_404(Post, id=pk)
    results = r'<i class="fas fa-arrow-down not-clicked"></i>'
    if post_info.dislikes.filter(id=request.user.id).exists():
        results = r'<i class="fas fa-arrow-down disliked"></i>'
    return mark_safe(results)

@register.simple_tag
def get_likes(pk, request):
    post_info = get_object_or_404(Post, id=pk)
    results = r'<i class="fas fa-arrow-up not-clicked"></i>'
    if post_info.likes.filter(id=request.user.id).exists():
        results = r'<i class="fas fa-arrow-up liked"></i>'
    return mark_safe(results)

@register.simple_tag
def get_comment_likes(pk, request):
    comment_info = get_object_or_404(Comment, id=pk)
    results = r'<i class="fas fa-arrow-up not-clicked"></i><span class="count">'
    if comment_info.likes.filter(id=request.user.id).exists():
        results = r'<i class="fas fa-arrow-up liked"></i><span class="count">'
    return mark_safe(results)

@register.simple_tag
def get_comment_dislikes(pk, request):
    comment_info = get_object_or_404(Comment, id=pk)
    results = r'<i class="fas fa-arrow-down not-clicked"></i><span class="count">'
    if comment_info.dislikes.filter(id=request.user.id).exists():
        results = r'<i class="fas fa-arrow-down disliked"></i><span class="count">'
    return mark_safe(results)


@register.simple_tag
def check_profile(request):
    pk = request.user.pk
    find_user = User.objects.get(pk=pk)
    find_profile = Profile.objects.filter(user=find_user)    
    if len(find_profile) > 0: # if this is not empty
        return None
    else:
        create_profile =  Profile(user=find_user)
        create_profile.save()
    return None


register.filter('value', html_value)
register.filter('placeholder', html_placeholder)
register.filter('style_width_100', style_width_100)
register.filter('red_border', red_border)
register.filter('hidden', style_hidden)

