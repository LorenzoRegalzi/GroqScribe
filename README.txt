"""
# Audio to Text Transcription using Groq and AssemblyAI APIs

## Description
This project automatically extracts text from MP4 audio files using the Groq transcription API or the AssemblyAI API. The output is a text file that contains the complete transcription of the speech present in the audio. The program manages environment variables using a `.env` file to keep your API keys secure.

## Requirements
- Python 3.7 or higher
- Groq API key (required to use the Groq transcription APIs)
- AssemblyAI API key (required to use the AssemblyAI transcription APIs)
- Python Libraries: `groq`, `python-dotenv`, `moviepy`, `assemblyai`

## Installation

### 1. Clone the Repository
If you are cloning the repository from GitHub, use the following command:

```bash
git clone https://github.com/LorenzoRegalzi/GroqScribe.git
cd GroqScribe
