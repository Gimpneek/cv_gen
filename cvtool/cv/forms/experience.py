""" Form for Experience entry """
from django import forms
from cv.models import Experience


class ExperienceForm(forms.ModelForm):
    """
    Form for Experience model
    """

    class Meta:
        """
        Meta data for form
        """
        model = Experience
        fields = ('company', 'role', 'start_date', 'end_date', 'projects',
                  'responsibilities')
