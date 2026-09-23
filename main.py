import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import feedparser
import gemini

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 160)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def get_news():
    url = "https://news.google.com/rss?hl=en-IN&gl=IN&ceid=IN:en"
    news = feedparser.parse(url)

    for article in news.entries[:10]:
        print(article.title)
        speak(article.title)

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open chat gpt" in c.lower():
        webbrowser.open("https://chatgpt.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ", 1)[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        get_news()
    else:
        # let open AI handle the case
        answer = gemini.askAI(c)
        print(answer)
        speak(answer)

r = sr.Recognizer()
if __name__ == "__main__":
    speak("Initializing Genius Navaneet.....")

    while True:
        # Listen for the wake work Genius Navaneet
        # obtain audio from the microphone

        # recognize speech using google
        try:
            with sr.Microphone() as source:
                print("Listening!!!....")
                audio = r.listen(source, timeout=5, phrase_time_limit=5)
            word = r.recognize_google(audio)
            print(word)
            if "genius navneet" in word.lower():
                speak("Hellowwww         ,genius Navaneet is  listening")
                # Listen command
                with sr.Microphone() as source:
                    print("Genius Navaneet Activated!!!..")
                    audio = r.listen(source, timeout=5, phrase_time_limit=5)
                    command = r.recognize_google(audio)
                    if command.lower().startswith("open"):
                        speak("opening" + command.split(" ", 1)[1])
                    elif command.lower().startswith("play"):
                        speak("playing" + command.split(" ", 1)[1])
                    print(command)
                    processCommand(command)

        except Exception as e:
            print("Error; {0}".format(e))
