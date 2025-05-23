import speech_recognition as sr  # Import the SpeechRecognition library

# Function to listen to the user's voice
def listen_command():
    recognizer = sr.Recognizer()  # Create a recognizer object

    with sr.Microphone() as source:  # Use the microphone as the audio source
        print("🎤 Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
        audio = recognizer.listen(source)  # Record the user's voice

    try:
        # Try converting speech to text using Google Web Speech API
        command = recognizer.recognize_google(audio)
        print(f"🗣️ You said: {command}")
        return command

    # Error if speech is unintelligible
    except sr.UnknownValueError:
        return "Sorry, I didn't understand that."

    # Error if the recognition service fails
    except sr.RequestError:
        return "Sorry, I can't connect to the recognition service."
