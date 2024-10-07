import os
from groq import Groq
from dotenv import load_dotenv


load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
if api_key is None:
    raise ValueError("GROQ_API_KEY isn't set on .env.")

client = Groq(
    api_key=api_key,
)


filename = os.path.dirname(__file__) + "sample_audio.mp3" # Replace with your audio file!


with open(filename, "rb") as file:

    transcription = client.audio.transcriptions.create(

      file=(filename, file.read()), # Required audio file

      model="distil-whisper-large-v3-en", # Required model to use for transcription

      prompt="Specify context or spelling",  # Optional

      response_format="json",  # Optional

      language="en",  # Optional

      temperature=0.0  # Optional

    )

    formatted_text = transcription.text.replace(". ", ".\n")

    output_file = "output.txt"
    with open(output_file, "w") as text_file:
        text_file.write(formatted_text)
        print(f"Trnascript saved in {output_file}")