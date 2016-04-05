""" Tests for education class """
from .common import EducationTestCase


class TestEducation(EducationTestCase):
    """
    Test Education class
    """

    def test_institution(self):
        """
        Test institution is set on Education
        """
        self.assertEqual(self.education.institution, "Test University")

    def test_courses(self):
        """
        Test courses is set on Education
        """
        course = self.education.courses.get(pk=1)
        self.assertEqual(course.name, "BA (Hons) Testing")
        self.assertEqual(course.mark, "First")

    def test_start_date(self):
        """
        Test start_date is set on Education
        """
        self.assertEqual(self.education.start_date, "2006-08-01")

    def test_end_date(self):
        """
        Test end_date is set on Education
        """
        self.assertEqual(self.education.end_date, "2009-06-01")

    def test_projects(self):
        """
        Test projects is set on Education
        """
        self.assertEqual(
            self.education.projects.get(pk=1).name,
            "Test Driven Development"
        )

    def test_object_name(self):
        """
        Test __str__ for object
        """
        self.assertEqual(str(self.education), "Test University")

    def test_absolute_url(self):
        """
        Test the absolute URL
        """
        self.assertIsNotNone(self.education.get_absolute_url())
