""" Tests for Tag Class """
from django.test import TestCase
from cv.models import Tag


class TestTag(TestCase):
    """
    Test the tag class
    """

    def setUp(self):
        self.tag = Tag(name="Test Name")

    def test_name(self):
        """
        Test name for tag
        """
        self.assertEqual(self.tag.name, "Test Name")

    def test_object_name(self):
        """
        Test __str__ for object
        """
        self.assertEqual(str(self.tag), "Test Name")
