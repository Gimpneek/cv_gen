""" Tests for Skill class """
from .common import SkillTestCase


class TestSkill(SkillTestCase):
    """
    Test the skill class
    """

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
