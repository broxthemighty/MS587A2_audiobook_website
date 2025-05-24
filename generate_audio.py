# ===========================================
# Local Audio Generator for eBooks
# Purpose: Use pyttsx3 to convert .txt books to audio files
# Output: .mp3 audio saved to 'static/audio/'
# ===========================================

import os
import pyttsx3
import logging

# Configure logging for status messages and errors
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

# Define source and target directories
EBOOK_DIR = "ebooks"
AUDIO_DIR = os.path.join("static", "audio")
os.makedirs(AUDIO_DIR, exist_ok=True)  # Ensure output directory exists

# Initialize the text-to-speech engine (offline, system-based)
engine = pyttsx3.init()

def generate_audio_from_text(filename: str):
    """
    Converts a single .txt file into an .mp3 using pyttsx3.
    Skips any file that doesn't end with .txt.
    """
    if not filename.endswith(".txt"):
        return

    base_name = filename.replace(".txt", "")
    audio_filename = f"{base_name}.mp3"
    audio_path = os.path.join(AUDIO_DIR, audio_filename)
    ebook_path = os.path.join(EBOOK_DIR, filename)

    try:
        # Read text content from the eBook
        with open(ebook_path, "r", encoding="utf-8") as file:
            text = file.read()

        # Generate and save audio from the text
        logging.info(f"Generating audio for: {filename}")
        engine.save_to_file(text, audio_path)
        engine.runAndWait()
        logging.info(f"Saved audio to: {audio_path}")

    except Exception as e:
        logging.error(f"Error processing {filename}: {e}")

def main():
    """
    Iterates over all files in the eBook directory and
    processes them into audio where applicable.
    """
    for file in os.listdir(EBOOK_DIR):
        generate_audio_from_text(file)

if __name__ == "__main__":
    main()
