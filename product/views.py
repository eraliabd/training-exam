from django.utils import timezone
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from django.db.models import Count, Sum, F, FloatField, ExpressionWrapper

from .models import Course, Lesson, ViewLesson, ViewLessonChoice

from .serializers import CourseSerializer, ViewLessonSerializer, LessonSerializer, CourseDetailSerializer


class LessonDetailView(RetrieveUpdateDestroyAPIView):
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


class CourseDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = CourseDetailSerializer

    def get_queryset(self):
        user = self.request.user
        course = Course.objects.filter(user=user, pk=self.kwargs['pk'])
        return course
