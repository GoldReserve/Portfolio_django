from django.contrib import admin
from index.models import *

@admin.register(Projects)
class Projects(admin.ModelAdmin):
    pass
