from django import template
from django.utils.timesince import timesince

register = template.Library()

@register.filter
def time_since_pub(date):
    return timesince(date)