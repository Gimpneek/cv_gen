""" Tests view for Skill class """
from django.core.urlresolvers import reverse_lazy
from bs4 import BeautifulSoup
from .common import SkillTestCase


class TestSkillViews(SkillTestCase):
    """
    Test the skill class
    """

    def setUp(self):
        super(TestSkillViews, self).setUp()
        self.view_resp = self.client.get(self.skill.get_absolute_url())
        self.bsview_resp = BeautifulSoup(self.view_resp.rendered_content,
                                         'html.parser')

    def test_view_contains_name(self):
        """
        Test the skill model view has name in it
        """
        self.assertContains(self.view_resp, self.skill.name)

    def test_view_contains_profiency(self):
        """
        Test the skill model view has proficiency in it
        """
        self.assertContains(self.view_resp, self.skill.proficiency)

    def test_view_contains_freshness(self):
        """
        Test the skill model view has freshness in it
        """
        self.assertContains(self.view_resp, self.skill.freshness)

    def test_view_contains_tag(self):
        """
        Test the skill model view
        """
        self.assertContains(self.view_resp, self.skill.tags.get(pk=1).name)

    def test_list_view(self):
        """
        Test skill in skills list view
        """
        list_resp = self.client.get(reverse_lazy('skills_list'))
        self.assertContains(list_resp, str(self.skill))

    def test_create_view(self):
        """
        Test create view
        """
        create_resp = self.client.get(reverse_lazy('skill-new'))
        self.assertEqual(create_resp.status_code, 200)

    def test_menu_highlight_edit(self):
        """
        Test menu is highlighted on edit view
        """
        menu_list = self.bsview_resp.select('.menu-list li a')
        menu_item = [item for item in menu_list if 'Skill' in item.text][0]
        item_class = menu_item.get('class')
        self.assertIsNotNone(item_class)
        self.assertEqual(item_class[0], 'is-active')

    def test_menu_highlight_create(self):
        """
        Test menu is highlighted on create view
        """
        create_resp = self.client.get(reverse_lazy('skill-new'))
        bscreate_resp = BeautifulSoup(create_resp.rendered_content,
                                      'html.parser')
        menu_list = bscreate_resp.select('.menu-list li a')
        menu_item = [item for item in menu_list if 'Skill' in item.text][0]
        item_class = menu_item.get('class')
        self.assertIsNotNone(item_class)
        self.assertEqual(item_class[0], 'is-active')

    def test_menu_highlight_list(self):
        """
        Test menu is highlighted on list view
        """
        list_resp = self.client.get(reverse_lazy('skills_list'))
        bslist_resp = BeautifulSoup(list_resp.content, 'html.parser')
        menu_list = bslist_resp.select('.menu-list li a')
        menu_item = [item for item in menu_list if 'Skill' in item.text][0]
        item_class = menu_item.get('class')
        self.assertIsNotNone(item_class)
        self.assertEqual(item_class[0], 'is-active')
