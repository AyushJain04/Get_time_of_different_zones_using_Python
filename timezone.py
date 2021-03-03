# Code for time in different time zone

import pendulum
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 170)  # rate for speaking
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)
    # for female voice
    engine.say(text)
    engine.runAndWait()
speak("Hello! here you can see timezones of differnt zones.")
# current details
d1=pendulum.now()
# splitting for getting date and time
dt1 = str(d1).split(".")
speak("Here's your current timezone with curret date and time.") # for diaplaying timezone
print(f"Currrent date and time: {dt1[0]}") # as we splitted time and timezone
speak("Enter the zone you wish to see the time!")
i = input("Enter here: ")
# details of inputed timezone

try:
    d2 = pendulum.now(i)
    dt2 = str(d2).split(".")
    speak("Here's details")
    print(f"Current date and time for {d2.timezone_name} : {dt2[0]}")

except Exception as e:
    speak("Sorry, You have entered incorrect timezone!")
    speak("Please check and try again!")
