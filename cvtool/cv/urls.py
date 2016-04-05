""" URLs for CV App """
from django.conf.urls import url
from .views.homepage import index
from .views.skill import skills_list, SkillUpdateView, SkillCreateView
from .views.experience import experience_list, ExperienceUpdateView, \
    ExperienceCreateView
from .views.education import education_list, EducationUpdateView, \
    EducationCreateView
from .views.profile import profiles_list, ProfileUpdateView, ProfileCreateView

urlpatterns = [
    url(r'^$', index, name='index'),

    # Skill URLs
    url(r'^skills/$', skills_list, name='skills_list'),
    url(r'^skill/(?P<pk>[0-9]+)/$', SkillUpdateView.as_view(),
        name='skill-edit'),
    url(r'^skill/add/$', SkillCreateView.as_view(), name='skill-new'),

    # Experience URLs
    url(r'^experiences/$', experience_list, name='experience_list'),
    url(r'^experience/(?P<pk>[0-9]+)/$', ExperienceUpdateView.as_view(),
        name='experience-edit'),
    url(r'^experience/add/$', ExperienceCreateView.as_view(),
        name='experience-new'),

    # Education URLs
    url(r'^educations/$', education_list, name='education_list'),
    url(r'^education/(?P<pk>[0-9]+)/$', EducationUpdateView.as_view(),
        name='education-edit'),
    url(r'^education/add/$', EducationCreateView.as_view(),
        name='education-new'),

    # Profile URLs
    url(r'^profiles/$', profiles_list, name='profiles_list'),
    url(r'^profile/(?P<pk>[0-9]+)/$', ProfileUpdateView.as_view(),
        name='profile-edit'),
    url(r'^profile/add/$', ProfileCreateView.as_view(),
        name='profile-new'),

]
