import re
import ffmpeg

def reformat_time(time_str):
    # Split the time string into hours, minutes, seconds, and microseconds
    h, m, s_ms = time_str.split(':')
    s, ms = s_ms.split(',')

    # Calculate the total time in seconds
    total_seconds = int(h) * 3600 + int(m) * 60 + int(s) + int(ms) / 1000

    # Return the time in seconds as a float
    return round(total_seconds, 3)

def mute_voices2(audio, subtitles, output_file = 'output_audio.mp3'):
    """
    Takes in an audio stream and a string with subtitles
    and mutes the audio stream att the places for the subtitle.
    """

    # Extract time codes using regular expressions
    time_codes = re.findall(r'\d{2}:\d{2}:\d{2},\d{3}', subtitles)

    # Convert time codes to tuples of start and end times
    time_points = [(time_codes[i], time_codes[i+1]) for i in range(0, len(time_codes), 2)]

    # Print the time points


    for tpnt in time_points:

        # Define the time points to mute (in seconds)
        start_time = reformat_time(tpnt[0])
        end_time = reformat_time(tpnt[1])

        print(start_time)
        print(end_time)

        # Define the ffmpeg command
        ffmpeg_cmd = (
            ffmpeg
            .input(audio)
            .filter('volume', enable=f'between(t,{start_time},{end_time})', volume='0dB')
            .output(output_file, format='mp3')#, acodec='copy'
        )
        # Run the ffmpeg command

        ffmpeg_cmd.run(overwrite_output=True)


def mute_voices(audio, subtitles, output_file='output_audio.mp3'):
    """
    Takes in an audio stream and a string with subtitles
    and mutes the audio stream at the places for the subtitle.
    """

    # Extract time codes using regular expressions
    time_codes = re.findall(r'\d{2}:\d{2}:\d{2},\d{3}', subtitles)

    # Convert time codes to tuples of start and end times
    time_points = [(reformat_time(time_codes[i]), reformat_time(time_codes[i+1])) for i in range(0, len(time_codes), 2)]

    # Define the ffmpeg command
    ffmpeg_cmd = ffmpeg.input(audio)

    # Build the filtergraph with multiple volume filters
    filter_graph = ''
    for i, tpnt in enumerate(time_points):
        start_time, end_time = tpnt
        filter_graph += f"volume=enable='between(t,{start_time},{end_time})':volume=0dB"
        if i < len(time_points) - 1:
            #No comma at end
            filter_graph += ', '

    filter_graph = f'[0:a]{filter_graph}[a]'

    # Add the filtergraph to the ffmpeg command
    ffmpeg_cmd = ffmpeg_cmd.filter(filter_graph)
    breakpoint()
    # Set the output format and run the command
    ffmpeg_cmd.output(output_file, format='mp3').run(overwrite_output=True)



if __name__ == '__main__':

    #Extract Audio Stream

    #Make Subtitles
    with open('Subtitles/squere.str', 'r') as file:
        subtitles = file.read()

    audio = 'Audios/The.Square.mp3'
    mute_voices(audio, subtitles)