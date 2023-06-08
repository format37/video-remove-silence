import os

def extract_audio(video_path, audio_output_path):
    command = f"ffmpeg -i {video_path} -vn -acodec pcm_s16le -ar 44100 -ac 2 {audio_output_path}"
    os.system(command)

# Replace 'input.mp4' and 'output.wav' with your file paths
extract_audio('untitled_result.mp4', 'output.wav')
