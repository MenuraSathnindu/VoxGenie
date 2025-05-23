from flask import Flask, render_template, jsonify
from backend.voice_engine import listen_command
from backend.assistant_core import speak
from datetime import datetime

app = Flask(__name__, static_folder="static")   # Create a Flask web server

# Serve the homepage
@app.route('/')
def index():
    return render_template("index.html")

# When '/listen' is called, listen to user, speak response, and log it
@app.route('/listen')
def listen():
    command = listen_command()  # Get the user's voice input
    response = f"You said: {command}"  # Format response
    speak(response)  # Speak it aloud

    # Log the conversation in a text file with a timestamp
    with open("logs/chat_history.txt", "a") as log:
        log.write(f"{datetime.now()} - {response}\n")

    # Send result back to the browser as JSON
    return jsonify({"command": command})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
