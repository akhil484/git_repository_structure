from django import template
from django.utils.safestring import mark_safe
from base.utils import folder_structure_html
register = template.Library()

@register.filter
def get_complete_struct(key, value):
    return mark_safe(folder_structure_html(key, value))
