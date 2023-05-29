import re
import ffmpeg
import pyttsx3
import time

def text_to_audio(subtitles):
    """
    Takes a subtitle string and uses text-to-speech API to construct an audio file with speech at the specific time points and silence in between.
    """
    # Initialize the TTS engine
    engine = pyttsx3.init()

    # Set the audio file format (e.g., "wav", "mp3")
    audio_format = "wav"

    # Split the subtitle string into individual time points and speech texts
    subtitle_parts = subtitles.split("\n")
    time_points = [part.split(":")[0] for part in subtitle_parts]
    speech_texts = [part.split(":")[1] for part in subtitle_parts]

    # Iterate over the subtitle parts and convert them to audio
    for i in range(len(subtitle_parts)):
        # Extract the time point and speech text
        time_point = time_points[i]
        speech_text = speech_texts[i]

        # Convert the speech text to audio
        engine.save_to_file(speech_text, f"audio_{i}.{audio_format}")

        # Wait until the specified time point to continue
        current_time = time.strftime("%H:%M", time.gmtime())
        while current_time < time_point:
            current_time = time.strftime("%H:%M", time.gmtime())
            time.sleep(1)

    # Run the TTS engine's event loop and wait for all the audio files to be generated
    engine.runAndWait()



if __name__ == '__main__':

    video_path = 'videos/The.Square.2017.1080p.BrRip.6CH.sample.mkv'

    import io

    audio_stream = (ffmpeg.input(video_path).audio.output('pipe:', format='mp3').run(capture_stdout=True))

    audio_stream = io.BytesIO(audio_stream[0])

    with open('Subtitles/squere.str', 'r') as file:
        subtitles = file.read()

    text_to_audio(audio_stream, subtitles)