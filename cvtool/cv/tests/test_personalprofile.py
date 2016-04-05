from django.test import TestCase
from django.core.urlresolvers import reverse_lazy
from cv.models import PersonalProfile


class TestPersonalProfile(TestCase):
    """
    Test PersonalProfile class
    """

    def setUp(self):
        self.profile = PersonalProfile(
            name="Colin Wren",
            email="colin@gimpneek.com",
            website="http://colinwren.is/awesome",
            portfolio="https://github.com/Gimpneek",
            personal_statement="Disciplined Software Development Manager and "
                               "Developer with a passion for delivering high "
                               "quality and valuable software."
        )
        self.profile.save()
        self.view_resp = self.client.get(self.profile.get_absolute_url())

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
