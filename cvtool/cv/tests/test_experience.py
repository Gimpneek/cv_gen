""" Tests for experience class """
from django.test import TestCase
from django.core.urlresolvers import reverse_lazy
from cv.models import Experience


class TestExperience(TestCase):
    """
    Test Experience class
    """

    def setUp(self):
        self.experience = Experience(
            company="Test Corp",
            role="Senior Test Executor",
            start_date="2016-04-02"
        )
        self.experience.save()
        self.experience.projects.create(name='Test Project')
        self.experience.responsibilities.create(name="Test Responsibility")
        self.view_resp = self.client.get(self.experience.get_absolute_url())

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

    def test_view_contains_company(self):
        """
        Test the experience model view
        """
        self.assertContains(self.view_resp, self.experience.company)

    def test_view_contains_role(self):
        """
        Test the experience model view
        """
        self.assertContains(self.view_resp, self.experience.role)

    def test_view_contains_start_date(self):
        """
        Test the experience model view
        """
        self.assertContains(self.view_resp, self.experience.start_date)

    def test_view_responsibility(self):
        """
        Test the experience model view
        """
        self.assertContains(self.view_resp,
                            self.experience.responsibilities.get(pk=1).name)

    def test_view_contains_project(self):
        """
        Test the experience model view
        """
        self.assertContains(self.view_resp,
                            self.experience.projects.get(pk=1).name)

    def test_list_view(self):
        """
        Test experience in experiences list view
        """
        list_resp = self.client.get(reverse_lazy('experience_list'))
        self.assertContains(list_resp, str(self.experience))

    def test_create_view(self):
        """
        Test create view
        """
        create_resp = self.client.get(reverse_lazy('experience-new'))
        self.assertEqual(create_resp.status_code, 200)
