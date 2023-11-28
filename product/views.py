from django.utils import timezone
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from django.db.models import Count, Sum, F, FloatField, ExpressionWrapper

from .models import Course, Lesson, ViewLesson, ViewLessonChoice

from .serializers import CourseSerializer, ViewLessonSerializer, LessonSerializer, CourseDetailSerializer, \
    CourseStatisticsSerializer

from django.contrib.auth import get_user_model

User = get_user_model()


class LessonDetailView(RetrieveAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        Lesson.objects.filter(course__user=user, pk=self.kwargs['pk']).update(updated_at=timezone.now())
        lesson = Lesson.objects.filter(course__user=user, pk=self.kwargs['pk'])

        return lesson


class CourseListAPIView(ListAPIView):
    serializer_class = CourseSerializer

    def get_queryset(self):
        user = self.request.user
        courses = Course.objects.filter(user=user)
        return courses


class CourseDetailView(RetrieveAPIView):
    serializer_class = CourseDetailSerializer

    def get_queryset(self):
        user = self.request.user
        Course.objects.filter(user=user, pk=self.kwargs['pk']).update(entries_count=F('entries_count')+1)
        course = Course.objects.filter(user=user, pk=self.kwargs['pk'])
        return course


class CourseStatisticsListAPIView(ListAPIView):
    serializer_class = CourseStatisticsSerializer

    def get_queryset(self):
        statistics = Course.objects.annotate(
            lesson_count=Count('lessons__view_lesson'),
            total_time_watched=Sum('lessons__view_lesson__seen_duration'),
            student_count=Count('lessons__view_lesson__user', distinct=True),
            percentage_of_course_purchases=
            (Sum('entries_count') / User.objects.all().count())
        )

        return statistics


course_statistics = CourseStatisticsListAPIView.as_view()
