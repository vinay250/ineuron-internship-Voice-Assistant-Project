
#____________________________________________________________________ V.I.N.A.Y___________________________________________________________________________________________________
#python modules used for this program
import pyttsx3                       # for text to audio conversion
import datetime                      # for obtaining date and time
from datetime import date
import speech_recognition as sr      # for speech recognition and conversion to string
import wikipedia                     # for searching on wikipedia
import webbrowser                    # for opening a webpage in browser
import os                            # for reaching to a certain pathS
import random                        # for picking random number
import pyautogui                     # for taking screenshot
import requests                      # for making API requests
import json                          # for parsing data
from bs4 import BeautifulSoup        # for weather forecasting
import subprocess , time             # for opening windows applications and closing the, after certain interval
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import ctypes
import platform
import tkinter as tk
from tkinter import ttk
import screen_brightness_control as sbc
import wmi
import pywhatkit
import pygetwindow
import socket
import speedtest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import qrcode



# Text to speech using pyttsx3 module.
engine = pyttsx3.init()


#Function to handle button click event
def process_command():
    command = input_entry.get()
    # Process the command here and update the output_label text accordingly
    output_label.configure(text="Command: " + command)





def speak(text):
    """
    This function will convert given text to audio and plays it.
    """
    #engine.setProperty("rate", 200)
    #voices = engine.getProperty("voices")
    #engine.setProperty("voice", voices[1].id)
    engine.say(text)
    engine.runAndWait()

def wish():
    """
    This function will wish the user according to the time
    and ask for further commands.
    """
    hour = datetime.datetime.now().hour
    if (hour < 12):
        text = "Good morning sir!"
        print(text)
        speak(text)
    elif (hour >= 12 and hour <= 18):
        text = "Good afternoon sir!"
        print(text)
        speak(text)
    else:
        text = "Good evening sir!"
        print(text)
        speak(text)
    text = "vinay, is all ready for your commands sir. How may I help you?"
    print(text)
    speak(text)


def day_and_time():
    """
    This function will tell current date and time as per the user input.
    """
    today = str(date.today())
    text = "Sir Today's date is : " + today
    print(text)
    speak(text)

    from datetime import datetime
    time = datetime.today().strftime("%I:%M %p")
    text = "And current time is : " + time
    print(text)
    speak(text)
        
def takeCommand():
    """
    This function takes microphone input from user and returns a string.
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening.....")
        # giving some time before considering it as final input.
        # r.pause_threshold = 1
        audio = r.listen(source,60,60)

        # dealing with external module hence using exception handling.
        try:
           print("Recognizing input...")
           input = r.recognize_google(audio , language = "en-in")
           print(f"You said : {input}\n")

        except Exception as e:
            # print(e)
            text = "Please say it again sir."
            print(text)
            speak(text)
            return "None"
        return input
   

def newsReader():
    """
    This function will tell top 5 news headlines using API and json module.
    """

    req = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=1fcd9f118c5449b8a92c143fd012b922")
    dict = json.loads(req.text)
    text = "Top 5 News for today are:\n"
    print('''=============== TIMES OF INDIA ============'''+ '\n')
    speak('here are some top news from the times of india')
    print(text)
    speak(text)
    print(dict)
    speak(dict)
    
    
    
    #counter = 5s
    #arts = dict['articles']
   #for i in arts:
        #if(counter > 0):
            #print("The Headline is - " + str(i["title"]))
            #speak("The Headline is - " + str(i["title"]))

            #print("Story - " + str(i["description"]))
            #speak(i["description"])

            #print("Checkout the link for detail : " + str(i['url']))
            #speak("Moving to the next news...")

            #counter -= 1

#newsReader()


  #Internet speed
def InternetSpeed():
        speak("Wait a few seconds sir, checking your internet speed")
        print(speak)
        
        st =speedtest.Speedtest()
        download_speed = st.download()/1000000
        upload_speed = st.upload()/1000000
        
        print("NET SPEED :")
        print(f' Download speed: {download_speed:.2f} Mbps || Upload speed: {upload_speed:.2f} Mbps\n')
        speak(f' Download speed: {download_speed:.2f} Mbps || Upload speed: {upload_speed:.2f} Mbps\n')
        print(speak)

def there_exists(terms):
    """
    Function to check if required word or phrase is present in the text or not.
    """
    for term in terms:
        if term in input:
            return True



def details():
    """
    This function will print and speak written text.
    """
    text = "Hello sir! I am vinay. I am a virtual assistant created by vinay sir. " \
           "You can check the things that I can do by saying 'what can you do' or 'things you can do'"
    print(text)
    speak(text)



def vinayWork():
    """
        This function will print and speak written text.
    """
    text = "Sir, I can open numerous applications and webpages, play games, take screenshots, tell you time, date, weather, location and " \
           "can read news headlines, flip coin , search on spotify, google, youtube and wikipedia. I can also calculate, take notes etc." \
           "I am still learning new things from wonderful humans like you. Nice knowing your sir."
    print(text)
    speak(text)


def close_appliction():
    """
    This function will print and speak written text
    """
    text="sir , i can close nemerous applications and webpages ,playgames,take screenshots,wikipedia,google,youtube,musicplayer,webrowser"
    print(text)
    speak(text)

def get_brightness(display=0):
    # Create a connection to the WMI namespace
    c = wmi.WMI(namespace='wmi')

    # Get the current brightness object for the specified display
    brightness = c.WmiMonitorBrightness()[display]

    # Retrieve the current brightness value
    current_brightness = brightness.CurrentBrightness

    return current_brightness

def open_wifi_settings():
    subprocess.run(["start", "ms-settings:network-wifi"], shell=True)
    

def view_connected_devices():
    subprocess.run(["arp", "-a"], shell=True)
    
   
def available_devices():
    subprocess.run(['netsh', 'wlan', 'show', 'network', 'mode=Bssid'], shell=True)
       

#whatsapp
def send_whatsapp_message(mobile_number, message):
    """
    This function sends a WhatsApp message using pywhatkit library.
    """
    mobile_number = mobile_number.replace(' ', '').replace('+91', '')
    if not mobile_number.isdigit() or len(mobile_number) != 10:
        print("Invalid mobile number. Please enter a valid 10-digit mobile number.")
        speak("Invalid mobile number. Please enter a valid 10-digit mobile number.")
    else:
        print("Opening WhatsApp web to send your message...")
        speak("Opening WhatsApp web to send your message...")
        print("Please be patient, sometimes it takes time. OR In some cases, it does not work.")
        speak("Please be patient, sometimes it takes time. OR In some cases, it does not work.")
        try:
            pywhatkit.sendwhatmsg("+91" + mobile_number, message, datetime.datetime.now().hour, datetime.datetime.now().minute + 1)
            print('Message sent successfully.')
            speak('Message sent successfully.')
        except Exception as e:
            print(f"An error occurred: {e}")
            speak(f"An error occurred: {e}")
            print("Error: Message not sent. Please try again.")
            speak("Error: Message not sent. Please try again.")

def perform_calculation(operator, operand1, operand2):
    if operator == '+' or operator == 'add' or operator == 'plus':
        return operand1 + operand2
    elif operator == '-' or operator == 'subtract' or operator == 'minus':
        return operand1 - operand2
    elif operator == 'into' or operator == '*':
        return operand1 * operand2
    elif operator == '/' or operator == 'divide' or operator == 'by':
        return operand1 / operand2
    elif operator == 'power' or operator == '**':
        return operand1 ** operand2
    else:
        return None
    
    
    
def qrCodeGenerator():
        print(f"Boss enter the text/link that you want to keep in the qr code")
        print("Enter the Text/Link : ")
        text = takeCommand()
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=15,
            border=4,
        )
        QRfile_name = (str(datetime.datetime.now())).replace(" ","-")
        QRfile_name = QRfile_name.replace(":","-")
        QRfile_name = QRfile_name.replace(".","-")
        QRfile_name = QRfile_name+"-QR.png"
        qr.add_data(text)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img.save(f"QRCodes\{QRfile_name}")
        print(f"Boss the qr code has been generated")
                        
                        
def temperature():
        IP_Address = requests.get('https://api.ipify.org').text
        url = 'https://get.geojs.io/v1/ip/geo/'+IP_Address+'.json'
        geo_reqeust =requests.get(url)
        geo_data = geo_reqeust.json()
        city = geo_data['city']
        search = f"temperature in {city}"
        url_1 = f"https://www.google.com/search?q={search}"
        r = requests.get(url_1)
        data = BeautifulSoup(r.text,"html.parser")
        temp = data.find("div",class_="BNeawe").text
        speak(f"current {search} is {temp}")
    
                        
                        
                        
                        
def unlock_windows(password):
    pyautogui.moveTo(860, 600)
    pyautogui.typewrite(password)
    pyautogui.hotkey('enter')
    ctypes.windll.user32.LockWorkStation()
    ctypes.windll.user32.UnlockWorkStation()
    
def get_user_input(prompt):
    speak(prompt)
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            audio = recognizer.listen(source, timeout=5)
            user_input = recognizer.recognize_google(audio)
            return user_input
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that. Can you please repeat?")
            print("Sorry, I didn't catch that. Can you please repeat?")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            

def set_alarm():
    user_time = get_user_input("What time would you like to set the alarm for? (HH:MM format)")

    try:
        if user_time:
            # Convert the input time to a datetime object
            alarm_time = datetime.datetime.strptime(user_time, "%H:%M")
            current_time = datetime.datetime.now().time()

            while True:
                current_time = datetime.datetime.now().time()

                # Check if the current time matches the alarm time
                if current_time >= alarm_time.time():
                    speak("Time to wake up!")
                    break

                time.sleep(1)  # Sleep for 1 second before checking again
        else:
            speak("No input received. Please try again.")

    except ValueError:
        speak("Invalid time format. Please use HH:MM.")


def close_browser():
    os.system(" pkill 'Google Chrome'")  # Replace "Google Chrome" with the appropriate browser process name
    
# main function
if __name__ == "__main__":
    wish()
    

    while True:
        input = takeCommand().lower()

        # Greetings.
        if there_exists(["hi" , "hello" , "hey" , "vinay you there"]):
            text = "Hello! vinay at your service sir."
            print(text)
            speak(text)


        elif there_exists(["how are you" , "how you doing" , "whats up"]):
            text = "Hello! Thanks for asking! I am good sir and all ready at your service sir"
            print(text)
            speak(text)


        # Assistant Details.
        elif there_exists(["who are you" , "who made you" , "what is your name"]):
            details()


        # Things that vinay can do.
        elif there_exists(["what can you do" , "things you can do"]):
            vinayWork()


        # Logic behind each task execution as per the input.
        elif there_exists(["day","date","time"]):
            day_and_time()

        #whastspp
        if "send whatsapp message" in input:
            print("Sure! Please provide the 10-digit mobile number of the recipient.")
            speak("Sure! Please provide the 10-digit mobile number of the recipient.")
            mobile_number = takeCommand()
            print("What message would you like to send?")
            speak("What message would you like to send?")
            message = takeCommand()
            send_whatsapp_message(mobile_number, message)
        
        
        
        
        # Searching on wikipedia.
        elif ("wikipedia" in input):
            text = "Searching on Wikipedia sir..."
            print(text)
            speak(text)
            input = input.replace("wikipedia" , "")
            try:
                result = wikipedia.summary(input , sentences=1)
                text = "Sir According to Wikipedia : " + result
                print(text)
                speak(text)
            except Exception as e:
                # print(e)
                text = "Could not recognize or find it sir, can you please say it again?"
                print(text)
                speak(text)


        # Searching on google
        elif there_exists(["search google" , "google search" , "search on google" ,"close the google"]):
            text = "Searching on Google sir..."
            print(text)
            speak(text)
            search_term = input.split("google")[-1]
            try:
                url = "https://google.com/search?q=" + search_term
                webbrowser.get().open(url)
                webbrowser.get().close(url)
                text = "This is what I found on Google sir."
                print(text)
                speak(text)
            except Exception as e:
                # print(e)
                text = "Could not recognize or find it sir, can you please say it again?"
                print(text)
                speak(text)


        # Searching on spotify
        elif there_exists(["search spotify" , "spotify search"]):
            text = "Searching on Spotify sir..."
            print(text)
            speak(text)
            search_term = input.split("spotify")[-1]
            try:
                url = "https://open.spotify.com/search/"+search_term
                webbrowser.get().open(url)
                text = "This is what I found on Spotify sir."
                print(text)
                speak(text)
            except Exception as e:
                # print(e)
                text = "Could not recognize or find it sir, can you please say it again?"
                print(text)
                speak(text)


        # Searching on youtube
        elif there_exists(["search youtube" , "search on youtube" ,"close youtube" ,"open youtube"]):
            text = "Searching on Youtube sir..."
            text ="i quiting youtube sir"
            print(text)
            speak(text)
            search_term = input.split("youtube")[-1]
            try:
                url = "https://www.youtube.com/results?search_query=" + search_term
                text = "This is what I found on Youtube sir."
                print(text)
                speak(text)
                webbrowser.get().open(url)
                webbrowser.quit().close(url)
            except Exception as e:
                 # print(e)
                text = "Could not recognize or find it sir, can you please say it again?"
                print(text)
                speak(text)
                


        # Opening different webpages.
        elif ("open google" in input):
            url = "https://www.google.com/"
            webbrowser.get().open(url)
        if('open top 10 news' in input):
            api_url = "https://timesofindia.indiatimes.com/india/timestopten.cms"  # Replace with the correct API endpoint URL
            webbrowser.open(api_url)
        elif ("open linkedin" in input):
            url = "https://www.linkedin.com/"
            webbrowser.get().open(url)
        elif ("open github" in input):
            url = "http://github.com/"
            webbrowser.get().open(url)
        elif ("open gmail" in input):
            url = "http://gmail.com/"
            webbrowser.get().open(url)
        elif ("open twitter" in input):
            url = "https://twitter.com/"
            webbrowser.get().open(url)
        elif ("open facebook" in input):
            url = "https://www.facebook.com/"
            webbrowser.get().open(url)
        elif ("open flipkart" in input):
            url = "https://www.flipkart.com/"
            webbrowser.get().open(url)
        elif ("open amazon" in input):
            url = "https://www.amazon.in/"
            webbrowser.get().open(url)
        elif ("open stack overlow" in input):
            url = "https://stackoverflow.com/"
            webbrowser.get().open(url)
        elif ("open geeksforgeeks" in input):
            url = "https://www.geeksforgeeks.org/"
            webbrowser.get().open(url)
        elif("open our university"in input):
            url = "https://vskub.ac.in/"
            webbrowser.get().open(url)
        if ("close our university" in input):
            url = "https://vskub.ac.in/"
            webbrowser.get().taskkill(url)
        elif ("lock window" in input):
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()
        elif ("close music" in  input):
            speak("closeing music")
            os.system('taskkill /f /im vlc.exe')
        elif ("close notepad" in input):
            speak("Closing Notepad")
            os.system('taskkill /f /im notepad.exe')
        elif ("close excel" in input):
            speak("Closing Excel")
            os.system('taskkill /f /im excel.exe')
        elif("close powerpoint" in input):
            speak("Closing powerpoint")
            os.system('taskkill /f /im powerpnt.exe ')
        elif("close word" in input):
            speak("Closing word")
            os.system('taskkill /f /im winword.exe')
        elif ("close adobe" in input):
            speak("closing adobe")
            os.system('taskkill/f /im Acrobat.exe')
        elif ("close chrome" in input):
            speak("Closing Chrome")
            os.system('taskkill /f /im chrome.exe')
        elif("close microsoft edge" in input):
            speak("closing microsoft edge")
            os.system('taskkill/f /im msedge.exe')
        elif("close zoom"in input):
            speak("closeing zoom")
            os.system("taskkill /im Zoom.exe /f")
        elif("close whatsapp" in input):
            speak("closeing whatsapp")
            subprocess.Popen('taskkill /im whatsapp.exe /f', shell=True)
        elif("close discord" in input):
            speak(" closeing discord")
            subprocess.Popen('taskkill /im discord.exe /f',shell=True)
        elif( "unlock device" in input):
            speak("Unlocking the device")
            password = "virat"
            unlock_windows(password)
        elif ("close command prompt" in input):
            speak("closeing command prompt")
            os.system("taskkill /im cmd.exe /f")
        elif("close on screen keyboard" in input):
            speak("closeing on screen keyboard")
            os.system("taskkill /im osk.exe /f") 
        elif("close youtube" in input):
            speak("closing youtube")
            url = "https://www.youtube.com/results?search_query=" 
            webbrowser.get().close(url)
            
        
            
            
            
        # playing music.
        elif there_exists(["play" , "music" , "play music" , "song","stop","stop  song","changesong","changethesong","quit music player" "stoptheMusic","stopMusic","close Music floder","existVLCmediaplayer"]):
            musicFolder = "D:\\Music"
            allSongs = os.listdir(musicFolder)
            choice = random.choice(allSongs)
            close=allSongs
            close=musicFolder
            os.startfile(os.path.join(musicFolder , choice))
        elif ("existmusicplayer" in input):
                musicFolder ="D:\\Music"
                
        # opening coding platforms (IDEs) and other applications.
        elif ("open code blocks" in input):
            location = "C:\\Program Files (x86)\\CodeBlocks\\codeblocks.exe"
            os.startfile(location)
        elif ("open visual studio" in input or "open vs code" in input):
            shortcut_path = "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\VS Code.exe"
            target_path = os.path.realpath(shortcut_path)
            os.startfile(target_path)
        elif ("open git" in input):
            location = "C:\\Program Files\\Git\\git-bash.exe"
            os.startfile(location)
        elif ("open pycharm" in input):
            location = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.3.3\\bin\\pycharm64.exe"
            os.startfile(location)
        elif ("open netbeans" in input):
            location = "C:\\Program Files\\NetBeans 8.2\\bin\\netbeans64.exe"
            os.startfile(location)
        elif ("open chrome" in input):
            shortcut_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            target_path = os.path.realpath(shortcut_path)
            os.startfile(target_path)
        elif ("open word" in input):
            shortcut_path = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            target_path = os.path.realpath(shortcut_path)
            os.startfile(target_path)
        elif ("open excel" in input):
            shortcut_path = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE" 
            target_path = os.path.realpath(shortcut_path)
            os.startfile(target_path)
        elif ("open adobe" in input):
            shortcut_path = "C:\\Program Files\\Adobe\\Acrobat DC\\Acrobat\\Acrobat.exe"
            target_path = os.path.realpath(shortcut_path)
            os.startfile(target_path)
        elif("open notepad" in input):
            subprocess.Popen('notepad.exe')
            location = "C:\\Users\\HP\\AppData\\Local\\Microsoft\\WindowsApps\\notepad.exe"
            subprocess.Popen(location)
        elif("open microsoft edge"in input):
            shortcut_path="C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
            target_path = os.path.realpath(shortcut_path)
            os.startfile(target_path)
        elif("open whatsapp"in input):
            subprocess.Popen('start whatsapp:', shell=True)
        elif("open discord"in input):
            subprocess.Popen('start discord:', shell=True)
        elif("open zoom"in input):
            shortcut_path = "C:\\Users\\HP\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"
            target_path = os.path.realpath(shortcut_path)
            os.startfile(target_path)
        elif("open command prompt"in input):
            shortcut_path = "C:\\WINDOWS\\system32\\cmd.exe"
            target_path = os.path.realpath(shortcut_path)
            os.startfile(target_path)
        elif("open on screen keyboard"in input):
            shortcut_path = "C:\WINDOWS\system32\osk.exe"
            target_path = os.path.realpath(shortcut_path)
            os.startfile(target_path)
        elif("open powerpoint" in input):
            shortcut_path = "C:\\Program Files\\Microsoft Office\\root\Office16\\POWERPNT.EXE"
            target_path = os.path.realpath(shortcut_path)
            os.startfile(target_path)
            
        elif( "open wi-fi settings" in input):
            print("opening a wifi settings window")
            speak("opening a wifi settings window")
            open_wifi_settings()
            
        #elif("close wi-fi settings" in input):
            #os.system('taskkill/ms-settings:network-wifi/f')
         

        elif ("view connected devices" in input):
            print("ip devices address")
            speak("ip devices address")
            print("Internet Address and Physical Address and Type")
            speak("Internet Address and Physical Address and Type")
            view_connected_devices()
            
        elif("internet speed" in input):
            InternetSpeed()
            
        elif("get brightness" in input):
            get_brightness(display=0)
            current_brightness = get_brightness()
            print(current_brightness)
            speak(current_brightness)
            # Get the brightness of the primary display
            primary_brightness = get_brightness(display=0)
            print(primary_brightness)
            speak(primary_brightness)
            
            
        elif("available devices" in input):
            print("Available devices:")
            speak("Available devices:")
            print("wifi devices")
            speak("wifi devices")
            available_devices()

        #Command to generate the qr codes
        elif("create a qr code" in input):
                qrCodeGenerator()
        
            #Eg: vinay increase volume
        elif ("volume up" in input) or ("increase volume" in input):
                pyautogui.press("volumeup")
                speak('volume increased')
                print('volume increased')
            #command for decreaseing the volume in the system
            #Eg: vinay decrease volume
        elif ("volume down" in input) or ("decrease volume" in input):
                pyautogui.press("volumedown")
                speak('volume decreased')
                print('volume decreased')
            #Command to mute the system sound
            #Eg: vinay mute the sound
        elif ("volume mute" in input) or ("mute the sound" in input) :
                pyautogui.press("volumemute")
                speak('volume muted')
                print('volume muted')

        elif("set an alarm"in input):
                set_alarm()
        
        #Command for screenRecording
            #Eg: vinay start voice recording
        elif ("voice recording" in input):
                try:
                    print("Boss press q key to stop recordings")
                    speak("Boss press q key to stop recordings")
                    option = input
                    Record_Option(option=option)
                    print("Boss recording is being saved")
                    speak("Boss recording is being saved")
                except:
                    print("Boss an unexpected error occured couldn't start screen recording")
                    speak("Boss an unexpected error occured couldn't start screen recording")
                
                
        #command for knowing your system IP address
            #Eg: vinay check my ip address
        elif ('ip address' in input):
                ip = requests.get('https://api.ipify.org').text
                print(f"your IP address is {ip}")
                speak(f"your IP address is {ip}")
                
             #command for make the system sleep
                #Eg: vinay  sleep the system
        elif ('sleep the system' in input):
                speak("Boss the system is going to sleep")
                os.system("rundll32.exe powrprof.dll, SetSuspendState 0,1,0")
                
        elif ("temp" in input):
                temperature()
                
        # news reading.
        elif ("news" in input):
                newsReader()


        # current location.q
        elif ("location" in input):
            import geocoder
            g = geocoder.ip('me')
            speak(str(g.latlng))
            print(g.latlng)

        # Opening camera
        elif ("camera" in input):
            subprocess.run('start microsoft.windows.camera:', shell=True)
            time.sleep(11)
            text = "Sir it will automatically close after 11 seconds."
            print(text)
            speak(text)
            subprocess.run('Taskkill /IM WindowsCamera.exe /F', shell=True)

        

        # make a note
        elif there_exists(["make a note" , "take a note" , "take note" , "takes notes"]):
            text = "Opening note taker..."
            print(text)
            speak(text)
            try:
                url = "https://keep.google.com/#home"
                text = "Note taker opened sir."
                print(text)
                speak(text)
                webbrowser.get().open(url)
            except Exception as e:
                # print(e)
                text = "Could not recognize or find it sir, can you please say it again?"
                print(text)
                speak(text)


        # Take screenshot
        elif there_exists(["capture" , "capture screen" , "take screenshot" , "screenshot"]):
            myScreenshot = pyautogui.screenshot()
            myScreenshot.save("D:\screenshot\\" + "_vinay_screenshot.png")
            text = "Screenshot taken sir."
            print(text)
            speak(text)



        # Play Rock , Paper , Scissor Game
        elif there_exists(["game" ,  "rock paper scissor"]):
            text = "Please choose among rock, paper and scissor"
            print(text)
            speak(text)

            pmove = takeCommand()

            moves = ["rock", "paper", "scissor"]
            cmove = random.choice(moves)

            if pmove == cmove:
                text = "the match is draw"
                print(text)
                speak(text)
            elif (pmove == "rock" and cmove == "scissor") or (pmove == "paper" and cmove == "rock") or (pmove == "scissor" and cmove == "paper"):
                text = "Player wins"
                print(text)
                speak(text)
            elif (pmove == "scissor" and cmove == "rock") or (pmove == "rock" and cmove == "paper") or ("paper" and cmove == "scissor"):
                text = "Computer wins"
                print(text)
                speak(text)


        # Weather Forecasting.
        elif there_exists(["temperature" , "weather" , "what is the weather" , "how is the weather"]):
            try :
                url = "https://google.com/search?q=" + input
                r = requests.get(url)
                data = BeautifulSoup(r.text , "html.parser")
                weather = data.find("div" , class_="BNeawe").text
                output = "Current weather is : " + weather
                print(output)
                speak(output)
            except Exception as e:
                # print(e)
                text = "Could not recognize or find it sir, can you please say it again?"
                print(text)
                speak(text)


        # Toss a coin
        elif there_exists(["toss" , "flip" , "coin"]):
            moves = ["head" , "tails"]
            choice = random.choice(moves)
            text = "Sir we have got : " + choice
            print(text)
            speak(text)

        # Calculations.
        elif there_exists(["calculate", "plus", "minus", "add", "into", "subtract", "multiply", "divide", "+", "-", "*", "/", "power", "**","velocity","square"]):
         try:
            operator = input.split()[1]
            num1 = int(input.split()[0])
            num2 = int(input.split()[2])
        
            # Simple arithmetic calculations
            result = perform_calculation(operator, num1, num2)
            if result is not None:
                speak(result)
        
             # Simple physics formulas
            elif operator == 'velocity':
                speak(f"The velocity is {num1} m/s.")
            elif operator == 'acceleration':
                speak(f"The acceleration is {num1} m/s^2.")
        
            # Simple commerce formulas
            elif operator == 'profit_percentage':
                profit_percent = (num1 / num2) * 100
                speak(f"The profit percentage is {profit_percent:.2f}%.")
        
            # Simple math formulas
            elif operator == 'square':
                speak(f"The square of {num1} is {num1 ** 2}.")
            elif operator == 'cube':
                speak(f"The cube of {num1} is {num1 ** 3}.")
            elif operator == 'square_root':
                speak(f"The square root of {num1} is {num1 ** 0.5}.")
            elif operator == 'cube_root':
                speak(f"The cube root of {num1} is {num1 ** (1/3)}.")
            else:
                speak("Sorry, I couldn't recognize the formula. Please try again.")
         except Exception as e:
                text = "Could not recognize or find it, sir. Can you please say it again?"
                print(text)
                speak(text)


        # About creator.
        elif there_exists(["creator", "vinay"]):
            text = '''
                    vinay is a  student, pursuing master in Computer Science . 
                    he was actully studing  in vijanagara sri krishnadevaraya university ballari
                    he was tecnically build by me .......thank you vinay
                    '''
            speak(text)
            



        # Terminating vinay
        elif there_exists(["sleep" , "nothing" , "bye" , "exit" , "quit" , "thank you","vinay thank you","thank you vinay"]):
            text = "Bye. See you soon sir. Take care!"
            print(text)
            speak(text)
            break
        
    
    



    
