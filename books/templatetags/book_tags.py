from django import template

register = template.Library()


@register.filter()
def to_lower(value1ddd):
    return value1ddd.lower()
