#!/usr/bin/env python
# coding: utf-8

# Personal Voice Assistant

# In[]:


import pyttsx3                               
import datetime
import speech_recognition as sr              
import wikipedia
import webbrowser as wb                      
import sys,bs4,requests
import urllib.request, urllib.parse, urllib.error
import json
from subprocess import call
import os
import time
import googletrans
from PIL import ImageGrab                    
from PIL import Image

eng=pyttsx3.init("sapi5")                     #sapi5 is microsoft speech API .
voices=eng.getProperty("voices")              #fetches the voices available in your pc.
eng.setProperty("voice",voices[1].id)         #sets the value of voice as voice present as index 1 in your computer.


def speak(audio):
    eng.say(audio)
    eng.runAndWait() 
    
    
def takeinput():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)
    try:
        print("Recognising....")
        query=r.recognize_google(audio)
        print("User Said: ",query)
    except Exception as e:
        print("Say that again!")
        return "none"
    return query    


def wish():
    h=int(datetime.datetime.now().hour)                 
    if (h<12 and h>=0):
        speak("Good Morning!")
    elif (h>=12 and h<=16):
        speak("Good Afternoon!")  
    else:
        speak("Good Evening!")
    speak("Hey, I am Anna, your personal voice assistant. How can I help you?")    

    
def getweather():
    api_key="8ef61edcf1c576d65d836254e11ea420"
    base_url="https://api.openweathermap.org/data/2.5/weather?"
    speak("whats the city name")
    city_name = takeinput()
    complete_url=base_url+"appid="+api_key+"&q="+city_name
    response = requests.get(complete_url)
    x=response.json()
    if x["cod"]!="404":
        y=x["main"]
        current_temperature = y["temp"]-273.15
        current_humidiy = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        speak(" Temperature in Celsius is " +
              str(current_temperature) +
              "\n humidity in percentage is " +
              str(current_humidiy) +
              "\n description  " +
              str(weather_description))
        print(" Temperature in Celsius = " +
              str(current_temperature) +
              "\n humidity (in percentage) = " +
              str(current_humidiy) +
              "\n description = " +
              str(weather_description))
    else:
        speak(" City Not Found ")      
                
def gettranslation():
    trans=Translator()
    speak("What do you want to translate ?")
    msg=takeinput().lower()
    flag=True
    while (flag==True):
        speak("In which language do you want to translate it?")
        d=takeinput().lower()
        if(d=="chinese"):
            d='chinese (simplified)'
        if (d=="kurdish"):
            d='kurdish (kurmanji)' 
        if (d=="myanmar"):
            d='myanmar (burmese)'
        if d in googletrans.LANGUAGES.values():
            v=trans.translate(msg ,dest=d)
            ans="Google translation of "+ msg + " in " + d +" is "+v.text 
            speak(ans)
            print(ans)
            flag=False
        else:
            speak("Speak language name clearly")
    return "none"
    
    
def takescreenshot():
    snapshot = ImageGrab.grab()
    save_path = "desktop/MySnapshot.png"
    snapshot.save(save_path)
    snapshot.show()
    speak("Successfully taken the screenshot. Please check your desktop and taskbar.")
    
    
if __name__ == "__main__":
    
    wish()
    if 1 :
        query=takeinput().lower()
        speak("Searching results for")
        speak(query)


        if "wikipedia" in query:
            query=query.replace("wikipedia","")
            try:
                results=wikipedia.summary(query,sentences=1)
                print(results)
                speak("According to wikipedia,")
                speak(results)
            except Exception as ex :  
                speak("google speech recognition could not find answers")
            except sr.RequestError : 
                speak("couldn't get the results from google speech recognition") 
                
                
        elif "on google" in query:
            query=query.replace("on google","")
            try:
                wb.open("https://www.google.com/search?q="+query)
                speak("Opened on Google")
            except Exception as exc :  
                speak("google speech recognition could not find answers")
        
        
        elif "on youtube" in query:
            query=query.replace("on youtube","")
            try:
                wb.open("https://www.youtube.com/results?search_query="+query)
                speak("Opened results in new tab")
            except Exception as exc :  
                speak("google speech recognition could not find answers")   


        elif "on github" in query:
            query=query.replace("on github","")
            try:
                wb.open("https://github.com/search?q="+query)
                speak("Opened results in new tab")
            except Exception as exc :  
                speak("google speech recognition could not find answers")


        elif "on stackoverflow" in query:
            query=query.replace("on stackoverflow","")
            try:
                wb.open("https://stackoverflow.com/search?q="+query)
                speak("Opened results in new tab")
            except Exception as exc :  
                speak("google speech recognition could not find answers")        

        
        elif "open youtube" in query:
            wb.open("https://www.youtube.com/")
        

        elif "open google" in query:
            wb.open("https://www.google.com/")


        elif "open instagram" in query:
            wb.open("https://www.instagram.com/") 


        elif "open twitter" in query:
            wb.open("https://twitter.com/") 


        elif "open stack overflow" in query:
            wb.open("https://stackoverflow.com/") 
        
        
        elif "the time" in query:
            h=str(datetime.datetime.now().hour)
            m=str(datetime.datetime.now().minute)
            s=str(datetime.datetime.now().second)
            st= (h+ "hours " + m + " minutes " + s + " seconds ")
            speak(st)
        
     
        elif "translate" in query:
            try:
                print("searching....")
                gettranslation()
            except Exception as exc:
                speak("Please Speak again")

        elif "weather" in query:
            try:
                getweather()
            except Exception as exc:
                speak("Could not access weather details")
        
                
        elif "screenshot" in query:
            try:    
                print("Taking Screenshot...")
                speak("Taking Screenshot...")
                takescreenshot()        
            except Exception as exp:
                speak("Try Again!")

        elif "who are you" in query:
            speak("Here is a brief intro : I am Anna version 1 point O your personal voice assistant created by Anshika Sariya. I am programmed to perform minor tasks such as opening youtube, google chrome , instagram, twitter, gmail and stackoverflow") 
            speak("tell time, take a screenshot, search wikipedia, predict weather of different cities and get top headline news from times of india.")
            speak(" I translate sentences into various languages. I am also trained to open in-built applications like calculator, command prompt etc. I can help in searching solutions on GitHub, stack overflow, youtube as well as google" )
            speak("what can I do for you?")
            print("Here is a brief intro about me: I am Anna version 1 point O your personal voice assistant created by Anshika Sariya. I am programmed to perform minor tasks such asopening youtube,google chrome , instagram, twitter, gmail and stackoverflow ,tell time,take a screenshot,search wikipedia,predict weather in different cities and get top headline news from times of india." )
            print(" I translate sentences into various languages. I am also trained to open in-built applications like calculator, command prompt etc. I can help in searching solutions on GitHub, stack overflow, youtube as well as google" )
            print("what can I do for you?")

            
        elif 'news' in query:
            news = wb.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            
            
        elif "open calculator" in query:
            call(["calc.exe"])
                
        
        elif "open command prompt" in query:
            os.system("start /wait cmd {command}")
        
        elif "how are you" in query:
            speak("I am fine and what about you ?")
        
        
        elif "good bye" in query or "bye" in query or "stop" in query:
            speak('your personal assistant Anna is shutting down,Good bye')
            print ('your personal assistant Anna is shutting down,Good bye')
            
            
        else:
            speak("Here are the google search results for it.")
            try:
                wb.open("https://www.google.com/search?q="+query)
            except Exception as exc :  
                speak("Even google speech recognition could not find answers, Please speak clearly")

         
            


# In[ ]:





# In[ ]:




