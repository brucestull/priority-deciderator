from django.contrib import admin

from .models import Task, SubTask, ImportantConcept


admin.site.register(Task)
admin.site.register(SubTask)
admin.site.register(ImportantConcept)
