from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^skills', views.skills_list, name='skills_list'),
    url(r'^experiences$', views.experience_list, name='experience_list'),
    url(r'^educations$', views.education_list, name='education_list'),
]