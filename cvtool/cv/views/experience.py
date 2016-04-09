# pylint: disable=too-many-ancestors
""" Views experience class """
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy
from cv.models import Project, Responsibility, Experience
from cv.forms.experience import ExperienceForm


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


class ExperienceCreateView(CreateView):
    """
    Create view for experience
    """
    model = Experience
    form_class = ExperienceForm
    success_url = reverse_lazy('experience_list')

    def get_context_data(self, **kwargs):
        """
        Add the list of projects and responsibilities to the inputs and tell
        the template its an add action
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
    form_class = ExperienceForm
    success_url = reverse_lazy('experience_list')

    def get_context_data(self, **kwargs):
        """
        Add the list of projects and responsibilities to the context as well
        as calculate the ones the experience is linked to and also tell teh
        template its an edit action
        """
        context = super(ExperienceUpdateView, self).get_context_data(**kwargs)
        context['projects'] = Project.objects.order_by('id')
        context['responsibilities'] = Responsibility.objects.order_by('id')
        context['action'] = 'Edit'
        context['active_projects'] = context['form'].initial['projects']
        context['active_responsibilities'] = \
            context['form'].initial['responsibilities']
        return context
