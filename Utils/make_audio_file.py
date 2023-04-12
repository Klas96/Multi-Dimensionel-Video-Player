from moviepy.editor import VideoFileClip

def make_audio_file(video_file, audio_file):
    # Set up the video file path
    video_file = 'videos/file'

    # Set up the audio file path
    audio_file = 'videos/file'

    # Extract the audio track from the video file
    clip = VideoFileClip(video_file)
    clip.audio.write_audiofile(audio_file)
    clip.close()