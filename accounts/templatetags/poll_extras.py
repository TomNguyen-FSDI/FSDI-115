
from django import template
from pages.models import InboxMessage

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

@register.simple_tag
def set_unread_message(pk):
    item = InboxMessage.objects.get(pk=pk)
    item.unread = False
    item.save()
    return None


register.filter('value', html_value)
register.filter('placeholder', html_placeholder)
register.filter('style_width_100', style_width_100)
register.filter('hidden', style_hidden)

