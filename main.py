import cv2


def get_video_duration_seconds(video_path):
    cap = cv2.VideoCapture(video_path)

    # Get the frames per second and total frames count
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Calculate duration (in seconds)
    duration_seconds = frame_count / fps
    print("Sec:", duration_seconds)

    return duration_seconds

print(get_video_duration_seconds('/media/erali/Новый том/my projects/training-exam/media/lesson/video.mp4'))


from moviepy.editor import VideoFileClip

def get_video_duration(file_path):
    try:
        video = VideoFileClip(file_path)
        duration = video.duration
        video.close()
        print("dur:", duration)
        return duration
    except Exception as e:
        # Handle exceptions, e.g., file not found, unsupported file type, etc.
        print(f"Error: {e}")
        return None

print(get_video_duration('/media/erali/Новый том/my projects/training-exam/media/lesson/video.mp4'))


def get_video_duration_seconds(self):
    file_path = os.path.join(settings.BASE_DIR, 'media/lesson/', self.video.name)
    cap = cv2.VideoCapture(file_path)
    print(cap)

    # Get the frames per second and total frames count
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(fps, frame_count)
    # Calculate duration (in seconds)
    duration_seconds = frame_count / (fps + 1)
    print("Sec:", duration_seconds)

    # self.view_time = duration_seconds
    return duration_seconds


def get_video_duration(self):
    try:
        file_path = os.path.join(settings.BASE_DIR, 'media/lesson/', self.video.name)
        video = VideoFileClip(file_path)
        print(f"video_path:{video}")
        duration = video.duration
        video.close()
        print("dur:", duration)
        self.view_time = duration
        return duration
    except Exception as e:
        # Handle exceptions, e.g., file not found, unsupported file type, etc.
        print(f"Error: {e}")
        return None

