"""
Simple tags to help render page:
- reverse_url nav active: https://www.turnkeylinux.org/blog/django-navbar
"""
from django import template
from django.core.urlresolvers import resolve, Resolver404

register = template.Library()


@register.simple_tag
def navactive(request, views):
    """
    Template tag to check to see if the page the user is currently on is in
    an array of reverse url look ups
    Args:
        request: Request object sent while rendering page
        views: space separated string of url names (ie: 'skill-edit skill-new')

    Returns: string to be used in class attribute
    """
    try:
        view = resolve(request.path).url_name
        if view in views:
            return "is-active"
        else:
            return ""
    except Resolver404:
        return ""


@register.filter('fieldtype')
def field_type(field):
    """
    Access the widget in form field and return the name of the class for
    conditional rendering
    Args:
        field: form field
    Returns: string of form field type
    """
    return field.field.widget.__class__.__name__
