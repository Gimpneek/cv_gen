""" Tests for experience class """
from .common import ExperienceTestCase


class TestExperience(ExperienceTestCase):
    """
    Test Experience class
    """

    def test_company(self):
        """
        Test company is set on experience
        """
        self.assertEqual(self.experience.company, "Test Corp")

    def test_role(self):
        """
        Test role is set on experience
        """
        self.assertEqual(self.experience.role, "Senior Test Executor")

    def test_start_date(self):
        """
        Test start_date is set on experience
        """
        self.assertEqual(self.experience.start_date, "2016-04-02")

    def test_end_date(self):
        """
        Test end_date is set on experience
        """
        self.assertEqual(self.experience.end_date, None)

    def test_responsibilities(self):
        """
        Test responsibilities is set on experience
        """
        self.assertEqual(
            self.experience.responsibilities.get(pk=1).name,
            "Test Responsibility"
        )

    def test_projects(self):
        """
        Test projects is set on experience
        """
        self.assertEqual(
            self.experience.projects.get(pk=1).name,
            "Test Project"
        )

    def test_object_name(self):
        """
        Test __str__ for object
        """
        self.assertEqual(str(self.experience),
                         "Senior Test Executor - Test Corp")

    def test_absolute_url(self):
        """
        Test the absolute URL
        """
        self.assertIsNotNone(self.experience.get_absolute_url())
