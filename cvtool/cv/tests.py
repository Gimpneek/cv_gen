from django.test import TestCase
from .models import *


class TestTag(TestCase):
    """
    Test the tag class
    """

    def test_name(self):
        """
        Test name for tag
        """
        tag = Tag(name="Test Name")
        self.assertEqual(tag.name, "Test Name")


class TestSkill(TestCase):
    """
    Test the skill class
    """

    def setUp(self):
        self.skill = Skill(
            name="Test Skill",
            proficiency=5,
            freshness=2
        )
        self.skill.save()
        self.skill.tags.create(name="Test Tag")

    def test_name(self):
        """
        Test name for skill
        """
        self.assertEqual(self.skill.name, "Test Skill")

    def test_proficiency(self):
        """
        Test proficiency for skill
        """
        self.assertEqual(self.skill.proficiency, 5)

    def test_freshness(self):
        """
        Test freshness for skill
        """
        self.assertEqual(self.skill.freshness, 2)

    def test_tag(self):
        """
        Test tag for skill
        """
        self.assertEqual(self.skill.tags.get(pk=1).name, "Test Tag")


class TestResponsibility(TestCase):
    """
    Test Responsibility class
    """

    def test_name(self):
        """
        Test name is set on object
        """
        resp = Responsibility(name="Test Responsibility")
        self.assertEqual(resp.name, "Test Responsibility")


class TestProject(TestCase):
    """
    Test Project class
    """

    def test_name(self):
        """
        Test name is set on project
        """
        project = Project(name="Test Project")
        self.assertEqual(project.name, "Test Project")


class TestExperience(TestCase):
    """
    Test Experience class
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

    def test_company(self):
        """
        Test company is set on experience
        """
        self.assertEqual(self.experience.company, "Test Corp")

    def test_role(self):
        """
        Test role is set on experience
        """
        self.assertEqual(self.experience.role, "Senior Test Executor")

    def test_start_date(self):
        """
        Test start_date is set on experience
        """
        self.assertEqual(self.experience.start_date, "2016-04-02")

    def test_end_date(self):
        """
        Test end_date is set on experience
        """
        self.assertEqual(self.experience.end_date, None)

    def test_responsibilities(self):
        """
        Test responsibilities is set on experience
        """
        self.assertEqual(
            self.experience.responsibilities.get(pk=1).name,
            "Test Responsibility"
        )

    def test_projects(self):
        """
        Test projects is set on experience
        """
        self.assertEqual(
            self.experience.projects.get(pk=1).name,
            "Test Project"
        )


class TestCourse(TestCase):
    """
    Test Course class
    """

    def setUp(self):
        self.course = Course(name="Test Course", mark="Distinction")

    def test_name(self):
        """
        Test name is set on Course
        """
        self.assertEqual(self.course.name, "Test Course")

    def test_mark(self):
        """
        Test mark is set on Course
        """
        self.assertEqual(self.course.mark, "Distinction")


class TestEducation(TestCase):
    """
    Test Education class
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

    def test_institution(self):
        """
        Test institution is set on Education
        """
        self.assertEqual(self.education.institution, "Test University")

    def test_courses(self):
        """
        Test courses is set on Education
        """
        course = self.education.courses.get(pk=1)
        self.assertEqual(course.name, "BA (Hons) Testing")
        self.assertEqual(course.mark, "First")

    def test_start_date(self):
        """
        Test start_date is set on Education
        """
        self.assertEqual(self.education.start_date, "2006-08-01")

    def test_end_date(self):
        """
        Test end_date is set on Education
        """
        self.assertEqual(self.education.end_date, "2009-06-01")

    def test_projects(self):
        """
        Test projects is set on Education
        """
        self.assertEqual(
            self.education.projects.get(pk=1).name,
            "Test Driven Development"
        )


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

        self.cv = CV(
            name="Test CV",
            personal_profile=personal_profile
        )
        self.cv.save()

        skills = self.cv.skills.create(name="Bow craft Skills")
        skills.save()
        skills.tags.create(name="Awesome")

        exp = self.cv.experiences.create(
            company="Test Corp",
            role="Senior Test Executor",
            start_date="2016-04-02",
            end_date="2016-04-03"
        )
        exp.save()
        exp.projects.create(name='Test Project')
        exp.responsibilities.create(name="Test Responsibility")

        edu = self.cv.education.create(
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
        self.assertEqual(self.cv.name, "Test CV")

    def test_personal_profile(self):
        """
        Test personal profile is set on CV
        """
        pp = self.cv.personal_profile
        self.assertEqual(pp.name, "Colin Wren")
        self.assertEqual(pp.email, "colin@gimpneek.com")
        self.assertEqual(pp.website, "http://colinwren.is/awesome")
        self.assertEqual(pp.portfolio, "https://github.com/Gimpneek")
        self.assertEqual(pp.personal_statement, "meh")

    def test_skills(self):
        """
        Test skills are set on CV
        """
        skill = self.cv.skills.get(pk=1)
        self.assertEqual(skill.name, "Bow craft Skills")
        self.assertEqual(skill.tags.get(pk=1).name, "Awesome")

    def test_experience(self):
        """
        Test experience set on CV
        """
        exp = self.cv.experiences.get(pk=1)
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
        edu = self.cv.education.get(pk=1)
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
        self.assertEqual(edu.projects.get(pk=2).name, "Test Driven Development")
