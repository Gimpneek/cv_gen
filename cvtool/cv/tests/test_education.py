""" Tests for education class """
from django.test import TestCase
from django.core.urlresolvers import reverse_lazy
from cv.models import Education


class TestEducation(TestCase):
    """
    Test Education class
    """

    def setUp(self):
        self.education = Education(
            institution="Test University",
            start_date="2006-08-01",
            end_date="2009-06-01"
        )
        self.education.save()
        self.education.courses.create(name="BA (Hons) Testing", mark="First")
        self.education.projects.create(name="Test Driven Development")
        self.view_resp = self.client.get(self.education.get_absolute_url())

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

    def test_view_contains_institution(self):
        """
        Test the education model view
        """
        self.assertContains(self.view_resp, self.education.institution)

    def test_view_contains_start_date(self):
        """
        Test the education model view
        """
        self.assertContains(self.view_resp, self.education.start_date)

    def test_view_contains_end_date(self):
        """
        Test the education model view
        """
        self.assertContains(self.view_resp, self.education.end_date)

    def test_view_contains_course(self):
        """
        Test the education model view
        """
        self.assertContains(self.view_resp,
                            self.education.courses.get(pk=1).name)

    def test_view_contains_project(self):
        """
        Test the education model view
        """
        self.assertContains(self.view_resp,
                            self.education.projects.get(pk=1).name)

    def test_list_view(self):
        """
        Test education in education list view
        """
        list_resp = self.client.get(reverse_lazy('education_list'))
        self.assertContains(list_resp, str(self.education))

    def test_create_view(self):
        """
        Test create view
        """
        create_resp = self.client.get(reverse_lazy('education-new'))
        self.assertEqual(create_resp.status_code, 200)
