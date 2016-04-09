""" Test form for Education """
from .common import EducationTestCase, invalid_start_date
from cv.forms.education import EducationForm
from cv.models import Education


class TestFormEducation(EducationTestCase):
    """
    Test the form for education
    """

    @staticmethod
    def test_init():
        """
        Test creates the form successfully
        """
        EducationForm()

    def test_form_valid(self):
        """
        Test that the form checks the validation properly
        """
        form = EducationForm({
            'institution': self.education.institution,
            'start_date': self.education.start_date,
            'end_date': self.education.end_date,
            'courses': [course.pk for course in self.education.courses.all()],
            'projects': [proj.pk for proj in self.education.projects.all()]
        })
        self.assertTrue(form.is_valid())

    def test_valid_no_end_date(self):
        """
        Test that the form says it's valid when no end_date passed
        """
        form = EducationForm({
            'institution': self.education.institution,
            'start_date': self.education.start_date,
            'courses': [course.pk for course in self.education.courses.all()],
            'projects': [proj.pk for proj in self.education.projects.all()]
        })
        self.assertTrue(form.is_valid())

    def test_valid_no_project(self):
        """
        Test that the form says it's valid when no projects passed
        """
        form = EducationForm({
            'institution': self.education.institution,
            'start_date': self.education.start_date,
            'end_date': self.education.end_date,
            'courses': [course.pk for course in self.education.courses.all()]
        })
        self.assertTrue(form.is_valid())

    def test_invalid_institute(self):
        """
        Test that the form says it's invalid when institute passed
        """
        form = EducationForm({
            'start_date': self.education.start_date,
            'end_date': self.education.end_date,
            'courses': [course.pk for course in self.education.courses.all()],
            'projects': [proj.pk for proj in self.education.projects.all()]
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'institution': ['This field is required.']
        })

    def test_invalid_start_date(self):
        """
        Test that the form says it's invalid when start_date passed
        """
        form = EducationForm({
            'institution': self.education.institution,
            'end_date': self.education.end_date,
            'courses': [course.pk for course in self.education.courses.all()],
            'projects': [proj.pk for proj in self.education.projects.all()]
        })
        self.assertTrue(invalid_start_date(form))

    def test_invalid_course(self):
        """
        Test that the form says it's valid when no course passed
        """
        form = EducationForm({
            'institution': self.education.institution,
            'start_date': self.education.start_date,
            'end_date': self.education.end_date,
            'projects': [proj.pk for proj in self.education.projects.all()]
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'courses': ['This field is required.']
        })

    def test_save(self):
        """
        Test that the form saves
        """
        form = EducationForm({
            'institution': self.education.institution,
            'start_date': self.education.start_date,
            'end_date': self.education.end_date,
            'courses': [course.pk for course in self.education.courses.all()],
            'projects': [proj.pk for proj in self.education.projects.all()]
        })
        self.assertEqual(len(Education.objects.all()), 1)
        form.save()
        data = form.cleaned_data
        self.assertEqual(data.get('institution'), self.education.institution)
        self.assertEqual(
            data.get('start_date').year,
            int(self.education.start_date.split('-')[0]))
        self.assertEqual(
            data.get('start_date').month,
            int(self.education.start_date.split('-')[1]))
        self.assertEqual(
            data.get('start_date').day,
            int(self.education.start_date.split('-')[2]))
        self.assertEqual(
            data.get('end_date').year,
            int(self.education.end_date.split('-')[0]))
        self.assertEqual(
            data.get('end_date').month,
            int(self.education.end_date.split('-')[1]))
        self.assertEqual(
            data.get('end_date').day,
            int(self.education.end_date.split('-')[2]))
        self.assertEqual(
            [course.id for course in data.get('courses')],
            [course.id for course in self.education.courses.all()]
        )
        self.assertEqual(
            [project.id for project in data.get('projects')],
            [project.id for project in self.education.projects.all()]
        )
        self.assertEqual(len(Education.objects.all()), 2)
