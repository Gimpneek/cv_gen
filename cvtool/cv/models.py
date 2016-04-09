""" Models for CV Tool """
from django.db import models
from django.core.urlresolvers import reverse


class Skill(models.Model):
    """
    Model to hold job hunters skills
    """
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
    name = models.CharField(max_length=256, help_text="Name of skill",
                            default="")
    proficiency = models.SmallIntegerField(
        choices=proficiency_choices,
        help_text="Proficiency of skill",
        default=3
    )
    freshness = models.SmallIntegerField(
        choices=freshness_choices,
        help_text="Is skill current practice?",
        default=4
    )
    tags = models.ManyToManyField("Tag", help_text='Tags', blank=True)

    def __str__(self):
        """
        String to return as the representation of this model
        """
        return self.name

    def get_absolute_url(self):
        """
        URL to use when submitting forms
        """
        return reverse('skill-edit', kwargs={'pk': self.pk})


class Tag(models.Model):
    """
    Model to hold the information for tags assigned to skills and the like
    """
    name = models.CharField(
        max_length=128,
        help_text="Name of tag"
    )

    def __str__(self):
        """
        String to return as the representation of this model
        """
        return self.name


class Responsibility(models.Model):
    """
    Model to hold the responsibilities job hunter had in jobs
    """
    name = models.CharField(
        max_length=256,
        help_text="Name of responsibility"
    )

    def __str__(self):
        """
        String to return as the representation of this model
        """
        return self.name


class Project(models.Model):
    """
    Model to hold the projects job hunter did in jobs and education
    """
    name = models.CharField(
        max_length=256,
        help_text="Name of project"
    )

    def __str__(self):
        """
        String to return as the representation of this model
        """
        return self.name


class Experience(models.Model):
    """
    Model to hold the experience and jobs they've had
    """
    company = models.CharField(
        max_length=256,
        help_text="Company worked for",
        default=""
    )
    role = models.CharField(
        max_length=256,
        help_text="Role/Position held",
        default=""
    )
    start_date = models.DateField(
        help_text="Date started job",
        default=""
    )
    end_date = models.DateField(
        help_text="Date ended job",
        null=True,
        blank=True
    )
    projects = models.ManyToManyField(
        Project, blank=True,
        help_text="Projects worked on during employment")
    responsibilities = models.ManyToManyField(
        Responsibility, blank=True,
        help_text="Responsibilities of job?"
    )

    def __str__(self):
        """
        String to return as the representation of this model
        """
        return "{0} - {1}".format(self.role, self.company)

    def get_absolute_url(self):
        """
        URL for form submission
        """
        return reverse('experience-edit', kwargs={'pk': self.pk})


class Course(models.Model):
    """
    Model to hold the information on the courses took as part of education
    """
    name = models.CharField(
        max_length=256,
        help_text="Name of course taken"
    )
    mark = models.CharField(
        max_length=128,
        help_text="Mark given"
    )

    def __str__(self):
        """
        String to return as the representation of this model
        """
        return self.name


class Education(models.Model):
    """
    Model to hold the education the job hunter has been through
    """
    institution = models.CharField(
        max_length=256,
        help_text="Institution studied at",
        default=""
    )
    start_date = models.DateField(
        help_text="Date started studies"
    )
    end_date = models.DateField(
        help_text="Date ended studies",
        null=True,
        blank=True
    )
    courses = models.ManyToManyField(Course, help_text="Courses studied")
    projects = models.ManyToManyField(
        Project, blank=True,
        help_text="Projects completed during studies")

    def __str__(self):
        """
        String to return as the representation of this model
        """
        return self.institution

    def get_absolute_url(self):
        """
        URL for form submission
        """
        return reverse('education-edit', kwargs={'pk': self.pk})


class PersonalProfile(models.Model):
    """
    Model to hold the profile information of the job hunter
    """
    name = models.CharField(
        max_length=256,
        help_text="Your name",
        default=""
    )
    email = models.EmailField(
        help_text="Your email address",
        default=""
    )
    website = models.URLField(
        help_text="Your website URL",
        blank=True,
        default=""
    )
    portfolio = models.URLField(
        help_text="Your portfolio URL",
        blank=True,
        default=""
    )
    personal_statement = models.TextField(
        help_text="Personal Statement to summarise who you are",
        default=""
    )

    def __str__(self):
        """
        String to return as the representation of this model
        """
        return self.name

    def get_absolute_url(self):
        """
        URL for form submission
        """
        return reverse('profile-edit', kwargs={'pk': self.pk})


class CV(models.Model):
    """
    Model to hold the generated CV with the information tailored to the search
    that generated it
    """
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
        """
        String to return as the representation of this model
        """
        return self.name
