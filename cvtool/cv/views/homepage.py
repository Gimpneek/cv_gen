# pylint: disable=too-many-ancestors
""" Views for homepage """
from django.shortcuts import render


def index(request):
    """
    Show the homepage
    """
    return render(request, 'cv/base.html')
