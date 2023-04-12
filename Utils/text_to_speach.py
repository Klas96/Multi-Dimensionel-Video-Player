import re
import ffmpeg


def text_to_audio(subtitles):
    """
    takes a subtitle string and uses text to speach api to construct an audio file with speach at the specific time points and scielence in between
    """
    pass



if __name__ == '__main__':

    video_path = 'videos/The.Square.2017.1080p.BrRip.6CH.sample.mkv'

    import io

    audio_stream = (ffmpeg.input(video_path).audio.output('pipe:', format='mp3').run(capture_stdout=True))

    audio_stream = io.BytesIO(audio_stream[0])

    with open('Subtitles/squere.str', 'r') as file:
        subtitles = file.read()

    text_to_audio(audio_stream, subtitles)