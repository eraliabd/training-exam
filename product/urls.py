from django.urls import path

from .views import LessonDetailView, CourseListAPIView, CourseDetailView

urlpatterns = [
    path('lesson/<int:pk>/', LessonDetailView.as_view(), name='lesson-detail'),
    path('course/', CourseListAPIView.as_view(), name='course'),
    path('course/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
]
