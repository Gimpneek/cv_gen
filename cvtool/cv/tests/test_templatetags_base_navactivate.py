""" Test for navactive template tag """
from django.test import TestCase, RequestFactory
from cv.templatetags.base_extras import navactive


class TestNavActive(TestCase):
    """
    Test the navactive Template Tag
    """

    def test_catches_on_invalid_url(self):
        """
        Should catch the 404 error and simply return ""
        """
        factory = RequestFactory()
        request = factory.get('/invalidtesturl/')
        nav = navactive(request, 'view1 view2')
        self.assertEqual(nav, '')
