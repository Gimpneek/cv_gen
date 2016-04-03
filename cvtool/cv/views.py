from django.shortcuts import render
from .models import *


def index(request):
    """
    Show the homepage
    """
    return render(request, 'cv/base.html')


def skills_list(request):
    """
    Show skills added to the system
    """
    skills = Skill.objects.order_by('id')
    return render(
        request,
        'cv/listing.html',
        {
            'title': 'Skills',
            'type': 'skill',
            'items': skills
        }
    )


def experience_list(request):
    """
    Show experience added to the system
    """
    experiences = Experience.objects.order_by('id')
    return render(
        request,
        'cv/listing.html',
        {
            'title': 'Experience',
            'type': 'experience',
            'items': experiences
        }
    )


def education_list(request):
    """
    Show education added to the system
    """
    education = Education.objects.order_by('id')
    return render(
        request,
        'cv/listing.html',
        {
            'title': 'Education',
            'type': 'education',
            'items': education
        }
    )