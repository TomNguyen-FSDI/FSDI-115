
from django import template

register = template.Library()


@register.filter(name="placeholder")
def html_placeholder(field, args=None):
    if args == None:
        return field
    field.field.widget.attrs.update({ "placeholder": args })
    return field


@register.filter(name="style_width_100")
def style_width_100(field):
    field.field.widget.attrs.update({"style":"width:100%;"})
    return field

register.filter('placeholder', html_placeholder)
register.filter('style_width_100', style_width_100)

