import datetime
import os
import smtplib
import sys
import webbrowser
import cv2
import pyautogui
import pyjokes
import pyttsx3
import pywhatkit
import requests
import speech_recognition as sr
import wikipedia
import pydictionary as D
from bs4 import BeautifulSoup
from playsound import playsound
from requests import get
import filemovenew
#from id_pass import mail_id, password, sender_mail_id

"""m = mail_id
p = password
s = sender_mail_id"""

Engine = pyttsx3.init('sapi5')
voices = Engine.getProperty('voices')
# print(voices[0].id)
Engine.setProperty('voice', voices[0].id)


def speak(audio):
    Engine.say(audio)
    print(f": {audio} ")
    print("   ")
    Engine.runAndWait()


Engine.setProperty('rate', 180)


def wishme():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good evening!")
    speak("I am dudes please tell me  how may I help you")


def takecommand():
    # it takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 2
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')

        print(f"user said:{query}\n")
    except:
        speak("say that again please...")
        return "none"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()  # to connect  our server to gmail server
    server.starttls()  # to provide security
    server.login(m, p)
    server.sendmail(s, to, content)
    server.close()


def dicti():
    speak("Dictionary Activated")
    speak("tell me the problem!")
    pro = takecommand()
    if "meaning" in pro:
        pro = pro.replace("what is the", "")
        pro = pro.replace("meaning of", "")
        result = D.meaning(pro)
        speak(f"The meaning for{pro} is {result}")
    elif "synonym" in pro:
        pro = pro.replace("what is the", "")
        pro = pro.replace("synonym of", "")
        result = D.synonym(pro)
        speak(f"The synonym for{pro} is {result}")
    elif "antonym" in pro:
        pro = pro.replace("what is the", "")
        pro = pro.replace("antonym of", "")
        result = D.antonym(pro)
        speak(f"The antonym for{pro} is {result}")
    speak("Exit dictionary")


def main():
    global strTime
    wishme()
    while True:
        query = takecommand().lower()

        if "open notepad" in query:
            query.replace("dudes ", "")
            vpath = "C:\\Windows\\System32\\notepad.exe"
            os.startfile(vpath)
        elif "close notepad" in query:
            speak("okay sir,closing notepad")
            os.system("taskkill /f /im notepad.exe")
        elif "open photoshop" in query:
            os.startfile("C:\\Program Files\\Adobe\\Adobe Photoshop 2021\\Photoshop.exe")
        elif "close photoshop" in query:
            os.system("taskkill /f  /im Photoshop.exe")
        elif "open visual studio code" in query:
            os.startfile("C:\\Users\\gautam\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
        elif "close visual studio code" in query:
            os.system("taskkill /f  /im Code.exe")
        elif "open steam app" in query:
            os.startfile("C:\\Program Files (x86)\\Steam\\Steam.exe")
        elif "close steam app" in query:
            os.system("taskkill /f  /im Steam.exe")
        elif "open microsoft word" in query:
            os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE")
        elif "close microsoft word" in query:
            os.system("taskkill /f /im WINWORD.EXE")
        elif "open map" in query:
            webbrowser.open("https:\\www.google.com\\maps\\@28.4076147,77.2949727,11.83z")
        elif "open chrome" in query:
            os.startfile("chrome.exe")
        elif "close chrome" in query:
            os.system("taskkill  /f /im chrome.exe")
        elif "open command prompt" in query:
            os.system("start cmd")
        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow("webcam", img)
                k = cv2.waitKey(50)
                if k == 27:
                    break
            cap.release()
            cv2.destroyAllWindows()
        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your ip address is {ip}")
        elif "set alarm" in query:
            speak("Enter the time!")
            time = input(":Enter the time:")
            while True:
                Time_Ac = datetime.datetime.now()
                now = Time_Ac.strftime("%H:%M:%S")
                if now == time:
                    speak("Time to wake up sir!")
                    playsound("wakeup.mp3")
                    speak("Alarm closed")
                elif now > time:
                    break

        elif "tell me a joke" in query:
            joke = pyjokes.get_jokes(language="en", category="all")
            speak(joke)
        elif "wikipedia" in query:
            speak("searching wikipedia")
            query = query.replace("wikipedia", " ")
            Results = wikipedia.summary(query, sentences=4)
            speak("According to wikipedia")
            speak(Results)
        elif "youtube search" in query:
            speak("ok sir,this is what i found for your search")
            query = query.replace("youtube search", "")
            web = "https://www.youtube.com/results?search_query=" + query
            webbrowser.open(web)

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "open facebook" in query:
            webbrowser.open("https://www.facebook.com/")
        elif "open instagram" in query:
            webbrowser.open("www.instagram.com")
        elif "google search" in query:
            speak("This is what i found for your search")
            query = query.replace("google search", "")
            pywhatkit.search(query)
            speak("done sir")
        elif "open website" in query:
            speak("Tell me the name of the website")
            query = query.replace(" ", " ")
            websitename = takecommand().lower()
            web = "https://www." + websitename + ".com"
            webbrowser.open(web)
            speak("Done sir")

        elif "play song on youtube" in query:
            speak("Which song")
            musicName = takecommand()
            pywhatkit.playonyt(musicName)
            speak("enjoy your song sir")
        elif "play video on youtube" in query:
            speak("Which video")
            musicName = takecommand()
            pywhatkit.playonyt(musicName)
            speak("enjoy your video sir")

        elif "send mail" in query:
            try:
                speak("what should i say")
                content = takecommand().lower()
                to = input("Enter the Mail Id Here:")
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("sorry sir,i am not able to sent this mail")

        elif "need a break" in query:
            speak("thanks for using dudes sir,Have a good day,call me anytime")
            sys.exit()
        elif "shutdown the system" in query:
            os.system("shutdown /s /t 5")
        elif "restart the system" in query:
            os.system("shutdown /r /t 5")
        elif "sleep the system" in query:
            os.system("rundll32.exe powrprof.dll,setsuspendstate 0,1,0")
        elif "hello" in query:
            speak("Hello sir,I am your personal Voice assistant")
            speak("How may i help you")
        elif "how are you" in query:
            speak("I am Good ,What about you")
        elif "you need a break" in query:
            speak("ok sir,call me anytime!")
            #break


        elif "take screenshot" in query:
            speak("sir,please tell me the name of the file")
            name = takecommand()
            path = name + ".png"
            path1 = "D:\\Project now" + path
            speak("please sir hold the screen for few second, I am taking screenshot")
            # time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{path}.png")
            os.startfile("D:\\Project now")
            speak("Done sir")
        elif "repeat my words" in query:
            speak("speak sir!")
            jj = takecommand()
            speak(f"you said:{jj}")
        elif "dictionary" in query:
            dicti()
        elif "remember that" in query:
            rememberMsg = query.replace("remember that", " ")
            speak("you tell me to Remind you that" + rememberMsg)
            rem = open('data.txt', 'w')
            rem.write(rememberMsg)
            rem.close()

        elif "what do you remember" in query:
            rem = open('data.txt', 'r')
            speak("you tell Me that" + rem.read())


        elif "file move" in query:
            filemovenew.main()

        elif "temperature" in query:
            search = "temperature in faridabad"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_="BNeawe").text
            speak(f"current {search} is {temp}")

        elif "what is the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            speak(f"Sir, the time is {strTime}")