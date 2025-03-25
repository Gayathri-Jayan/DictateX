import tkinter as tk
import speech_recognition as sr
import pyttsx3

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        status_label.config(text="Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            text_output.insert(tk.END, text)
            status_label.config(text="Speech Recognized!")
        except:
            status_label.config(text="Could not recognize speech.")

def text_to_speech():
    engine = pyttsx3.init()
    text = text_output.get("1.0", tk.END)
    engine.say(text)
    engine.runAndWait()

root = tk.Tk()
root.title("Speech-to-Text & Text-to-Speech")

tk.Button(root, text="Start Listening", command=speech_to_text).pack()
status_label = tk.Label(root, text="")
status_label.pack()

text_output = tk.Text(root, height=5, width=50)
text_output.pack()

tk.Button(root, text="Convert to Speech", command=text_to_speech).pack()

root.mainloop()
