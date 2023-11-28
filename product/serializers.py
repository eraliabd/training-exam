from rest_framework import serializers

from .models import Course, Lesson, ViewLesson


class CourseStatisticsSerializer(serializers.ModelSerializer):
    lesson_count = serializers.IntegerField()
    total_time_watched = serializers.IntegerField()
    student_count = serializers.IntegerField()
    percentage_of_course_purchases = serializers.IntegerField()

    class Meta:
        model = Course
        fields = ['id', 'user', 'title', 'created_at', 'lesson_count', 'total_time_watched', 'student_count',
                  'percentage_of_course_purchases']


class ViewLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = ViewLesson
        fields = ['status', 'seen_duration']


class LessonSerializer(serializers.ModelSerializer):
    status = ViewLessonSerializer(source='view_lesson', many=True)

    class Meta:
        model = Lesson
        fields = ['id', 'duration', 'status']


class CourseSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True)

    class Meta:
        model = Course
        fields = ['id', 'user', 'title', 'lessons']


# detail
class LessonDetailSerializer(serializers.ModelSerializer):
    status = ViewLessonSerializer(source='view_lesson', many=True)

    class Meta:
        model = Lesson
        fields = ['id', 'duration', 'updated_at', 'status']


class CourseDetailSerializer(serializers.ModelSerializer):
    lessons = LessonDetailSerializer(many=True)

    class Meta:
        model = Course
        fields = ['id', 'user', 'title', 'lessons']
