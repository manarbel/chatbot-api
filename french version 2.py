import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
from ecapture import ecapture as ec
import wolframalpha
import json
import requests


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')

class person:
    name = ''

    def setName(self, name):
        self.name = name

class asis:
    name = ''

    def setName(self, name):
        self.name = name

person_obj = person()
asis_obj = asis()
asis_obj.name = 'Lucy'
person_obj.name = ""

def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Bonjour")
        print("Bonjour")
    elif hour>=12 and hour<18:
        speak("Bon après-midi")
        print("Bon après-midi")
    else:
        speak("Bonsoir")
        print("Bonsoir")


def record_audio(ask=""):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        if ask:
            speak(ask)
        audio = r.listen(source)
        try:
            voice_data = r.recognize_google(audio, language='fr')
            print(f"vous dites:{voice_data}\n")

        except Exception as e:
            speak("Pardon, pouvez-vous répéter")
            voice_data = record_audio("je vous écoute")
            return voice_data
        return voice_data


wishMe()
time.sleep(1)
speak("Bienvenus à l'université Mohamed 6 polytechnique, je suis votre robot d'assistance")
print("Bienvenus à l'université Mohamed 6 polytechnique, je suis votre robot d'assistance")



def respond(voice_data):
    # 1: quit
    if there_exists(["au revoir", "ok bye", "stop", "bye"]):
        os.system("taskkill /im opera.exe /f")
        speak("Votre robot assistant s'arrête, au revoir")
        print("Votre robot assistant s'arrête, au revoir")
        exit()

     # 2: name
    if there_exists(["comment appelez-vous", "quel est votre nom", "nom"]):

        if person_obj.name:
            speak(f"Je m'appelle {asis_obj.name}, {person_obj.name}")  # gets users name from voice input
        else:
            speak(f"Je m'appelle {asis_obj.name}. et vous?")  # incase you haven't provided your name.

    if there_exists(["je m'appelle", "je suis"]):
        person_name = voice_data.split("suis")[-1].strip() or voice_data.split("appelle")[-1].strip()
        speak("Enchanté" + person_name)
        person_obj.setName(person_name)  # remember name in person object

    if there_exists(["qui suis-je", "comment je m'appelle"]):
        speak("vous êtes " + person_obj.name)

    # 3: greeting
    if there_exists(["comment allez-vous"]):
        speak("Je vais très bien, Merci" + person_obj.name)

    # 4: Elearning
    if there_exists(['elearning', 'ouvrir elearning']):
        webbrowser.open_new_tab("https://elearning.emines.um6p.ma/")
        speak("Vous avez l'accés à Elearning")
        time.sleep(3)

    # 5: Oasis
    if there_exists(['oasis', 'ouvrir oasis']):
        webbrowser.open_new_tab("https://emines.oasis.aouka.org/")
        speak("Vous avez l'accés à Oasis")
        time.sleep(3)

    # 6: Outlook
    if there_exists(['outlook', 'ouvrir outlook']):
        webbrowser.open_new_tab("https://www.office.com/")
        speak("Vous avez l'accés à Outlook")
        time.sleep(3)

    # 7: Emines
    if there_exists(['voir site emines', 'émine']):
        webbrowser.open_new_tab("https://www.emines-ingenieur.org/")
        speak("Vous avez l'accés au site d'EMINES")
        time.sleep(3)

    # 8: visite UM6P
    if there_exists(["je veux visiter virtuellement l'université"]):
        webbrowser.open_new_tab("https://alpharepgroup.com/um6p_univer/models.php")
        speak("Bienvenue à la visite virtuelle de um6p ")
        time.sleep(3)

    # 9: time
    if there_exists(['quelle heure est-il', 'heure']):
        strTime = datetime.datetime.now().strftime("%H""heures""%M")
        speak(f"Il est {strTime}")

    # 10: presentation
    if there_exists(['présente-toi']):
        speak("Je suis votre robot d'assistance" " Réalisé par les étudiants du quatrième année d'EMINE"
              "Je suis un projet mécatronique pour rendre service aux visiteurs de l'université mohamed 6 polytechnique")
        time.sleep(3)

    # 11 google
    if there_exists(['google', 'ouvrir google']):
        webbrowser.open_new_tab("https://www.google.com")
        speak("Vous avez l'accés à Google")
        time.sleep(3)

    # 12 localisation google maps
    if there_exists(["où suis-je exactement", "où suis-je", "où je suis ", "où je suis exactement"]):
        webbrowser.open_new_tab("https://www.google.com/maps/search/Where+am+I+?/")
        speak("Selon Google maps, vous devez être quelque part près d'ici")
        time.sleep(3)

    # 13 météo
    if there_exists(["météo"]):
        search_term = voice_data.split("for")[-1]
        webbrowser.open_new_tab(
            "https://www.google.com/search?sxsrf=ACYBGNSQwMLDByBwdVFIUCbQqya-ET7AAA%3A1578847393212&ei=oUwbXtbXDN-C4-EP-5u82AE&q=weather&oq=weather&gs_l=psy-ab.3..35i39i285i70i256j0i67l4j0i131i67j0i131j0i67l2j0.1630.4591..5475...1.2..2.322.1659.9j5j0j1......0....1..gws-wiz.....10..0i71j35i39j35i362i39._5eSPD47bv8&ved=0ahUKEwiWrJvwwP7mAhVfwTgGHfsNDxsQ4dUDCAs&uact=5")
        speak("Voici ce que j'ai trouvé pour la météo sur Google")
        time.sleep(3)


#time.sleep(1)


speak("Comment puis-je vous aider?")
print("Comment puis-je vous aider?")
while True:
    voice_data = record_audio("je vous écoute")
    respond(voice_data)
    time.sleep(10)
    if there_exists(["j'ai besoin de votre aide"]):
        voice_data = record_audio("je vous écoute")
        print(voice_data, ...)
        respond(voice_data)
    else:
        time.sleep(5)
        voice_data = record_audio("Avez-vous besoin de mon aide")
        #voice_data = record_audio("je vous écoute")
        print(voice_data, ...)
        if there_exists(['oui']):
            os.system("taskkill /im opera.exe /f")
            voice_data = record_audio("je vous écoute")
            print(voice_data, ...)
            respond(voice_data)
            continue
        if there_exists(['non','merci']):
            os.system("taskkill /im opera.exe /f")
            speak("Votre robot assistant s'arrête, au revoir")
            print("Votre robot assistant s'arrête, au revoir")
            break
