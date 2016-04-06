""" Test homepage view """
from django.test import TestCase
from django.core.urlresolvers import reverse_lazy
from bs4 import BeautifulSoup


class TestHomePage(TestCase):
    """
    Test HomePage view
    """

    def setUp(self):
        self.view_resp = self.client.get(reverse_lazy('index'))

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

    def test_menu_highlight(self):
        """
        Test menu is highlighted on list view
        """
        list_resp = self.client.get(reverse_lazy('index'))
        bslist_resp = BeautifulSoup(list_resp.content, 'html.parser')
        menu_list = bslist_resp.select('.menu-list li a')
        for menu_item in menu_list:
            item_class = menu_item.get('class', [''])
            self.assertEqual(item_class[0], '')
