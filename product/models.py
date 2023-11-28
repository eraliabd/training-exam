import cv2
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()

from moviepy.editor import VideoFileClip


class Course(models.Model):
    # relations
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # fields
    title = models.CharField(max_length=255)
    content = models.TextField()
    is_permission = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ViewLessonChoice(models.TextChoices):
    SEEN = "seen"
    NOT_SEEN = "not seen"


class Lesson(models.Model):
    # relations
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    # fields
    title = models.CharField(max_length=255)
    link = models.URLField()
    video = models.FileField(upload_to='lesson/', null=True)
    view_time = models.IntegerField(default=0)

    status = models.CharField(max_length=10, choices=ViewLessonChoice.choices, default=ViewLessonChoice.NOT_SEEN)

    last_seen_time = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_video_duration_seconds(self):
        cap = cv2.VideoCapture(self.link)

        # Get the frames per second and total frames count
        fps = cap.get(cv2.CAP_PROP_FPS)
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

        # Calculate duration (in seconds)
        duration_seconds = frame_count / fps
        print("Sec:", duration_seconds)

        self.view_time = duration_seconds
        return duration_seconds



class ViewLesson(models.Model):
    # relations
    lesson = models.ForeignKey(Course, on_delete=models.CASCADE)
    users = models.ManyToManyField(User)

    # fields
    video_record = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
