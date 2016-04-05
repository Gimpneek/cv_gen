"""
Simple tags to help render page:
- reverse_url nav active: https://www.turnkeylinux.org/blog/django-navbar
"""
from django import template
from django.core.urlresolvers import resolve, Resolver404

register = template.Library()


@register.simple_tag
def navactive(request, views):
    # if request.path in (reverse_lazy(url) for url in urls.split()):
    #     return "active"
    # return ""
    try:
        view = resolve(request.path).url_name
        if view in views:
            return "is-active"
        else:
            return ""
    except Resolver404:
        return ""
