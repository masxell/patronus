from django import template
from ..models import Reference

register = template.Library()

@register.inclusion_tag('reference/post/latest_post_reference.html')
def show_latest_references(count=5):
    latest_references = Reference.objects.order_by('-publish')[:count]
    
    return {
        'latest_references': latest_references,
    }