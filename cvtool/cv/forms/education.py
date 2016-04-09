""" Form for Education entry """
from django import forms
from cv.models import Education


class EducationForm(forms.ModelForm):
    """
    Form for Education model
    """

    class Meta:
        """
        Meta data for form
        """
        model = Education
        fields = ('institution', 'start_date', 'end_date', 'courses',
                  'projects')
