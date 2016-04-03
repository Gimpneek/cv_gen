from django.shortcuts import render
from .models import *
from django.views.generic.edit import CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy


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


class SkillCreateView(CreateView):
    model = Skill
    fields = ['name', 'proficiency', 'freshness', 'tags']

    def get_context_data(self, **kwargs):
        context = super(SkillCreateView, self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.order_by('id')
        context['proficiency_choices'] = context['form'].fields['proficiency'].choices
        context['freshness_choices'] = context['form'].fields['freshness'].choices
        context['action'] = 'Add'
        return context


class SkillUpdateView(UpdateView):
    model = Skill
    fields = ['name', 'proficiency', 'freshness', 'tags']
    success_url = reverse_lazy('skills_list')

    def get_context_data(self, **kwargs):
        context = super(SkillUpdateView, self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.order_by('id')
        context['active_tags'] = context['form'].initial['tags']
        context['action'] = 'Edit'
        context['proficiency_choices'] = context['form'].fields[
            'proficiency'].choices
        context['freshness_choices'] = context['form'].fields[
            'freshness'].choices
        return context


class ExperienceCreateView(CreateView):
        model = Experience
        fields = ['company', 'role', 'start_date', 'end_date', 'projects',
                  'responsibilities']

        def get_context_data(self, **kwargs):
            context = super(ExperienceCreateView, self).get_context_data(**kwargs)
            context['projects'] = Project.objects.order_by('id')
            context['responsibilities'] = Responsibility.objects.order_by('id')
            context['action'] = 'Add'
            return context


class ExperienceUpdateView(UpdateView):
        model = Experience
        fields = ['company', 'role', 'start_date', 'end_date', 'projects',
                  'responsibilities']
        success_url = reverse_lazy('experience_list')

        def get_context_data(self, **kwargs):
            context = super(ExperienceUpdateView, self).get_context_data(**kwargs)
            context['projects'] = Project.objects.order_by('id')
            context['responsibilities'] = Responsibility.objects.order_by('id')
            context['action'] = 'Edit'
            context['active_projects'] = context['form'].initial['projects']
            context['active_responsibilities'] = context['form'].initial['responsibilities']
            return context


class EducationCreateView(CreateView):
    model = Education
    fields = ['institution', 'start_date', 'end_date', 'courses', 'projects']

    def get_context_data(self, **kwargs):
        context = super(EducationCreateView, self).get_context_data(**kwargs)
        context['projects'] = Project.objects.order_by('id')
        context['courses'] = Course.objects.order_by('id')
        context['action'] = 'Add'
        return context


class EducationUpdateView(UpdateView):
    model = Education
    fields = ['institution', 'start_date', 'end_date', 'courses', 'projects']
    success_url = reverse_lazy('education_list')

    def get_context_data(self, **kwargs):
        context = super(EducationUpdateView, self).get_context_data(**kwargs)
        context['projects'] = Project.objects.order_by('id')
        context['courses'] = Course.objects.order_by('id')
        context['action'] = 'Edit'
        context['active_projects'] = context['form'].initial['projects']
        context['active_courses'] = context['form'].initial[
            'courses']
        return context


class ProfileCreateView(CreateView):
    model = PersonalProfile
    fields = ['name', 'email', 'website', 'portfolio', 'personal_statement']

    def get_context_data(self, **kwargs):
        context = super(ProfileCreateView, self).get_context_data(**kwargs)
        context['action'] = 'Add'
        return context


class ProfileUpdateView(UpdateView):
    model = PersonalProfile
    fields = ['name', 'email', 'website', 'portfolio', 'personal_statement']
    success_url = reverse_lazy('profiles_list')

    def get_context_data(self, **kwargs):
        context = super(ProfileUpdateView, self).get_context_data(**kwargs)
        context['action'] = 'Edit'
        return context

