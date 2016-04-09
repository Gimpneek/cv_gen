""" Test form for Personal Profile """
from .common import PersonalProfileTestCase, invalid_name
from cv.forms.profile import ProfileForm
from cv.models import PersonalProfile


class TestFormSkill(PersonalProfileTestCase):
    """
    Test the form for profile
    """

    @staticmethod
    def test_init():
        """
        Test creates the form successfully
        """
        ProfileForm()

    def test_form_valid(self):
        """
        Test that the form checks the validation properly
        """
        form = ProfileForm({
            'name': self.profile.name,
            'email': self.profile.email,
            'website': self.profile.website,
            'portfolio': self.profile.portfolio,
            'personal_statement': self.profile.personal_statement
        })
        self.assertTrue(form.is_valid())

    def test_valid_no_website(self):
        """
        Test that the form says it's valid when no website passed
        """
        form = ProfileForm({
            'name': self.profile.name,
            'email': self.profile.email,
            'portfolio': self.profile.portfolio,
            'personal_statement': self.profile.personal_statement
        })
        self.assertTrue(form.is_valid())

    def test_valid_no_portfolio(self):
        """
        Test that the form says it's valid when no portfolio passed
        """
        form = ProfileForm({
            'name': self.profile.name,
            'email': self.profile.email,
            'website': self.profile.website,
            'personal_statement': self.profile.personal_statement
        })
        self.assertTrue(form.is_valid())

    def test_invalid_name(self):
        """
        Test that the form says it's invalid when no name passed
        """
        form = ProfileForm({
            'email': self.profile.email,
            'website': self.profile.website,
            'portfolio': self.profile.portfolio,
            'personal_statement': self.profile.personal_statement
        })
        self.assertTrue(invalid_name(form))

    def test_invalid_email(self):
        """
        Test that the form says it's invalid when no email passed
        """
        form = ProfileForm({
            'name': self.profile.name,
            'website': self.profile.website,
            'portfolio': self.profile.portfolio,
            'personal_statement': self.profile.personal_statement
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'email': ['This field is required.']
        })

    def test_invalid_pstate(self):
        """
        Test that the form says it's invalid when no personal statement passed
        """
        form = ProfileForm({
            'name': self.profile.name,
            'email': self.profile.email,
            'website': self.profile.website,
            'portfolio': self.profile.portfolio
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'personal_statement': ['This field is required.']
        })

    def test_save(self):
        """
        Test that the form saves
        """
        form = ProfileForm({
            'name': self.profile.name,
            'email': self.profile.email,
            'website': self.profile.website,
            'portfolio': self.profile.portfolio,
            'personal_statement': self.profile.personal_statement
        })
        self.assertEqual(len(PersonalProfile.objects.all()), 1)
        form.save()
        data = form.cleaned_data
        self.assertEqual(data.get('name'), self.profile.name)
        self.assertEqual(data.get('email'), self.profile.email)
        self.assertEqual(data.get('website'), self.profile.website)
        self.assertEqual(data.get('portfolio'), self.profile.portfolio)
        self.assertEqual(data.get('personal_statement'),
                         self.profile.personal_statement)
        self.assertEqual(len(PersonalProfile.objects.all()), 2)
