""" Test form for Skill """
from .common import SkillTestCase
from cv.forms.skill import SkillForm
from cv.models import Skill


class TestFormSkill(SkillTestCase):
    """
    Test the form for skills
    """

    @staticmethod
    def test_init():
        """
        Test creates the form successfully
        """
        SkillForm()

    def test_form_valid(self):
        """
        Test that the form checks the validation properly
        """
        form = SkillForm({
            'name': self.skill.name,
            'proficiency': self.skill.proficiency,
            'freshness': self.skill.freshness,
            'tags': [tag.pk for tag in self.skill.tags.all()]
        })
        self.assertTrue(form.is_valid())

    def test_valid_no_tags(self):
        """
        Test that the form says it's valid when no tags passed
        """
        form = SkillForm({
            'name': self.skill.name,
            'proficiency': self.skill.proficiency,
            'freshness': self.skill.freshness
        })
        self.assertTrue(form.is_valid())

    def test_invalid_name(self):
        """
        Test that the form says it's invalid when no name passed
        """
        form = SkillForm({
            'proficiency': self.skill.proficiency,
            'freshness': self.skill.freshness,
            'tags': [tag.pk for tag in self.skill.tags.all()]
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'name': ['This field is required.']
        })

    def test_invalid_prof(self):
        """
        Test that the form says it's invalid when no proficiency passed
        """
        form = SkillForm({
            'name': self.skill.name,
            'freshness': self.skill.freshness,
            'tags': [tag.pk for tag in self.skill.tags.all()]
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'proficiency': ['This field is required.']
        })

    def test_invalid_fresh(self):
        """
        Test that the form says it's invalid when no freshness passed
        """
        form = SkillForm({
            'proficiency': self.skill.proficiency,
            'name': self.skill.name,
            'tags': [tag.pk for tag in self.skill.tags.all()]
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'freshness': ['This field is required.']
        })

    def test_save(self):
        """
        Test that the form saves
        """
        form = SkillForm({
            'name': self.skill.name,
            'proficiency': self.skill.proficiency,
            'freshness': self.skill.freshness,
            'tags': [tag.pk for tag in self.skill.tags.all()]
        })
        self.assertEqual(len(Skill.objects.all()), 1)
        form.save()
        data = form.cleaned_data
        self.assertEqual(data.get('name'), self.skill.name)
        self.assertEqual(data.get('proficiency'), self.skill.proficiency)
        self.assertEqual(data.get('freshness'), self.skill.freshness)
        self.assertEqual(
            [tag.id for tag in data.get('tags')],
            [tag.id for tag in self.skill.tags.all()]
        )
        self.assertEqual(len(Skill.objects.all()), 2)
