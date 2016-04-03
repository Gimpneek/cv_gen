# pylint: disable=too-many-ancestors
""" Views for CV App """
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy
from .models import Tag, Skill, Project, Responsibility, Experience
from .models import Course, Education, PersonalProfile


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
    """
    Create View for skills
    """
    model = Skill
    fields = ['name', 'proficiency', 'freshness', 'tags']

    def get_context_data(self, **kwargs):
        """
        Add the tags list, choices for freshness and proficiency to context so can show these
        Tell the page that it will be an Add
        """
        context = super(SkillCreateView, self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.order_by('id')
        context['proficiency_choices'] = context['form'].fields['proficiency'].choices
        context['freshness_choices'] = context['form'].fields['freshness'].choices
        context['action'] = 'Add'
        return context


class SkillUpdateView(UpdateView):
    """
    Edit view for skills
    """
    model = Skill
    fields = ['name', 'proficiency', 'freshness', 'tags']
    success_url = reverse_lazy('skills_list')

    def get_context_data(self, **kwargs):
        """
        Add the tags list, choices for proficiency and freshness lists  as well as get the active
        tags (so no need to compute in template) and tell template its an add action
        """
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
    """
    Create view for experience
    """
    model = Experience
    fields = ['company', 'role', 'start_date', 'end_date', 'projects',
              'responsibilities']

    def get_context_data(self, **kwargs):
        """
        Add the list of projects and responsibilities to the inputs and tell the template its an
        add action
        """
        context = super(ExperienceCreateView, self).get_context_data(**kwargs)
        context['projects'] = Project.objects.order_by('id')
        context['responsibilities'] = Responsibility.objects.order_by('id')
        context['action'] = 'Add'
        return context


class ExperienceUpdateView(UpdateView):
    """
    Edit view for experience
    """
    model = Experience
    fields = ['company', 'role', 'start_date', 'end_date', 'projects',
              'responsibilities']
    success_url = reverse_lazy('experience_list')

    def get_context_data(self, **kwargs):
        """
        Add the list of projects and responsibilities to the context as well as calculate the
        ones the experience is linked to and also tell teh template its an edit action
        """
        context = super(ExperienceUpdateView, self).get_context_data(**kwargs)
        context['projects'] = Project.objects.order_by('id')
        context['responsibilities'] = Responsibility.objects.order_by('id')
        context['action'] = 'Edit'
        context['active_projects'] = context['form'].initial['projects']
        context['active_responsibilities'] = context['form'].initial['responsibilities']
        return context


class EducationCreateView(CreateView):
    """
    Create view for the education
    """
    model = Education
    fields = ['institution', 'start_date', 'end_date', 'courses', 'projects']

    def get_context_data(self, **kwargs):
        """
        Add the list of projects and courses to teh context and tell the template its an add action
        """
        context = super(EducationCreateView, self).get_context_data(**kwargs)
        context['projects'] = Project.objects.order_by('id')
        context['courses'] = Course.objects.order_by('id')
        context['action'] = 'Add'
        return context


class EducationUpdateView(UpdateView):
    """
    Edit view for the education
    """
    model = Education
    fields = ['institution', 'start_date', 'end_date', 'courses', 'projects']
    success_url = reverse_lazy('education_list')

    def get_context_data(self, **kwargs):
        """
        Add the list of projects and courses to the context, tell the template its an edit action
        and get the active projects and courses so dont have to calculate this in template
        """
        context = super(EducationUpdateView, self).get_context_data(**kwargs)
        context['projects'] = Project.objects.order_by('id')
        context['courses'] = Course.objects.order_by('id')
        context['action'] = 'Edit'
        context['active_projects'] = context['form'].initial['projects']
        context['active_courses'] = context['form'].initial[
            'courses']
        return context


class ProfileCreateView(CreateView):
    """
    Create view for profile
    """
    model = PersonalProfile
    fields = ['name', 'email', 'website', 'portfolio', 'personal_statement']

    def get_context_data(self, **kwargs):
        """
        Tell template its an add action
        """
        context = super(ProfileCreateView, self).get_context_data(**kwargs)
        context['action'] = 'Add'
        return context


class ProfileUpdateView(UpdateView):
    """
    Edit view for profile
    """
    model = PersonalProfile
    fields = ['name', 'email', 'website', 'portfolio', 'personal_statement']
    success_url = reverse_lazy('profiles_list')

    def get_context_data(self, **kwargs):
        """
        Tell template its an edit action
        """
        context = super(ProfileUpdateView, self).get_context_data(**kwargs)
        context['action'] = 'Edit'
        return context

