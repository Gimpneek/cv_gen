""" Test responsibility class """
from django.test import TestCase
from cv.models import Responsibility


class TestResponsibility(TestCase):
    """
    Test Responsibility class
    """

    def setUp(self):
        self.resp = Responsibility(name="Test Responsibility")

    def test_name(self):
        """
        Test name is set on object
        """
        self.assertEqual(self.resp.name, "Test Responsibility")

    def test_object_name(self):
        """
        Test __str__ for object
        """
        self.assertEqual(str(self.resp), "Test Responsibility")
