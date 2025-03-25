

import speech_recognition as sr
import pyttsx3

# Initialize the recognizer
r = sr.Recognizer()

def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

while True:
    try:
        with sr.Microphone() as source2:
            print("Listening...")  # Debugging message
            r.adjust_for_ambient_noise(source2, duration=0.5)
            audio2 = r.listen(source2)

            print("Recognizing...")  # Debugging message
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()

            print("Did you say:", MyText)
            SpeakText(MyText)
    
    except sr.RequestError as e:
        print("Could not request results; check your internet connection:", e)

    except sr.UnknownValueError:
        print("Speech Recognition could not understand audio, try speaking clearly.")

    except Exception as e:
        print("An error occurred:", e)
