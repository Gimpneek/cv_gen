# pylint: disable=too-many-ancestors
""" Views for education class """
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy
from cv.models import Project
from cv.models import Course, Education
from cv.forms.education import EducationForm


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


class EducationCreateView(CreateView):
    """
    Create view for the education
    """
    model = Education
    form_class = EducationForm
    success_url = reverse_lazy('education_list')

    def get_context_data(self, **kwargs):
        """
        Add the list of projects and courses to teh context and tell the
        template its an add action
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
    form_class = EducationForm
    success_url = reverse_lazy('education_list')

    def get_context_data(self, **kwargs):
        """
        Add the list of projects and courses to the context, tell the template
        its an edit action and get the active projects and courses so dont
        have to calculate this in template
        """
        context = super(EducationUpdateView, self).get_context_data(**kwargs)
        context['projects'] = Project.objects.order_by('id')
        context['courses'] = Course.objects.order_by('id')
        context['action'] = 'Edit'
        context['active_projects'] = context['form'].initial['projects']
        context['active_courses'] = context['form'].initial[
            'courses']
        return context
