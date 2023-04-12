import ffmpeg

def extract_subtitle_stream(video_file_path, output_sub_path):

    # Extract the first subtitle stream from the video file
    input_stream = ffmpeg.input(video_file_path)
    output_stream = ffmpeg.output(input_stream['s:0'], output_sub_path, codec='srt', f='srt')

    # Save the subtitle stream to a separate file
    ffmpeg.run(output_stream, overwrite_output=True)


def extract_subtitle_stream(video_file_path, output_sub_path):

    # Extract the first subtitle stream from the video file
    input_stream = ffmpeg.input(video_file_path)
    output_stream = ffmpeg.output(input_stream['s:0'], output_sub_path, codec='srt', f='srt')

    # Save the subtitle stream to a separate file
    ffmpeg.run(output_stream, overwrite_output=True)


if __name__ == '__main__':
    video_path = 'videos/The.Square.2017.1080p.BrRip.6CH.sample.mkv'
    sub_path = 'Subtitles/squere.str'
    extract_subtitle_stream(video_path, sub_path)