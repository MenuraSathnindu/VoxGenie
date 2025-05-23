from gtts import gTTS  # Google's Text-to-Speech library
import os
import time

# Function to convert text to spoken output
def speak(text):
    print(f"🤖 VoxGenie: {text}")
    tts = gTTS(text=text, lang='en')  # Convert text to speech in English
    filename = "response.mp3"  # Temporary file to save audio
    tts.save(filename)  # Save audio to file
    os.system(f"start {filename}")  # Play the file using system's default player
    time.sleep(2)  # Wait for 2 seconds to let the file play
    os.remove(filename)  # Delete the file afterward
