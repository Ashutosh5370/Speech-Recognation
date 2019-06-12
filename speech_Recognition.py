import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak something")

    audio = r.listen(source)

    Text = r.recognize_google(audio)
    

    print(Text)
