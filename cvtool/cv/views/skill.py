# pylint: disable=too-many-ancestors
""" Views for Skill class
- List View
- CreateView
- UpdateDate
"""
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy
from cv.models import Tag, Skill
from cv.forms.skill import SkillForm


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


class SkillCreateView(CreateView):
    """
    Create View for skills
    """
    model = Skill
    form_class = SkillForm
    success_url = reverse_lazy('skills_list')

    def get_context_data(self, **kwargs):
        """
        Add the tags list, choices for freshness and proficiency to context
        so can show these tell the page that it will be an Add
        """
        context = super(SkillCreateView, self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.order_by('id')
        context['proficiency_choices'] = \
            context['form'].fields['proficiency'].choices
        context['freshness_choices'] = \
            context['form'].fields['freshness'].choices
        context['action'] = 'Add'
        return context


class SkillUpdateView(UpdateView):
    """
    Edit view for skills
    """
    model = Skill
    form_class = SkillForm
    success_url = reverse_lazy('skills_list')

    def get_context_data(self, **kwargs):
        """
        Add the tags list, choices for proficiency and freshness lists  as
        well as get the active tags (so no need to compute in template) and
        tell template its an add action
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
