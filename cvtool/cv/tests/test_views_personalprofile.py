""" Test views for PersonalProfile class """
from django.core.urlresolvers import reverse_lazy
from bs4 import BeautifulSoup
from .common import PersonalProfileTestCase


class TestPersonalProfileViews(PersonalProfileTestCase):
    """
    Test PersonalProfile class
    """

    def setUp(self):
        super(TestPersonalProfileViews, self).setUp()
        self.view_resp = self.client.get(self.profile.get_absolute_url())
        self.bsview_resp = BeautifulSoup(self.view_resp.rendered_content,
                                         'html.parser')

    def test_view_contains_name(self):
        """
        Test the profile model view
        """
        self.assertContains(self.view_resp, self.profile.name)

    def test_view_contains_email(self):
        """
        Test the profile model view
        """
        self.assertContains(self.view_resp, self.profile.email)

    def test_view_contains_website(self):
        """
        Test the profile model view
        """
        self.assertContains(self.view_resp, self.profile.website)

    def test_view_contains_portfolio(self):
        """
        Test the profile model view
        """
        self.assertContains(self.view_resp, self.profile.portfolio)

    def test_view_contains_statement(self):
        """
        Test the profile model view
        """
        self.assertContains(self.view_resp, self.profile.personal_statement)

    def test_list_view(self):
        """
        Test profile in profiles list view
        """
        list_resp = self.client.get(reverse_lazy('profiles_list'))
        self.assertContains(list_resp, str(self.profile))

    def test_create_view(self):
        """
        Test create view
        """
        create_resp = self.client.get(reverse_lazy('profile-new'))
        self.assertEqual(create_resp.status_code, 200)

    def test_menu_highlight_edit(self):
        """
        Test menu is highlighted on edit view
        """
        menu_list = self.bsview_resp.select('.menu-list li a')
        menu_item = \
            [item for item in menu_list if 'Profile' in item.text][0]
        item_class = menu_item.get('class')
        self.assertIsNotNone(item_class)
        self.assertEqual(item_class[0], 'is-active')

    def test_menu_highlight_create(self):
        """
        Test menu is highlighted on create view
        """
        create_resp = self.client.get(reverse_lazy('profile-new'))
        bscreate_resp = BeautifulSoup(create_resp.rendered_content,
                                      'html.parser')
        menu_list = bscreate_resp.select('.menu-list li a')
        menu_item = \
            [item for item in menu_list if 'Profile' in item.text][0]
        item_class = menu_item.get('class')
        self.assertIsNotNone(item_class)
        self.assertEqual(item_class[0], 'is-active')

    def test_menu_highlight_list(self):
        """
        Test menu is highlighted on list view
        """
        list_resp = self.client.get(reverse_lazy('profiles_list'))
        bslist_resp = BeautifulSoup(list_resp.content, 'html.parser')
        menu_list = bslist_resp.select('.menu-list li a')
        menu_item = \
            [item for item in menu_list if 'Profile' in item.text][0]
        item_class = menu_item.get('class')
        self.assertIsNotNone(item_class)
        self.assertEqual(item_class[0], 'is-active')
