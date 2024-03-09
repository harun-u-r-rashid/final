from django.contrib import admin

from .models import Blog, Contact, Skill, Project, Resume , ProjectReview


admin.site.register(Skill)
admin.site.register(Contact)
admin.site.register(Blog)
admin.site.register(Project)
admin.site.register(ProjectReview)
admin.site.register(Resume)
