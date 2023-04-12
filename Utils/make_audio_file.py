import ffmpeg

def extract_audio(input_file, output_file):
    # Define the ffmpeg command using the fluent API
    (
        ffmpeg
        .input(input_file)
        .audio
        .output(output_file)
        .run()
    )

if __name__ == '__main__':
    video_path = "videos/The.Square.2017.1080p.BrRip.6CH.sample.mkv"
    audio_path = "Audios/The.Square.mp3"
    extract_audio(video_path, audio_path)