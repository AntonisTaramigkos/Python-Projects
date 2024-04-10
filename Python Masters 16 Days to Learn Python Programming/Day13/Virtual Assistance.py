#Day 13 
#Virtual Assistance!

import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

 
# Hear the microphone and return the audio in text
def transform_audio_into_text():

    #store recognizer in variable
    r = sr.Recognizer()

    #set microphone
    with sr.Microphone() as source:

        #waiting time
        r.pause_threshold = 0.8

        # report the recording has begun
        print("Μπορεις να μιλήσεις!!")

        # save what to hear as audio
        audio = r.listen(source)

        try:
            #search on google
            request = r.recognize_google(audio, language = "en-US")

            #test in text
            print("Είπες :"+ request)

            #return request
            return request
        
        #in case it doesnt understand audio

        except sr.UnknownValueError:
            print("Λυπάμαι, δεν μπόρεσα να καταλάβω τι είπατε.")  # Error message in Greek
            # return error
            return "Ακόμα περιμένω!"
        
        #in case the request cannot be undertood

        except sr.RequestError as e:
            print("Λυπάμαι, υπήρξε ένα σφάλμα κατά τη σύνδεση με το Google API.")  # Error message in Greek
        
        # Unexpected error
        except:

            #show proof that it didnt understand the audio
            print("Ups! Κάτι πήγε στραβά!!")
            # return error
            return "I am still waiting"

#Function so the assistant can be heard            
def speak(message):
    #start engine of pyttsx3
    engine = pyttsx3.init()

    #delver message
    engine.say(message)
    engine.runAndWait()

#Inform day of the week
def ask_day():
    #create a variable wth today information
    day = datetime.date.today()
    print(day)
    # create variable for day of the week
    week_day =  day.weekday()
    print(week_day)
    calendar  = {0: "Monday",
                 1: "Thusday",
                 2: "Wensday",
                 3: "Thursday",
                 4: "Friday",
                 5: "Saturday",
                 6: "Sunday"}
    speak(f"Today is {calendar[week_day]}")
# transform_audio_into_text()
#speak(transform_audio_into_text())


# Inform what time is it
def ask_time():
    # Variable 
    time = datetime.datetime.now()
    time = f"At this moment it is {time.hour} hours and {time.minute} minutes"

    speak(time)    

#Create initial greeting
def initial_greeting():
    speak("I am Zahara, your personal assistance! How can i help?")

#Main Function of the assistant
def my_assistance():

        #Activate the Initial Greetin
        initial_greeting()
        #Cut-off Variable
        go_on = True

        # Main Loop
        while go_on:

            #Activate Microphone and save request
            my_request = transform_audio_into_text().lower()

            if "open youtube" in my_request:
                speak("Sure I am opening youtube")
                webbrowser.open("http://www.youtube.com")
                continue
            elif "open browser" in my_request:
                speak("Of course i am on it") # na balo diafoous xeretismous
                webbrowser.open("http://www.google.com")
                continue
            elif "what day is today" in my_request:
                ask_day()
                continue
            elif "what time it is" in my_request:
                ask_time()
                continue
my_assistance()