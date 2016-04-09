""" Test form for Experience """
from .common import ExperienceTestCase
from cv.forms.experience import ExperienceForm
from cv.models import Experience


class TestFormExperience(ExperienceTestCase):
    """
    Test the form for experience
    """

    @staticmethod
    def test_init():
        """
        Test creates the form successfully
        """
        ExperienceForm()

    def test_form_valid(self):
        """
        Test that the form checks the validation properly
        """
        form = ExperienceForm({
            'company': self.experience.company,
            'role': self.experience.role,
            'start_date': self.experience.start_date,
            'end_date': self.experience.end_date,
            'projects':
                [project.pk for project in self.experience.projects.all()],
            'responsibilities':
                [resp.pk for resp in self.experience.responsibilities.all()]
        })
        self.assertTrue(form.is_valid())

    def test_valid_no_end_date(self):
        """
        Test that the form says it's valid when no end date passed
        """
        form = ExperienceForm({
            'company': self.experience.company,
            'role': self.experience.role,
            'start_date': self.experience.start_date,
            'projects':
                [project.pk for project in self.experience.projects.all()],
            'responsibilities':
                [resp.pk for resp in self.experience.responsibilities.all()]
        })
        self.assertTrue(form.is_valid())

    def test_valid_no_project(self):
        """
        Test that the form says it's valid when no project passed
        """
        form = ExperienceForm({
            'company': self.experience.company,
            'role': self.experience.role,
            'start_date': self.experience.start_date,
            'end_date': self.experience.end_date,
            'responsibilities':
                [resp.pk for resp in self.experience.responsibilities.all()]
        })
        self.assertTrue(form.is_valid())

    def test_valid_no_resp(self):
        """
        Test that the form says it's valid when no responsibilities passed
        """
        form = ExperienceForm({
            'company': self.experience.company,
            'role': self.experience.role,
            'start_date': self.experience.start_date,
            'end_date': self.experience.end_date,
            'projects':
                [project.pk for project in self.experience.projects.all()],
        })
        self.assertTrue(form.is_valid())

    def test_invalid_company(self):
        """
        Test that the form says it's invalid when no company passed
        """
        form = ExperienceForm({
            'role': self.experience.role,
            'start_date': self.experience.start_date,
            'end_date': self.experience.end_date,
            'projects':
                [project.pk for project in self.experience.projects.all()],
            'responsibilities':
                [resp.pk for resp in self.experience.responsibilities.all()]
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'company': ['This field is required.']
        })

    def test_invalid_role(self):
        """
        Test that the form says it's invalid when no role passed
        """
        form = ExperienceForm({
            'company': self.experience.company,
            'start_date': self.experience.start_date,
            'end_date': self.experience.end_date,
            'projects':
                [project.pk for project in self.experience.projects.all()],
            'responsibilities':
                [resp.pk for resp in self.experience.responsibilities.all()]
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'role': ['This field is required.']
        })

    def test_invalid_start_date(self):
        """
        Test that the form says it's invalid when no role passed
        """
        form = ExperienceForm({
            'company': self.experience.company,
            'role': self.experience.role,
            'end_date': self.experience.end_date,
            'projects':
                [project.pk for project in self.experience.projects.all()],
            'responsibilities':
                [resp.pk for resp in self.experience.responsibilities.all()]
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'start_date': ['This field is required.']
        })

    def test_save(self):
        """
        Test that the form saves
        """
        form = ExperienceForm({
            'company': self.experience.company,
            'role': self.experience.role,
            'start_date': self.experience.start_date,
            'end_date': self.experience.end_date,
            'projects':
                [project.pk for project in self.experience.projects.all()],
            'responsibilities':
                [resp.pk for resp in self.experience.responsibilities.all()]
        })
        self.assertEqual(len(Experience.objects.all()), 1)
        form.save()
        data = form.cleaned_data
        self.assertEqual(data.get('company'), self.experience.company)
        self.assertEqual(data.get('role'), self.experience.role)
        self.assertEqual(
            data.get('start_date').year,
            int(self.experience.start_date.split('-')[0]))
        self.assertEqual(
            data.get('start_date').month,
            int(self.experience.start_date.split('-')[1]))
        self.assertEqual(
            data.get('start_date').day,
            int(self.experience.start_date.split('-')[2]))
        self.assertEqual(data.get('end_date'), self.experience.end_date)
        self.assertEqual(
            [project.id for project in data.get('projects')],
            [project.id for project in self.experience.projects.all()]
        )
        self.assertEqual(
            [resp.id for resp in data.get('responsibilities')],
            [resp.id for resp in self.experience.responsibilities.all()]
        )
        self.assertEqual(len(Experience.objects.all()), 2)
