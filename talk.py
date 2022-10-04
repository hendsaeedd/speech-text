# import pyttsx3 as pyt


# # talk in german
# def talk(text):
#     engine = pyt.init()
#     voices = engine.getProperty('voices')
#     engine.setProperty('voice', voices[1].id)
#     engine.setProperty('rate', 150)
#     engine.say(text)
#     engine.runAndWait()

# talk('Hallo, ich bin ein Computer')

# engine = pyt.init()
# engine.setProperty('rate', 150)
# engine.say("du bist ein arsch, ich hiesse hend")
# engine.runAndWait()

# Importing all the necessary modules
from tkinter import *
from tkinter.messagebox import showinfo
import pyttsx3
import speech_recognition as sr

# Creating the python text to speech and speech to text functions
def speak(text: str):
    engine = pyttsx3.init()

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('volume', 100)
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()


def record():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.pause_threshold = 2
        audio = r.listen(source)

        try:
            query = r.recognize_google(audio, language="en-IN")
        except Exception as e:
            showinfo(title='Error!', message=e)
            speak("I am sorry, I did not get that, but could you please repeat that")

            return "Nothing"
        return query


# Creating the main TTS and STT functions and the instruction functions
def TTS():
    tts_wn = Toplevel(root)
    tts_wn.title('Text-to-Speech Converter')
    tts_wn.geometry("350x250")
    tts_wn.configure(bg='Brown')

    Label(tts_wn, text='Text-to-Speech Converter', font=("Comic Sans MS", 15), bg='Brown').place(x=50)

    text = Text(tts_wn, height=5, width=30, font=12)
    text.place(x=50, y=50)

    speak_btn = Button(tts_wn, text='Record', bg='LightCoral', command=lambda: speak(str(text.get(1.0, END))))
    speak_btn.place(x=140, y=200)



def instruction():
    instructions = '''
These are the instructions:
1. Wait for some time because conversions take time.
2. Pause for 2 seconds to end your phrase , because that is the pause_threshold amount.
'''
    showinfo("Instructions before beginning", instructions)


# Creating the main GUI window
root = Tk()
root.title('GUI python text to speech ')
root.geometry('300x300')
root.resizable(0, 0)
root.configure(bg='Salmon')

# Placing all the components
Label(root, text=' Text-To-Speech python GUI',
    font=('Comic Sans MS', 16), bg='Salmon', wrap=True, wraplength=300).place(x=15, y=0)

tts_btn = Button(root, text='Start', font=('Helvetica', 16), bg='MediumPurple', command=TTS)
tts_btn.place(x=100, y=150)



instruction_btn = Button(root, text='Instructions before starting', font=('Helvetica', 16), bg='MediumPurple', command=instruction)
instruction_btn.place(x=15, y=250)

# Updating main window
root.update()
root.mainloop()