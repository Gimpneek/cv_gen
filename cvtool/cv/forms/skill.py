""" Form for Skill entry """
from django import forms
from cv.models import Skill


class SkillForm(forms.ModelForm):
    """
    Form for Skill model
    """

    class Meta:
        """
        Meta data for form
        """
        model = Skill
        fields = ('name', 'proficiency', 'freshness', 'tags')
