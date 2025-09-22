import speech_recognition as sr
from alsa_quiet import disable_alsa_errors
disable_alsa_errors()
 
def speech_listener():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    recognizer.energy_threshold = 300
    recognizer.dynamic_energy_threshold = True

    print("Listening...")
    with mic as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        while True:
            try:
                audio = recognizer.listen(source, phrase_time_limit=5)
                text = recognizer.recognize_google(audio, language="en-US")
                print("Je zei: ", text)
                return text
            except sr.WaitTimeoutError:
                print("No speech detected")
                continue
            except sr.UnknownValueError:
                print("Could not undstand speech, try talking again.")
                continue
            except sr.RequestError as e:
                print(f"Error while connecting to the Google API: {e}")
                break
            except KeyboardInterrupt:
                print("\Program stopped.")
                break