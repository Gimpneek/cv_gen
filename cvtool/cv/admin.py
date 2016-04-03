""" Administation screen setup """
from django.contrib import admin
from .models import Tag, Skill, Responsibility, Project, Experience
from .models import Course, Education, PersonalProfile, CV

admin.site.register(Tag)
admin.site.register(Skill)
admin.site.register(Responsibility)
admin.site.register(Project)
admin.site.register(Experience)
admin.site.register(Course)
admin.site.register(Education)
admin.site.register(PersonalProfile)
admin.site.register(CV)
