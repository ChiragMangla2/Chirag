import os
import shutil

import pyttsx3
import speech_recognition as sr

# it takes microphone input from the user and returns string output
Engine = pyttsx3.init('sapi5')
voices = Engine.getProperty('voices')
Engine.setProperty('voice', voices[0].id)


def speak(audio):
    Engine.say(audio)
    print(f": {audio} ")
    print("   ")
    Engine.runAndWait()


Engine.setProperty('rate', 180)


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print(f"user said:{text}\n")
        return text
    except:
        speak("say that again please...")
        takecommand()


def drives():
    all_drives = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    my_drives_li = []
    for each_drive in all_drives:
        drive_name = each_drive + ":\\"
        if os.path.exists(drive_name):
            my_drives_li.append(each_drive)
    return my_drives_li


# find function find the file path
def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)


"""ch=drives()
ch.remove('C')
ch.append('C')"""


# exten function is used for get file extension
def exten():
    global file_extention
    speak("What's your file type: ")
    choice = takecommand()
    choice = choice.capitalize()
    if choice == "Text" or choice == "TEXT":
        file_extention = "txt"
    elif choice == "Word" or choice == "WORD":
        file_extention = "docx"
    elif choice == "Python" or choice == "PYTHON":
        file_extention = "py"
    elif choice == "Excel" or choice == "EXCEL":
        file_extention= "xlsx"
    elif choice == "Pdf" or choice == "PDF":
        file_extention = "pdf"
    elif choice == "JPEG" or choice == "JPG":
        file_extention = "JPEG"
    else:
        file_extention = ""
    return file_extention


def main():
    global current_path
    ch = drives()
    ch.remove('C')
    ch.append("C")
    speak("What's your file name which you want to move : ")
    fname = takecommand()
    fname = f"{fname}.{exten()}"

    for p in ch:
        r = find(fname, f"{p}:")
        if (r != None):
            drive, path = r.split(":")
            current_path = f"{drive}:\\{path}"
            speak(f"File was found in {current_path}")
            break

    bfname = f"\{fname}"
    if bfname in current_path:
        open_explorer_path = current_path.replace(bfname, '')
        speak(open_explorer_path)
    #    os.startfile(open_explorer_path)

    speak("In which drive you want to move the file : ")
    dest_drive = input()
    dest_drive = dest_drive.capitalize()

    if dest_drive in ch:
        dest_drive = f"{dest_drive}:\\"
        destination_file_path = f"{dest_drive}:\{fname}"
        try:
            shutil.move(current_path, dest_drive)
            speak("File has successfull moved")
            # os.system("taskkill /f /im explorer.exe")
        except:
            speak("File is Already present here")
    else:
        speak(f"{dest_drive} is not present in your computer.")
