import re
import ffmpeg


def text_to_audio(audio, subtitles):
    """
    Mute the video at the momment of speach and inert audio overlay
    """
    pass

    #find all time points in the subtitles and give them as tubles [(start, end),....(start,end)]
    #mute video att time points

    #translate strings

    # Extract time codes using regular expressions
    time_codes = re.findall(r'\d{2}:\d{2}:\d{2},\d{3}', subtitles)

    # Convert time codes to tuples of start and end times
    time_points = [(time_codes[i], time_codes[i+1]) for i in range(0, len(time_codes), 2)]

    # Print the time points
    print(time_points)
    for tpnt in time_points:
        #mute the audio

        # Define the input and output file names
        input_file = 'input_audio.mp3'
        output_file = 'output_audio.mp3'

        # Define the time points to mute (in seconds)
        start_time = 10
        end_time = 20

        # Define the ffmpeg command
        ffmpeg_cmd = (
            audio
            .filter('volume', enable=f'between(t,{tpnt[0]},{tpnt[1]})', volume='0dB')
            .output(output_file, format='mp3', acodec='copy')
        )

        # Run the ffmpeg command
        ffmpeg_cmd.run()



if __name__ == '__main__':

    

    with open('Subtitles/squere.str', 'r') as file:
        subtitles = file.read()



    text_to_audio('', subtitles)