import os
import cv2
from moviepy.editor import VideoFileClip

from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.core.files import File

User = get_user_model()


class UserChoice(models.TextChoices):
    AUTHOR = "AUTHOR"
    STUDENT = "STUDENT"


class Course(models.Model):
    # relations
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # fields
    title = models.CharField(max_length=255)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ViewLessonChoice(models.TextChoices):
    SEEN = "seen"
    NOT_SEEN = "not seen"


class Lesson(models.Model):
    # relations
    course = models.ManyToManyField(Course, related_name='lessons')

    # fields
    title = models.CharField(max_length=255)
    video = models.FileField(upload_to='lesson/', null=True)
    duration = models.IntegerField(default=0, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def save(self, *args, **kwargs):
    #     self.view_time = self.get_video_duration()
    #     self.link = self.video.url
    #     return super().save(*args, **kwargs)


class ViewLesson(models.Model):
    # relations
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='view_lesson')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    # fields
    status = models.CharField(
        max_length=10, choices=ViewLessonChoice.choices, default=ViewLessonChoice.NOT_SEEN
    )

    seen_duration = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.seen_duration < self.lesson.duration * 0.8:
            self.status = ViewLessonChoice.NOT_SEEN

        self.status = ViewLessonChoice.SEEN
        return super().save(*args, **kwargs)
