""" Common setUp for tests """
from django.test import TestCase
from cv.models import Education, PersonalProfile, Experience, Skill


class EducationTestCase(TestCase):
    """
    Common stuff needed for testing education class
    """

    def setUp(self):
        self.education = Education(
            institution="Test University",
            start_date="2006-08-01",
            end_date="2009-06-01"
        )
        self.education.save()
        self.education.courses.create(name="BA (Hons) Testing", mark="First")
        self.education.projects.create(name="Test Driven Development")


class PersonalProfileTestCase(TestCase):
    """
    Common setUp needed for testing PersonalProfile class
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


class ExperienceTestCase(TestCase):
    """
    Common setUp needed for testing Experience class
    """

    def setUp(self):
        self.experience = Experience(
            company="Test Corp",
            role="Senior Test Executor",
            start_date="2016-04-02"
        )
        self.experience.save()
        self.experience.projects.create(name='Test Project')
        self.experience.responsibilities.create(name="Test Responsibility")


class SkillTestCase(TestCase):
    """
    Common setUp needed for testing Skill class
    """

    def setUp(self):
        self.skill = Skill(
            name="Test Skill",
            proficiency=5,
            freshness=2
        )
        self.skill.save()
        self.skill.tags.create(name="Test Tag")


def invalid_start_date(form):
    """ Test that the form is invalid and has an error for start date """
    valid = form.is_valid()
    error_msg = form.errors.get('start_date')
    return not valid and error_msg == ['This field is required.']


def invalid_name(form):
    """ Test that the form is invalid and has an error for name """
    valid = form.is_valid()
    error_msg = form.errors.get('name')
    return not valid and error_msg == ['This field is required.']
