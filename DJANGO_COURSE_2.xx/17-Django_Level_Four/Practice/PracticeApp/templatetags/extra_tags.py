from django import template

register = template.Library()

@register.filter(name='change')
def first_extra(original, to_change):
    changed = original.replace('_',' ')
    changed = changed.replace('inserted', to_change)
    return changed.title()+'!!!'