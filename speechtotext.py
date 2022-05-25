import pyttsx3
import speech_recognition as sr

# setting a voice using sapi5 speak API
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# function to speak or give audio output to user
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# function to take microphone audio and return string output
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        # setting pause time after execution (program start listening after pause threshlod)  
        r.pause_threshold = 1
        # listening to the source4
        audio = r.listen(source)
    try:
        print("recognizing...")
        # recognizing the audio context using google engine
        query = r.recognize_google(audio, language='en=in')
        print(f'user said: {query}\n')
    except Exception as e:
        print(e)
        print("please say that again.. ")
        return "None"
    return query

if __name__ == "__main__":
    speak("hello sir, please start speaking")
    lines = takeCommand()
    # writing lines into the file
    with open('text.txt', 'w') as f:
        f.write(lines)
    speak("speech to text has been done")
    print("speech to text has been done")