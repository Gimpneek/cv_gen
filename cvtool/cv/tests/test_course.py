""" Tests for course class """
from django.test import TestCase
from cv.models import Course


class TestCourse(TestCase):
    """
    Test Course class
    """

    def setUp(self):
        self.course = Course(name="Test Course", mark="Distinction")

    def test_name(self):
        """
        Test name is set on Course
        """
        self.assertEqual(self.course.name, "Test Course")

    def test_mark(self):
        """
        Test mark is set on Course
        """
        self.assertEqual(self.course.mark, "Distinction")

    def test_object_name(self):
        """
        Test __str__ for object
        """
        self.assertEqual(str(self.course), "Test Course")
