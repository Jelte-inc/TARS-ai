import speech_recognition as sr
 
# Maak een recognizer object
recognizer = sr.Recognizer()
 
# Gebruik de microfoon als audio bron
mic = sr.Microphone()
 
# Stel de minimale energie drempel in voor achtergrondgeluid
recognizer.energy_threshold = 300
 
# Zet dynamische aanpassing van de drempel aan
recognizer.dynamic_energy_threshold = True
 
def listen_and_transcribe():
    print("Luistert... Zeg iets in het Engels!")
    with mic as source:
        # Pas de microfoon aan achtergrondgeluid aan
        recognizer.adjust_for_ambient_noise(source, duration=1)
        while True:
            try:
                # Luister naar audio
                audio = recognizer.listen(source, phrase_time_limit=5)

                # Gebruik Google Speech Recognition om de audio om te zetten naar tekst
                text = recognizer.recognize_google(audio, language="en-US")
                print("Je zei: ", text)
            except sr.WaitTimeoutError:
                # Als er geen spraak wordt gedetecteerd binnen de timeout
                print("Geen spraak gedetecteerd, blijf luisteren...")
                continue
            except sr.UnknownValueError:
                # Als de spraak niet verstaanbaar is
                print("Kon je niet verstaan, probeer opnieuw.")
                continue
            except sr.RequestError as e:
                # Als er een probleem is met de Google API
                print(f"Fout bij het verbinden met de Google API: {e}")
                break
            except KeyboardInterrupt:
                # Stop het programma met Ctrl+C
                print("\nProgramma gestopt.")
                break
 
if __name__ == "__main__":
    listen_and_transcribe()