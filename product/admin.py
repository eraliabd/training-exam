from django.contrib import admin

from .models import Course, Lesson, ViewLesson

admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(ViewLesson)

