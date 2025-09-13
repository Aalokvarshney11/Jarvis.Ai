import webbrowser
import pyttsx3
import random
import speech_recognition as sr

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 110)   
engine.setProperty('volume', 1.0) 
engine.setProperty('voice', voices[1].id)   

def speak(text):
    engine.say(text)
    engine.runAndWait()


chats = {
    "how r u": ["I am fine, bro!", "All good! Ready to help.", "Great! What about you?"],
    "kese ho": ["Main thik hoon bhai.", "Mast chal raha hai!", "Sab badiya hai."],
    "hello": ["Hello! Kaise ho?", "Hi! Jarvis ready hai.", "Namaste bhai!"],
    "bye": ["Goodbye! Take care.", "Bye bro, milte hai.", "See you soon!"],
    "who are you": ["Main Jarvis hoon, tera apna AI dost.", "Main ek assistant hoon jo teri madat ke liye bana hu."],
    "your name": ["Mera naam Jarvis hai.", "Log mujhe Jarvis bulate hain."],
    "what can you do": ["Main teri madat kar sakta hoon, Google khol sakta hoon, YouTube chala sakta hoon, aur tere sawalon ka jawab de sakta hoon!"]
}


fallback_replies = [
    "Bhai, ye sawal thoda tough hai mere liye.",
    "Mujhe ye samajh nahi aaya, fir se puchhoge?",
    "Interesting! Lekin iska jawab abhi mere pass nahi hai.",
    "Bhai, isme thodi madad chahiye mujhe bhi.",
    "Good question! Lekin mujhe training ki zarurat hai iske liye."
]


def chatbot(data: str) -> str:
    """User input leke reply return aur bol kar dega"""
    reply = random.choice(fallback_replies)
    data = data.lower().strip()
    for key in chats:
        if key in data:  
            reply = random.choice(chats[key])
            speak(reply)
            engine.runAndWait()
            return reply
    
    speak(reply)
    engine.runAndWait()
    return reply
