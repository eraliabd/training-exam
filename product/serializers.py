from rest_framework import serializers

from .models import Course, Lesson, ViewLesson


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'user', 'title', 'content', 'is_permission', 'created_at')


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('id', 'status', 'view_time')
