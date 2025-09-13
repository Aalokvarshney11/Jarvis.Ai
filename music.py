import webbrowser
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 150)   # Default ~200, kam karega to clear lagega
engine.setProperty('volume', 1.0) # 0.0 se 1.0 tak
engine.setProperty('voice', voices[1].id)   # Female (usually index 1 hota hai)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processsong(song):
    music = {

    "play dance like" : "https://youtu.be/vXuO3Yg6yKE?si=xEjWpxo1L5bc_naw" ,
    "play bhar do" : "https://youtu.be/zk0-f92gg9A?si=6GW1R0QG_2NfcMN6" , 
    "play char kadam" : "https://youtu.be/WKbwopSXLWU?si=hKsWioCSpXCd_BZM"

     }
    song = song.lower().strip()

    if song in music:
        url = music[song]
        speak(f"playing {song}")
        engine.runAndWait()
        return url
        
    else:
        speak("this Command not supported in my system.")
        engine.runAndWait()
        return None
        
    