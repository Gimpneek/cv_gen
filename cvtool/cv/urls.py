""" URLs for CV App """
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    # Skill URLs
    url(r'^skills/$', views.skills_list, name='skills_list'),
    url(r'^skill/(?P<pk>[0-9]+)/$', views.SkillUpdateView.as_view(),
        name='skill-edit'),
    url(r'^skill/add/$', views.SkillCreateView.as_view(), name='skill-new'),

    # Experience URLs
    url(r'^experiences/$', views.experience_list, name='experience_list'),
    url(r'^experience/(?P<pk>[0-9]+)/$', views.ExperienceUpdateView.as_view(),
        name='experience-edit'),
    url(r'^experience/add/$', views.ExperienceCreateView.as_view(),
        name='experience-new'),

    # Education URLs
    url(r'^educations/$', views.education_list, name='education_list'),
    url(r'^education/(?P<pk>[0-9]+)/$', views.EducationUpdateView.as_view(),
        name='education-edit'),
    url(r'^education/add/$', views.EducationCreateView.as_view(),
        name='education-new'),

    # Profile URLs
    url(r'^profiles/$', views.profiles_list, name='profiles_list'),
    url(r'^profile/(?P<pk>[0-9]+)/$', views.ProfileUpdateView.as_view(),
        name='profile-edit'),
    url(r'^profile/add/$', views.ProfileCreateView.as_view(),
        name='profile-new'),

]
