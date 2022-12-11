import speech_recognition as sr


while True:
    r = sr.Recognizer()
    with sr.Microphone() as mic:
        print("[+] Listening...")
        r.adjust_for_ambient_noise(mic, duration=0.2)
        audio = r.listen(mic)

    try:
        print("[+] Recognizing...")
        query = r.recognize_google(audio, language="en-us")
        print(f"user said: {query}\m")
    except Exception as e:
        print("say that again please")
        query = None

    print(query)
