""" Tests views for education class """
from django.core.urlresolvers import reverse_lazy
from bs4 import BeautifulSoup
from .common import EducationTestCase


class TestEducationViews(EducationTestCase):
    """
    Test Education class
    """

    def setUp(self):
        super(TestEducationViews, self).setUp()
        self.view_resp = self.client.get(self.education.get_absolute_url())
        self.bsview_resp = BeautifulSoup(self.view_resp.rendered_content,
                                         'html.parser')

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

    def test_menu_highlight_edit(self):
        """
        Test menu is highlighted on edit view
        """
        menu_list = self.bsview_resp.select('.menu-list li a')
        menu_item = \
            [item for item in menu_list if 'Education' in item.text][0]
        item_class = menu_item.get('class')
        self.assertIsNotNone(item_class)
        self.assertEqual(item_class[0], 'is-active')

    def test_menu_highlight_create(self):
        """
        Test menu is highlighted on create view
        """
        create_resp = self.client.get(reverse_lazy('education-new'))
        bscreate_resp = BeautifulSoup(create_resp.rendered_content,
                                      'html.parser')
        menu_list = bscreate_resp.select('.menu-list li a')
        menu_item = \
            [item for item in menu_list if 'Education' in item.text][0]
        item_class = menu_item.get('class')
        self.assertIsNotNone(item_class)
        self.assertEqual(item_class[0], 'is-active')

    def test_menu_highlight_list(self):
        """
        Test menu is highlighted on list view
        """
        list_resp = self.client.get(reverse_lazy('education_list'))
        bslist_resp = BeautifulSoup(list_resp.content, 'html.parser')
        menu_list = bslist_resp.select('.menu-list li a')
        menu_item = \
            [item for item in menu_list if 'Education' in item.text][0]
        item_class = menu_item.get('class')
        self.assertIsNotNone(item_class)
        self.assertEqual(item_class[0], 'is-active')
