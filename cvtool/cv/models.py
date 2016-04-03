from django.db import models
from django.core.urlresolvers import reverse


class Skill(models.Model):

    proficiency_choices = (
        (1, "No Proficiency"),
        (2, "Basic Understanding"),
        (3, "Working Knowledge"),
        (4, "Advanced Knowledge"),
        (5, "Expert Knowledge")
    )
    freshness_choices = (
        (1, "Not Current Practice"),
        (2, "Out of Date"),
        (3, "On Way Out"),
        (4, "Current Practice"),
        (5, "Not Widely Adopted Yet")
    )
    name = models.CharField(max_length=256, help_text="Name of skill")
    proficiency = models.SmallIntegerField(
        choices=proficiency_choices,
        help_text="Proficiency of skill",
        default=2
    )
    freshness = models.SmallIntegerField(
        choices=freshness_choices,
        help_text="Is skill current practice?",
        default=4
    )
    tags = models.ManyToManyField("Tag")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('skill-edit', kwargs={'pk': self.pk})


class Tag(models.Model):
    name = models.CharField(
        max_length=128,
        help_text="Name of tag"
    )

    def __str__(self):
        return self.name


class Responsibility(models.Model):
    name = models.CharField(
        max_length=256,
        help_text="Name of responsibility"
    )

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(
        max_length=256,
        help_text="Name of project"
    )

    def __str__(self):
        return self.name


class Experience(models.Model):
    company = models.CharField(
        max_length=256,
        help_text="Company worked for"
    )
    role = models.CharField(
        max_length=256,
        help_text="Role/Position held"
    )
    start_date = models.DateField(
        help_text="Date started job"
    )
    end_date = models.DateField(
        help_text="Date ended job",
        null=True,
        blank=True
    )
    projects = models.ManyToManyField(Project, blank=True)
    responsibilities = models.ManyToManyField(Responsibility, blank=True)

    def __str__(self):
        return "{0} - {1}".format(self.role, self.company)

    def get_absolute_url(self):
        return reverse('experience-edit', kwargs={'pk': self.pk})


class Course(models.Model):
    name = models.CharField(
        max_length=256,
        help_text="Name of course taken"
    )
    mark = models.CharField(
        max_length=128,
        help_text="Mark given"
    )

    def __str__(self):
        return self.name


class Education(models.Model):
    institution = models.CharField(
        max_length=256,
        help_text="Institution studied at"
    )
    start_date = models.DateField(
        help_text="Date started studies"
    )
    end_date = models.DateField(
        help_text="Date ended studies",
        null=True,
        blank=True
    )
    courses = models.ManyToManyField(Course)
    projects = models.ManyToManyField(Project, blank=True)

    def __str__(self):
        return self.institution

    def get_absolute_url(self):
        return reverse('education-edit', kwargs={'pk': self.pk})


class PersonalProfile(models.Model):
    name = models.CharField(
        max_length=256,
        help_text="Your name"
    )
    email = models.EmailField(
        help_text="Your email address"
    )
    website = models.URLField(
        help_text="Your website URL"
    )
    portfolio = models.URLField(
        help_text="Your portfolio URL"
    )
    personal_statement = models.TextField(
        help_text="Personal Statement to summarise who you are"
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('profile-edit', kwargs={'pk': self.pk})


class CV(models.Model):
    name = models.CharField(
        max_length=256,
        help_text="name of CV"
    )
    personal_profile = models.ForeignKey(
        PersonalProfile,
        help_text="Personal Profile to use"
    )
    skills = models.ManyToManyField(Skill, help_text="Skills to use")
    experiences = models.ManyToManyField(
        Experience,
        help_text="Experiences to use"
    )
    education = models.ManyToManyField(
        Education,
        help_text="Education to use"
    )

    def __str__(self):
        return self.name
