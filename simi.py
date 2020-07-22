import pyaudio
import speech_recognition as sr
import os
import re
import pyttsx3
import random
import webbrowser
import smtplib
import requests
import weather
import glob
from time import localtime, strftime
#import speaking


#speaking functionlity
speak = speaking.speaker

doss = os.getcwd()
i=0
n=0
INFO = '''
        ->Here are the available commands
        ->open website,
        ->open reddit,
        ->greetings (hello, hi, etc),
        ->adding all of them when completed
            '''
print(INFO)
################################# simi sound recognitions mechanism #################################
while (i<1):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.adjust_for_ambient_noise(source)
        n=(n+1)
        ready = "I am ready for your command!"
        print(ready)
        speak(ready)
        audio = r.listen(source)
    try:
        s = (r.recognize_google(audio))
        command = (s.lower())
        print (command)
        #common commands for simi
        if ('goodbye') in command or ('stop simi') in command or ('power off') in command or ('go to sleep') in command:                          
            rand = ['Goodbye Genes', 'simi powering off in 3, 2, 1, 0']
            speak(rand)
            break
        #Time checking
        elif ('what is the time') in command or ('what time is it') in command or ('time') in command:
            Ctime= strftime("%X", localtime())
            rand = [Ctime]
            speak(rand)

        elif ('hello') in command or ('hi') in command:
            rand = ['Welcome, I am simi, ready at your service   Genes..!.']
            speak(rand)

        elif ('thanks') in command or ('tanks') in command or ('thank you') in command:
            rand = ['You are welcome', 'no problem']
            speak(rand)

        elif command == ('simi'):
            rand = ['Yes Genes?', 'What can I do for you Genes?']
            speak(rand)

        elif  ('how are you') in command or ('and you') in command or ('are you okay') in command:
            rand = ['Fine thank you']
            speak(rand)

        elif  ('*') in command:
            rand = ['Be polite please']
            speak(rand)

        elif ('your name') in command:
            rand = ['My name is simi, at your service Genes']
            speak(rand)

        #elif ('*') in command:
         #   rand = ['Hell, you, too..!']
          #  speak(rand)
        #jokes
        elif 'joke' in command:
            res = requests.get(
                'https://icanhazdadjoke.com/',
                headers={"Accept":"application/json"}
                )
            if res.status_code == requests.codes.ok:
                speak(str(res.json()['joke']))
            else:
                speak('oops!I ran out of jokes')

        #checking connection
        #elif ('wi-fi') in command or ('check connection') in command or ('connection') in command:  
         #   REMOTE_SERVER = "www.google.com"
          #  speaking.wifi()
           # rand = ['We are connected']
            #speak(rand)

        #opening websites
        elif ('open website') in command:
            rg_exp = re.search('open website (.+)', command)
            if rg_exp:
                domain = rg_exp.group(1)
                url = 'https://www.' + domain
                webbrowser.open(url)
                sayer = 'opening website ' + domain
                print(sayer)
                speak(sayer)
        
        #opening reddit
        elif('open reddit') in command:
            rg_exp = re.search('open reddit(.*)',command)
            url = 'https:/www.reddit.com/'
            if rg_exp:
                subreddit = rg_exp.group(1)
                url = url + 'r/' + subreddit
            webbrowser.open(url)
            rand = 'opening reddit'
            print(rand)
            speak(rand)

        #opening google maps via chrome
        elif ('google maps') in command:
            query = command
            stopwords = ['google', 'maps']
            querywords = query.split()
            resultwords  = [word for word in querywords if word.lower() not in stopwords]
            result = ' '.join(resultwords)
            Chrome = ("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s")
            webbrowser.get(Chrome).open("https://www.google.be/maps/place/"+result+"/")
            rand = [result+'on google maps']
            speak(rand)

        #weather checking
        elif 'current weather in' in command:
            reg_ex = re.search('current weather in (.*)', command)
            if reg_ex:
                city = reg_ex.group(1)
                weather = Weather()
                location = weather.lookup_by_location(city)
                condition = location.condition()
                speak('The Current weather in %s is %s The tempeture is %.1f degree' % (city, condition.text(), (int(condition.temp())-32)/1.8))

        elif 'weather forecast in' in command:
            reg_ex = re.search('weather forecast in (.*)', command)
            if reg_ex:
                city = reg_ex.group(1)
                weather = Weather()
                location = weather.lookup_by_location(city)
                forecasts = location.forecast()
                for i in range(0,3):
                    speak('On %s will it %s. The maximum temperture will be %.1f degree.'
                             'The lowest temperature will be %.1f degrees.' % (forecasts[i].date(), forecasts[i].text(), (int(forecasts[i].high())-32)/1.8, (int(forecasts[i].low())-32)/1.8))


        #starting applications
        elif command != ('start music') and ('start') in command:   
            query = command
            stopwords = ['start']
            querywords = query.split()
            resultwords  = [word for word in querywords if word.lower() not in stopwords]
            result = ' '.join(resultwords)
            os.system('start ' + result)
            rand = [('starting '+result)]
            speak(rand)

        #stoping running applications
        elif command != ('stop music') and ('stop') in command:
            query = command
            stopwords = ['stop']
            querywords = query.split()
            resultwords  = [word for word in querywords if word.lower() not in stopwords]
            result = ' '.join(resultwords)
            os.system('taskkill /im ' + result + '.exe /f')
            rand = [('stopping '+result)]
            speak(rand)

        #email sending functionality
        elif ('email') in command or ('send mail') in command:
            speak('Who is the recipient?')
            recipient = Commands()
            if 'kenny' in recipient:
                speak('What should I say?')
                content = commands()
                #init gmail SMTP
                mail = smtplib.SMTP('smtp.gmail.com', 587)
                #identify to server
                mail.ehlo()
                #encrypt session
                mail.starttls()
                #login
                mail.login('username', 'password')
                #send message
                mail.sendmail('name', 'email', content)
                #end mail connection
                mail.close()
                speak('Email sent.')

        #installing python packages with pip
        elif ('install') in command:
            query = command
            stopwords = ['install']
            querywords = query.split()
            resultwords  = [word for word in querywords if word.lower() not in stopwords]
            result = ' '.join(resultwords)
            rand = [('installing '+result)]
            speak(rand)
            os.system('python -m pip install ' + result)

        #sleeping the computer
        elif ('sleep mode') in command:
            rand = ['good night']
            speak(rand)
            os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')

        #Playing music from the music folder
        elif ('music') in command:
            mus = random.choice(glob.glob(doss + "music" + "\\*.mp3"))
            os.system('chown -R user-id:group-id mus')
            os.system('start ' + mus)
            rand = ['start playing']
            speak(rand)
        else:
            print('say something')
    except sr.UnknownValueError:
        print("$Could not understand what you said \n")
    except sr.RequestError as e:
        print("Could not request results$; {0} \n".format(e))
