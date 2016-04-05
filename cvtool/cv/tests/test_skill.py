""" Tests for Skill class """
from django.test import TestCase
from django.core.urlresolvers import reverse_lazy
from cv.models import Skill


class TestSkill(TestCase):
    """
    Test the skill class
    """

    def setUp(self):
        self.skill = Skill(
            name="Test Skill",
            proficiency=5,
            freshness=2
        )
        self.skill.save()
        self.skill.tags.create(name="Test Tag")
        self.view_resp = self.client.get(self.skill.get_absolute_url())

    def test_name(self):
        """
        Test name for skill
        """
        self.assertEqual(self.skill.name, "Test Skill")

    def test_proficiency(self):
        """
        Test proficiency for skill
        """
        self.assertEqual(self.skill.proficiency, 5)

    def test_freshness(self):
        """
        Test freshness for skill
        """
        self.assertEqual(self.skill.freshness, 2)

    def test_tag(self):
        """
        Test tag for skill
        """
        self.assertEqual(self.skill.tags.get(pk=1).name, "Test Tag")

    def test_object_name(self):
        """
        Test __str__ for object
        """
        self.assertEqual(str(self.skill), "Test Skill")

    def test_absolute_url(self):
        """
        Test the absolute URL
        """
        self.assertIsNotNone(self.skill.get_absolute_url())

    def test_view_contains_name(self):
        """
        Test the skill model view has name in it
        """
        self.assertContains(self.view_resp, self.skill.name)

    def test_view_contains_profiency(self):
        """
        Test the skill model view has proficiency in it
        """
        self.assertContains(self.view_resp, self.skill.proficiency)

    def test_view_contains_freshness(self):
        """
        Test the skill model view has freshness in it
        """
        self.assertContains(self.view_resp, self.skill.freshness)

    def test_view_contains_tag(self):
        """
        Test the skill model view
        """
        self.assertContains(self.view_resp, self.skill.tags.get(pk=1).name)

    def test_list_view(self):
        """
        Test skill in skills list view
        """
        list_resp = self.client.get(reverse_lazy('skills_list'))
        self.assertContains(list_resp, str(self.skill))

    def test_create_view(self):
        """
        Test create view
        """
        create_resp = self.client.get(reverse_lazy('skill-new'))
        self.assertEqual(create_resp.status_code, 200)
