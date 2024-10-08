import os
from groq import Groq
from dotenv import load_dotenv
from moviepy.editor import VideoFileClip

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
if api_key is None:
    raise ValueError("GROQ_API_KEY isn't set on .env.")

client = Groq(
    api_key=api_key,
)






filename = os.path.dirname(__file__) + "sample_audio.mp3" # Replace with your audio file!

def convert_mp4_to_mp3(mp4_path, mp3_path):
    # Carica il video
    video_clip = VideoFileClip(mp4_path)

    # Estrai la traccia audio e salva come file MP3
    video_clip.audio.write_audiofile(mp3_path)

    # Chiudi il video clip per liberare risorse
    video_clip.close()


convert_mp4_to_mp3("video.mp4","sample_audio.mp3")

print(f"File convertito con successo")



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

     # Funzione per aggiungere un a capo ogni 50 caratteri
    def add_newline_every_50_chars(text, max_length=100):
        words = text.split()  # Suddividi il testo in parole
        lines = []
        current_line = ""
        
        for word in words:
            if len(current_line) + len(word) + 1 > max_length:
                # Se la riga corrente supera il limite, aggiungi a lines e inizia una nuova riga
                lines.append(current_line)
                current_line = word
            else:
                # Altrimenti, aggiungi la parola alla riga corrente
                if current_line:  # Se non è vuoto, aggiungi uno spazio
                    current_line += " "
                current_line += word
        
        # Aggiungi l'ultima riga
        lines.append(current_line)
        return "\n".join(lines)

    # Applica la funzione di formattazione al testo trascritto
    formatted_text = add_newline_every_50_chars(formatted_text)

    output_file = "output.txt"
    with open(output_file, "w") as text_file:
        text_file.write(formatted_text)
        print(f"Trnascript saved in {output_file}")


