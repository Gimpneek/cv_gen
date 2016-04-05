""" Test homepage view """
from django.test import TestCase


class TestHomePage(TestCase):
    """
    Test HomePage view
    """

    def setUp(self):
        self.view_resp = self.client.get('/')

    def test_welcome(self):
        """
        Test Welcome is present on homepage
        """
        self.assertContains(self.view_resp, 'Welcome')

    def test_skills_menu(self):
        """
        Test skills in side menu
        """
        self.assertContains(self.view_resp, 'Skills')

    def test_experiences_menu(self):
        """
        Test experiences in side meny
        """
        self.assertContains(self.view_resp, 'Experience')

    def test_education_menu(self):
        """
        Test education in side menu
        """
        self.assertContains(self.view_resp, 'Education')

    def test_profile_menu(self):
        """
        Test profile in side menu
        """
        self.assertContains(self.view_resp, 'Profile')

    def test_generate_cv_menu(self):
        """
        Test generate cv in side menu
        """
        self.assertContains(self.view_resp, 'Generated CVs')
