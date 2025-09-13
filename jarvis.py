import speech_recognition as sr
import webbrowser
import pyttsx3
import music
import chatbot

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 130)   # Default ~200, kam karega to clear lagega
engine.setProperty('volume', 1.0) # 0.0 se 1.0 tak
engine.setProperty('voice', voices[0].id)   # Female (usually index 1 hota hai)


def speak(text):
    engine.say(text)
    engine.runAndWait()

speak(" ready to pair with jarvis")
print("🎤 ready to pair with jarvis")

def  processcommand(text):
    if "open google" in text.lower():
        speak("opening google")
        engine.runAndWait()

        webbrowser.open("https://google.com")

    elif "open facebook"in text.lower():
        speak("opening facebook")
        engine.runAndWait()

        webbrowser.open("https://m.facebook.com")

    elif "open github" in text.lower():
        speak("opening github")
        engine.runAndWait()

        webbrowser.open("https://github.com/Aalokvarshney11")


    elif "open youtube" in text.lower():
        speak("opening you tube")
        engine.runAndWait()

        webbrowser.open("https://www.youtube.com/")
       

    elif  text.lower().startswith("play"):
         song  = text.lower()
         link = music.processsong(song)
         if link :
             webbrowser.open(link)
         else:
             print(" ❌ invalid ❌ ")

    elif "bye" in text:
        reply = chatbot.chatbot(text)  # chatbot bye ka reply dega
        print("Jarvis:", reply)
        # yaha extra line: aur koi madat chahiye
        print("Jarvis: Bhai, aur koi madat chahiye?")
        chatbot.speak("Bhai, aur koi madat chahiye?")

    elif text:   # agar koi aur input ho to chatbot handle kare
        reply = chatbot.chatbot(text)
        print("Jarvis:", reply)

            
    # else:
    #     speak("this Command not supported in my system.")
    #     engine.runAndWait()
    #     print("❌ this Command not supported in my system.  ")
             
 
      

while True:
    r = sr.Recognizer()
    r.energy_threshold = 300
    r.pause_threshold = 0.8

    try:
        with sr.Microphone() as source:
            # print("Adjusting for background noise...")
            r.adjust_for_ambient_noise(source, duration=1)
            print(" 🔊 Listening...")
            audio = r.listen(source, timeout=5, phrase_time_limit=5)

        word = r.recognize_google(audio)
        print("You said: ", word)


        if word.lower() == "jarvis":
            engine.say("yaa")
            print(" 🔑  Jarvis activated! 🔑 ")

            with sr.Microphone() as source:
                
                print("jarvis active, 🗣️ waiting for command... 🗣️")
                try:
                 audio = r.listen(source, timeout=5, phrase_time_limit=5)
                 command = r.recognize_google(audio)
                 print("Command: ", command)
                 processcommand(command)
                except sr.WaitTimeoutError:
                    # agar 4 sec me kuch nahi bola
                    engine.say("Bhai bol kuch")
                    engine.runAndWait()
                    print("⚠️ Timeout: Bhai bol kuch")

    except sr.UnknownValueError:
        print(" ⚠️ Sorry, I could not understand.")
    except sr.RequestError as e:
        print(" ⚠️ Could not request results; {0}".format(e))
    except sr.WaitTimeoutError:
        # Wake word ke time agar kuch nahi bola
        engine.say("Bhai bol kuch")
        engine.runAndWait()
        print("⚠️ Timeout: Bhai bol kuch")