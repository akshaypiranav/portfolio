from django.contrib import admin

# Register your models here.
from .models import Projects,ResumeModel

admin.site.register(Projects)
admin.site.register(ResumeModel)