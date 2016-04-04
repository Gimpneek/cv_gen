""" Unit Tests for CV app """
from django.test import TestCase
from django.core.urlresolvers import reverse_lazy
from .models import Tag, Skill, Responsibility, Project, Experience
from .models import Course, Education, PersonalProfile, CV


class TestTag(TestCase):
    """
    Test the tag class
    """

    def setUp(self):
        self.tag = Tag(name="Test Name")

    def test_name(self):
        """
        Test name for tag
        """
        self.assertEqual(self.tag.name, "Test Name")

    def test_object_name(self):
        """
        Test __str__ for object
        """
        self.assertEqual(str(self.tag), "Test Name")


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
        self.view_resp = self.client.get(self.skill.get_absolute_url())

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

    def test_object_name(self):
        """
        Test __str__ for object
        """
        self.assertEqual(str(self.skill), "Test Skill")

    def test_absolute_url(self):
        """
        Test the absolute URL
        """
        self.assertIsNotNone(self.skill.get_absolute_url())

    def test_view_contains_name(self):
        """
        Test the skill model view has name in it
        """
        self.assertContains(self.view_resp, self.skill.name)

    def test_view_contains_profiency(self):
        """
        Test the skill model view has proficiency in it
        """
        self.assertContains(self.view_resp, self.skill.proficiency)

    def test_view_contains_freshness(self):
        """
        Test the skill model view has freshness in it
        """
        self.assertContains(self.view_resp, self.skill.freshness)

    def test_view_contains_tag(self):
        """
        Test the skill model view
        """
        self.assertContains(self.view_resp, self.skill.tags.get(pk=1).name)

    def test_list_view(self):
        """
        Test skill in skills list view
        """
        list_resp = self.client.get(reverse_lazy('skills_list'))
        self.assertContains(list_resp, str(self.skill))

    def test_create_view(self):
        """
        Test create view
        """
        create_resp = self.client.get(reverse_lazy('skill-new'))
        self.assertEqual(create_resp.status_code, 200)


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


class TestProject(TestCase):
    """
    Test Project class
    """

    def setUp(self):
        self.project = Project(name="Test Project")

    def test_name(self):
        """
        Test name is set on project
        """
        self.assertEqual(self.project.name, "Test Project")

    def test_object_name(self):
        """
        Test __str__ for object
        """
        self.assertEqual(str(self.project), "Test Project")


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
        self.view_resp = self.client.get(self.experience.get_absolute_url())

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

    def test_object_name(self):
        """
        Test __str__ for object
        """
        self.assertEqual(str(self.experience),
                         "Senior Test Executor - Test Corp")

    def test_absolute_url(self):
        """
        Test the absolute URL
        """
        self.assertIsNotNone(self.experience.get_absolute_url())

    def test_view_contains_company(self):
        """
        Test the experience model view
        """
        self.assertContains(self.view_resp, self.experience.company)

    def test_view_contains_role(self):
        """
        Test the experience model view
        """
        self.assertContains(self.view_resp, self.experience.role)

    def test_view_contains_start_date(self):
        """
        Test the experience model view
        """
        self.assertContains(self.view_resp, self.experience.start_date)

    def test_view_responsibility(self):
        """
        Test the experience model view
        """
        self.assertContains(self.view_resp,
                            self.experience.responsibilities.get(pk=1).name)

    def test_view_contains_project(self):
        """
        Test the experience model view
        """
        self.assertContains(self.view_resp,
                            self.experience.projects.get(pk=1).name)

    def test_list_view(self):
        """
        Test experience in experiences list view
        """
        list_resp = self.client.get(reverse_lazy('experience_list'))
        self.assertContains(list_resp, str(self.experience))

    def test_create_view(self):
        """
        Test create view
        """
        create_resp = self.client.get(reverse_lazy('experience-new'))
        self.assertEqual(create_resp.status_code, 200)


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

    def test_object_name(self):
        """
        Test __str__ for object
        """
        self.assertEqual(str(self.course), "Test Course")


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
        self.view_resp = self.client.get(self.education.get_absolute_url())

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

    def test_object_name(self):
        """
        Test __str__ for object
        """
        self.assertEqual(str(self.education), "Test University")

    def test_absolute_url(self):
        """
        Test the absolute URL
        """
        self.assertIsNotNone(self.education.get_absolute_url())

    def test_view_contains_institution(self):
        """
        Test the education model view
        """
        self.assertContains(self.view_resp, self.education.institution)

    def test_view_contains_start_date(self):
        """
        Test the education model view
        """
        self.assertContains(self.view_resp, self.education.start_date)

    def test_view_contains_end_date(self):
        """
        Test the education model view
        """
        self.assertContains(self.view_resp, self.education.end_date)

    def test_view_contains_course(self):
        """
        Test the education model view
        """
        self.assertContains(self.view_resp,
                            self.education.courses.get(pk=1).name)

    def test_view_contains_project(self):
        """
        Test the education model view
        """
        self.assertContains(self.view_resp,
                            self.education.projects.get(pk=1).name)

    def test_list_view(self):
        """
        Test education in education list view
        """
        list_resp = self.client.get(reverse_lazy('education_list'))
        self.assertContains(list_resp, str(self.education))

    def test_create_view(self):
        """
        Test create view
        """
        create_resp = self.client.get(reverse_lazy('education-new'))
        self.assertEqual(create_resp.status_code, 200)


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


class TestHomePage(TestCase):
    """
    Test HomePage view
    """

    def setUp(self):
        self.view_resp = self.client.get('/')

    def test_welcome(self):
        """
        Test Welcome is present on homepage
        """
        self.assertContains(self.view_resp, 'Welcome')

    def test_skills_menu(self):
        """
        Test skills in side menu
        """
        self.assertContains(self.view_resp, 'Skills')

    def test_experiences_menu(self):
        """
        Test experiences in side meny
        """
        self.assertContains(self.view_resp, 'Experience')

    def test_education_menu(self):
        """
        Test education in side menu
        """
        self.assertContains(self.view_resp, 'Education')

    def test_profile_menu(self):
        """
        Test profile in side menu
        """
        self.assertContains(self.view_resp, 'Profile')

    def test_generate_cv_menu(self):
        """
        Test generate cv in side menu
        """
        self.assertContains(self.view_resp, 'Generated CVs')
