""" Unit Tests for CV app """
from django.test import TestCase
from cv.models import PersonalProfile, CV


class TestCV(TestCase):
    """
    Test CV class
    """

    def setUp(self):

        personal_profile = PersonalProfile(
            name="Colin Wren",
            email="colin@gimpneek.com",
            website="http://colinwren.is/awesome",
            portfolio="https://github.com/Gimpneek",
            personal_statement="meh"
        )
        personal_profile.save()

        self.generated_cv = CV(
            name="Test CV",
            personal_profile=personal_profile
        )
        self.generated_cv.save()

        skills = self.generated_cv.skills.create(name="Bow craft Skills")
        skills.save()
        skills.tags.create(name="Awesome")

        exp = self.generated_cv.experiences.create(
            company="Test Corp",
            role="Senior Test Executor",
            start_date="2016-04-02",
            end_date="2016-04-03"
        )
        exp.save()
        exp.projects.create(name='Test Project')
        exp.responsibilities.create(name="Test Responsibility")

        edu = self.generated_cv.education.create(
            institution="Test University",
            start_date="2006-08-01",
            end_date="2009-06-01"
        )
        edu.save()
        edu.courses.create(name="BA (Hons) Testing", mark="First")
        edu.projects.create(name="Test Driven Development")

    def test_name(self):
        """
        Test name is set on CV
        """
        self.assertEqual(self.generated_cv.name, "Test CV")

    def test_personal_profile(self):
        """
        Test personal profile is set on CV
        """
        profile = self.generated_cv.personal_profile
        self.assertEqual(profile.name, "Colin Wren")
        self.assertEqual(profile.email, "colin@gimpneek.com")
        self.assertEqual(profile.website, "http://colinwren.is/awesome")
        self.assertEqual(profile.portfolio, "https://github.com/Gimpneek")
        self.assertEqual(profile.personal_statement, "meh")

    def test_skills(self):
        """
        Test skills are set on CV
        """
        skill = self.generated_cv.skills.get(pk=1)
        self.assertEqual(skill.name, "Bow craft Skills")
        self.assertEqual(skill.tags.get(pk=1).name, "Awesome")

    def test_experience(self):
        """
        Test experience set on CV
        """
        exp = self.generated_cv.experiences.get(pk=1)
        self.assertEqual(exp.company, "Test Corp")
        self.assertEqual(exp.role, "Senior Test Executor")
        self.assertEqual(exp.start_date.year, 2016)
        self.assertEqual(exp.start_date.month, 4)
        self.assertEqual(exp.start_date.day, 2)
        self.assertEqual(exp.end_date.year, 2016)
        self.assertEqual(exp.end_date.month, 4)
        self.assertEqual(exp.end_date.day, 3)
        self.assertEqual(exp.projects.get(pk=1).name, "Test Project")
        self.assertEqual(
            exp.responsibilities.get(pk=1).name,
            "Test Responsibility"
        )

    def test_education(self):
        """
        Test education set on CV
        """
        edu = self.generated_cv.education.get(pk=1)
        self.assertEqual(edu.institution, "Test University")
        self.assertEqual(edu.start_date.year, 2006)
        self.assertEqual(edu.start_date.month, 8)
        self.assertEqual(edu.start_date.day, 1)
        self.assertEqual(edu.end_date.year, 2009)
        self.assertEqual(edu.end_date.month, 6)
        self.assertEqual(edu.end_date.day, 1)
        course = edu.courses.get(pk=1)
        self.assertEqual(course.name, "BA (Hons) Testing")
        self.assertEqual(course.mark, "First")
        self.assertEqual(edu.projects.get(pk=2).name,
                         "Test Driven Development")

    def test_object_name(self):
        """
        Test __str__ for object
        """
        self.assertEqual(str(self.generated_cv), "Test CV")
