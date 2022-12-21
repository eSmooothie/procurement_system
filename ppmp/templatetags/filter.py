from django import template
from django.utils.safestring import mark_safe
import re

register = template.Library()

@register.filter
def highlight(text, search):

    if search:
        rx_pattern = "\S*({})\S*".format(search)
        match_words = re.findall(rx_pattern, text, flags=re.IGNORECASE)

        for i in match_words:
            highlighted = re.sub(i, '<span style="background-color: yellow;">{}</span>'.format(i), text, flags=re.IGNORECASE)
            text = highlighted

    return mark_safe(text)