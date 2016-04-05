""" Test for PersonalProfile class """
from .common import PersonalProfileTestCase


class TestPersonalProfile(PersonalProfileTestCase):
    """
    Test PersonalProfile class
    """

    def test_name(self):
        """
        Test name set on PersonalProfile
        """
        self.assertEqual(self.profile.name, "Colin Wren")

    def test_email(self):
        """
        Test email set on PersonalProfile
        """
        self.assertEqual(self.profile.email, "colin@gimpneek.com")

    def test_website(self):
        """
        Test website set on PersonalProfile
        """
        self.assertEqual(self.profile.website, "http://colinwren.is/awesome")

    def test_portfolio(self):
        """
        Test portfolio set on PersonalProfile
        """
        self.assertEqual(self.profile.portfolio, "https://github.com/Gimpneek")

    def test_personal_statement(self):
        """
        Test personal statement set on PersonalProfile
        """
        self.assertEqual(
            self.profile.personal_statement,
            "Disciplined Software Development Manager and "
            "Developer with a passion for delivering high "
            "quality and valuable software."
        )

    def test_object_name(self):
        """
        Test __str__ for object
        """
        self.assertEqual(str(self.profile), "Colin Wren")

    def test_absolute_url(self):
        """
        Test the absolute URL
        """
        self.assertIsNotNone(self.profile.get_absolute_url())
