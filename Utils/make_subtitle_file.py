import ffmpeg

video_file = '/path/to/video/file.mp4'
subtitle_file = '/path/to/subtitle/file.srt'

# Extract the first subtitle stream from the video file
stream = ffmpeg.input(video_file).output('dummy', map='0:s:0').global_args('-c:s', 'srt').compile()

# Save the subtitle stream to a separate file
ffmpeg.run(stream, overwrite_output=True, output_filename=subtitle_file)
