import os
from groq import Groq
from dotenv import load_dotenv
from moviepy.editor import VideoFileClip

mp4_file_name = "FileName.mp4"
mp3_file_name = "sample_audio.mp3"

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
if api_key is None:
    raise ValueError("GROQ_API_KEY is not set in the .env file.")

# Function to convert an MP4 video to an MP3 audio file
def convert_mp4_to_mp3(mp4_path, mp3_path):
    # Load the video file
    video_clip = VideoFileClip(mp4_path)

    # Extract the audio track and save it as an MP3 file
    video_clip.audio.write_audiofile(mp3_path)

    # Close the video clip to free resources
    video_clip.close()

# Function to add a newline every specified number of characters
def add_newline_every_50_chars(text, max_length=100):
    words = text.split()  # Split the text into words
    lines = []
    current_line = ""
    
    for word in words:
        if len(current_line) + len(word) + 1 > max_length:
            # If the current line exceeds the max length, add it to the list and start a new line
            lines.append(current_line)
            current_line = word
        else:
            # Otherwise, add the word to the current line
            if current_line:  # Add a space if the line is not empty
                current_line += " "
            current_line += word
    
    # Add the last line
    lines.append(current_line)
    return "\n".join(lines)

# Initialize the Groq client with the API key
client = Groq(api_key=api_key)

# Specify the audio file path
filename = os.path.join(os.path.dirname(__file__), mp3_file_name)  # Replace with your audio file path

# Convert the MP4 video to MP3 format
convert_mp4_to_mp3(mp4_file_name, mp3_file_name)
print("File successfully converted")

# Open the converted audio file and send it for transcription
with open(filename, "rb") as file:
    transcription = client.audio.transcriptions.create(
        file=(filename, file.read()),  # Required audio file
        model="whisper-large-v3",  # Model for transcription
        prompt="Specify context or spelling",  # Optional context prompt
        response_format="json",  # Response format
        language="en",  # Language of the audio
        temperature=0.0  # Decoding temperature
    )

    # Format the transcribed text
    formatted_text = transcription.text.replace(". ", ".\n")
    formatted_text = add_newline_every_50_chars(formatted_text)

    # Save the formatted text to a file
    output_file = mp4FileName + ".txt"
    with open(output_file, "w") as text_file:
        text_file.write(formatted_text)
        print(f"Transcript saved in {output_file}")
