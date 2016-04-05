""" Tests for project class """
from django.test import TestCase
from cv.models import Project


class TestProject(TestCase):
    """
    Test Project class
    """

    def setUp(self):
        self.project = Project(name="Test Project")

    def test_name(self):
        """
        Test name is set on project
        """
        self.assertEqual(self.project.name, "Test Project")

    def test_object_name(self):
        """
        Test __str__ for object
        """
        self.assertEqual(str(self.project), "Test Project")
