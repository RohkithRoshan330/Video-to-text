from moviepy.editor import VideoFileClip
import speech_recognition as sr

# Load the video file
video_path = r"D:\Nj\Learning\pozentprojects\video.mp4"
audio_path = "audio.wav"

# Extract audio from the video file
video_clip = VideoFileClip(video_path)
audio_clip = video_clip.audio
audio_clip.write_audiofile(audio_path)

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

# Open the audio file
with sr.AudioFile(audio_path) as source:
    audio_text = r.record(source)

# Recognize the speech in the audio
text = r.recognize_google(audio_text, language='en-US')

file_name = "transcription.txt"

with open(file_name, "w") as file:
    # Write to the file
    file.write(text)

# Open the file for editing by the user
import os
os.system(f"start {file_name}")
