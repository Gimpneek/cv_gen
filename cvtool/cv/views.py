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


def profiles_list(request):
    """
    Show profiles added to the system
    """
    profiles = PersonalProfile.objects.order_by('id')
    return render(
        request,
        'cv/listing.html',
        {
            'title': 'Profiles',
            'type': 'profile',
            'items': profiles
        }
    )


def skills_form(request, skill_id):
    """
    Show form to edit or add skills
    """
    skill = Skill.objects.get(pk=skill_id)
    skill_tags = Skill.objects.filter(pk=skill_id).values_list('tags', flat=True)
    tags = Tag.objects.order_by('id')
    return render(
        request,
        'cv/skills_form.html',
        {
            'action': 'Edit',
            'skill': skill,
            'tags': tags,
            'active_tags': skill_tags
        }
    )
