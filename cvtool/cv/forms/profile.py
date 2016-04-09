""" Form for Profile entry """
from django import forms
from cv.models import PersonalProfile


class ProfileForm(forms.ModelForm):
    """
    Form for Profile model
    """

    class Meta:
        """
        Meta data for form
        """
        model = PersonalProfile
        fields = ('name', 'email', 'website', 'portfolio',
                  'personal_statement')
