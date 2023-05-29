from google.cloud import speech_v1

def get_subtitle_from_audio(audio_file = '/path/to/audio/file'):
    # Set up the speech-to-text client
    client = speech_v1.SpeechClient()

    # Set up the SRT subtitle file path
    subtitle_file = '/path/to/subtitle/file.srt'

    # Set up the transcription config
    config = speech_v1.RecognitionConfig(
        encoding=speech_v1.RecognitionConfig.AudioEncoding.LINEAR16,
        language_code='en-US',
        audio_channel_count=2,
    )

    # Read the audio file content
    with open(audio_file, 'rb') as audio_file:
        content = audio_file.read()
        audio = speech_v1.RecognitionAudio(content=content)

    # Perform the transcription
    response = client.recognize(config=config, audio=audio)

    # Function to format the time in the SRT format
    def format_time(milliseconds):
        seconds = int(milliseconds / 1000)
        minutes = int(seconds / 60)
        hours = int(minutes / 60)
        milliseconds = milliseconds % 1000
        seconds = seconds % 60
        minutes = minutes % 60
        return '{:02d}:{:02d}:{:02d},{:03d}'.format(hours, minutes, seconds, milliseconds)


    # Generate the SRT subtitle file
    with open(subtitle_file, 'w') as subtitle_file:
        i = 1
        for result in response.results:
            start_time = int(result.alternatives[0].words[0].start_time.seconds * 1000 + result.alternatives[0].words[0].start_time.nanos / 1000000)
            end_time = int(result.alternatives[0].words[-1].end_time.seconds * 1000 + result.alternatives[0].words[-1].end_time.nanos / 1000000)
            subtitle_file.write('{}\n{} --> {}\n{}\n\n'.format(i, format_time(start_time), format_time(end_time), result.alternatives[0].transcript))
            i += 1


