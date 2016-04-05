""" Views for profile (personal profile) class """
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy
from cv.models import PersonalProfile


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
