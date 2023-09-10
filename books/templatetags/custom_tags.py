from django import template

register = template.Library()


@register.filter
def custom_action_button(obj):
    return '<a href="#">Custom Action</a>'
