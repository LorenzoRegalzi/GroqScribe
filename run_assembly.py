import os
from dotenv import load_dotenv
import assemblyai as aai
from moviepy.editor import VideoFileClip

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv("ASSEMBLY_AI_KEY")
if api_key is None:
    raise ValueError("ASSEMBLY_AI_KEY is not set in the .env file.")

# Set the AssemblyAI API key
aai.settings.api_key = api_key

# File names for the input video and output audio/transcription
mp4_file_name = "FileName.mp4"
mp3_file_name = "sample_audio.mp3"

# Function to convert an MP4 video to an MP3 audio file
def convert_mp4_to_mp3(mp4_path, mp3_path):
    # Load the video file
    video_clip = VideoFileClip(mp4_path)

    # Extract the audio track and save it as an MP3 file
    video_clip.audio.write_audiofile(mp3_path)

    # Close the video clip to free resources
    video_clip.close()

# Function to upload a local file to AssemblyAI
def upload_file(file_path):
    transcriber = aai.Transcriber()
    upload_response = transcriber.upload_file(file_path)
    return upload_response

# Convert the MP4 video to MP3 format
convert_mp4_to_mp3(mp4_file_name, mp3_file_name)
print("Audio extracted and saved as MP3.")

# Construct the full path for the MP3 file
file_path = os.path.join(os.path.dirname(__file__), mp3_file_name)

# Upload the MP3 file to AssemblyAI and get the URL
file_url = upload_file(file_path)
print("File uploaded successfully to AssemblyAI.")

# Transcribe the uploaded audio file
transcriber = aai.Transcriber()
transcript = transcriber.transcribe(file_url)

# Check the transcription status and save the result
if transcript.status == aai.TranscriptStatus.error:
    print(f"Error during transcription: {transcript.error}")
else:
    output_file = f"{mp4_file_name}.txt"
    with open(output_file, "w") as text_file:
        text_file.write(transcript.text)
        print(f"Transcript saved in {output_file}")
