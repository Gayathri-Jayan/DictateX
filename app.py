from flask import Flask, request, jsonify
import speech_recognition as sr
import pyttsx3

app = Flask(__name__)

# Enable CORS (Cross-Origin Resource Sharing)
from flask_cors import CORS
CORS(app)

recognizer = sr.Recognizer()
engine = pyttsx3.init()

@app.route("/speech-to-text", methods=["POST"])
def speech_to_text():
    try:
        # Check if audio file is sent
        if "audio" not in request.files:
            return jsonify({"error": "No audio file received"}), 400
        
        audio_file = request.files["audio"]
        
        with sr.AudioFile(audio_file) as source:
            audio_data = recognizer.record(source)
            text = recognizer.recognize_google(audio_data)

        return jsonify({"text": text})

    except sr.UnknownValueError:
        return jsonify({"error": "Speech not recognized"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/text-to-speech", methods=["POST"])
def text_to_speech():
    try:
        data = request.get_json()
        text = data.get("text", "")

        if not text:
            return jsonify({"error": "No text provided"}), 400

        engine.say(text)
        engine.runAndWait()

        return jsonify({"message": "Speech played successfully"})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
