from django import template
from django.template.defaultfilters import stringfilter #check if we will get STR (else/error)

register = template.Library()

@register.filter(name='split')
@stringfilter
def split(value,key=' '):
    return value.split(key)


@register.filter(name='times')
def times(start):
    return range(start)


@register.filter(name='ranges')
def ranges(start,end):
    return range(start,end)