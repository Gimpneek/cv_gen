""" Tests views for experience class """
from django.core.urlresolvers import reverse_lazy
from bs4 import BeautifulSoup
from .common import ExperienceTestCase


class TestExperienceViews(ExperienceTestCase):
    """
    Test Experience class
    """

    def setUp(self):
        super(TestExperienceViews, self).setUp()
        self.view_resp = self.client.get(self.experience.get_absolute_url())
        self.bsview_resp = BeautifulSoup(self.view_resp.rendered_content,
                                         'html.parser')

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

    def test_menu_highlight_edit(self):
        """
        Test menu is highlighted on edit view
        """
        menu_list = self.bsview_resp.select('.menu-list li a')
        menu_item = \
            [item for item in menu_list if 'Experience' in item.text][0]
        item_class = menu_item.get('class')
        self.assertIsNotNone(item_class)
        self.assertEqual(item_class[0], 'is-active')

    def test_menu_highlight_create(self):
        """
        Test menu is highlighted on create view
        """
        create_resp = self.client.get(reverse_lazy('experience-new'))
        bscreate_resp = BeautifulSoup(create_resp.rendered_content,
                                      'html.parser')
        menu_list = bscreate_resp.select('.menu-list li a')
        menu_item = \
            [item for item in menu_list if 'Experience' in item.text][0]
        item_class = menu_item.get('class')
        self.assertIsNotNone(item_class)
        self.assertEqual(item_class[0], 'is-active')

    def test_menu_highlight_list(self):
        """
        Test menu is highlighted on list view
        """
        list_resp = self.client.get(reverse_lazy('experience_list'))
        bslist_resp = BeautifulSoup(list_resp.content, 'html.parser')
        menu_list = bslist_resp.select('.menu-list li a')
        menu_item = \
            [item for item in menu_list if 'Experience' in item.text][0]
        item_class = menu_item.get('class')
        self.assertIsNotNone(item_class)
        self.assertEqual(item_class[0], 'is-active')
