
#!/usr/bin/env python

#imports
import eel
import wolframalpha
import wikipedia
import pyshorteners.shorteners.tinyurl
import speedtest
import time
import socket
import os
import platform
import webbrowser
import smtplib
import ctypes
import linecache
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from win10toast import ToastNotifier
from getmac import getmac
import pyjokes


# Useful when packaging Penty into an exe, since --noconsole in pyinstaller returns an error for some reason.
def hideConsole():
  whnd = ctypes.windll.kernel32.GetConsoleWindow()
  if whnd != 0:
     ctypes.windll.user32.ShowWindow(whnd, 0)
hideConsole()

eel.init('web') # Initialize the 'web' folder where frontend and js is stored.

# Wolfram Alpha module
@eel.expose
def wlfrm(userinputglobal):
  client = wolframalpha.Client('34U93P-WGR36VG7WE') # Add your wolfram Alpha App ID Key here
  res = client.query(userinputglobal)
  answer = (next(res.results).text)
  return answer

# Wikipedia Module
@eel.expose
def wikiped(userinputglobal):
  answer = wikipedia.summary(userinputglobal, sentences=1)
  return answer

# Mailer (Passcode and Username is stored at web/mail_creds.text)
@eel.expose
def email(RECV_ID, CONTENT):
  mainErrorMsg = "Something went wrong.."
  try:
    if CONTENT != '':
      MAIL_ID = linecache.getline(r"web/mreds.txt", 1)
      PASS = linecache.getline(r"web/mreds.txt", 2)
      server = smtplib.SMTP("smtp.gmail.com", 587)
      server.starttls()
      server.login(MAIL_ID, PASS)
      server.sendmail( MAIL_ID, RECV_ID, CONTENT)
      return f"Sending mail to {RECV_ID}"
    else:
      return 'Cancelled mail successfully.'
    linecache.clearcache()
  except (smtplib.SMTPAuthenticationError):
    return f"{mainErrorMsg} \n Please enter your credentials at mail settings."
  except (smtplib.SMTPRecipientsRefused):
    return f"{mainErrorMsg} \n Please enter a valid recipient address."
  except (smtplib.SMTPConnectError):
    return f"{mainErrorMsg} \n Please establish a network connection."
  except:
    return f"{mainErrorMsg}"

# Returns some platform specs
@eel.expose
def platforminfo():
    return f"System: {platform.system()} \n Processor: {platform.processor()} \n Architecture: {platform.architecture()} \n Version: {platform.version()} \n Release: {platform.release()}"

# Quick Browser Module
@eel.expose
def browser(link):
  link_one = f'https://{link}'
  link_suffixes = ['.com', '.org', '.in', '.be']
  for suffix in link_suffixes:
    if suffix in link and ' ' not in link:
      return webbrowser.open(link_one, new=0, autoraise=True)
  link = link.replace(' ', '+')
  link_two = f"https://www.google.com/search?-b-d&q={link}"
  return webbrowser.open(link_two, new=0, autoraise=True)

# A small 'about Pent' Screen
@eel.expose
def about():
  return "Pent is a Desktop Assistant aimed at helping your workflow. It is fast and reliable. Moreover, it does not use any private user data. It uses the Chrome browser (if available), or the windows pre-installed Edge browser. Developed by github.com/JeswinSunsi, with an Idea by repl.com/@SavioXavier."

# Displays the Lan IP
@eel.expose
def ipaddress():
  hostname = socket.gethostname()
  addip = socket.gethostbyname(hostname)
  return f"IP Address : {addip}"

# Displays the MAC Address
@eel.expose
def macaddress():
  addmac = getmac.get_mac_address()
  return f"MAC Address : {addmac}"

# A joke to lighten the mood
def sayJoke():
  return pyjokes.get_joke()

# Toast Reminder
@eel.expose
def reminder():
    remind = ToastNotifier()
    if "set reminder" in userinputglobal:
      remind_text = userinputglobal.replace('set reminder', "")
    elif "reminder" in userinputglobal:
      remind_text = userinputglobal.replace('reminder', "")
    elif "remind" in userinputglobal:
      remind_text = userinputglobal.replace("remind", "")
    timefactor = 0
    for infactor in remind_text.split():
        if infactor.isdigit():
          timefactor = int(infactor)
          #print (timefactor) [For Devt Only]
    if timefactor == 0:
      eel.sleep(2)
      return "Please set a duration."
    remind_text = remind_text.replace(infactor, "")
    remind_text = remind_text.replace("after", "")
    eel.sleep(timefactor)
    retvalue = remind.show_toast("Reminder", remind_text, icon_path='fav.ico', duration = 20)
    return remind_text
    return retvalue

# Quick Restart
@eel.expose
def restrt():
  restart = os.system("shutdown /r /t 1")
  return restart

# Checks the download speed
@eel.expose
def downloadcheck():
  maintest = speedtest.Speedtest()
  download = maintest.download()
  download = int(download) / 1048576
  download = round(download, 3)
  full_answer = f"Download speed: {download}Mbps"
  return full_answer

# Quick Complex Math Evaluator
@eel.expose
def complexMath(question):
  actualQuestion = question.replace(' ', '+')
  actualQuestion = actualQuestion.replace('eval', '')
  link = f'https://www.wolframalpha.com/input/?i={actualQuestion}'
  return webbrowser.open(link, new=0, autoraise=True)

# Checks the upload speed
@eel.expose
def uploadcheck():
  maintest = speedtest.Speedtest()
  upload = maintest.upload()
  upload = int(upload) / 1048576
  upload = round(upload, 3)
  full_answer = f"Upload speed: {upload}Mbps"
  return full_answer

# Function to change email username and passcode
@eel.expose
def emailSettings(email, passcode):
  with open('web/mreds.txt', 'r') as emailAndPass:
    data = emailAndPass.readlines()
  if email != '' and passcode != '':
    data[0] = f'{email} \n'
    data[1] = passcode

  with open('web/mreds.txt', 'w') as emailAndPass:
    emailAndPass.writelines(data)

# The logic that connects it with the user io.
@eel.expose
def mainBackend(userinput):
  global userinputglobal
  userinputglobal = userinput.lower()
  #functions
  try:
    if "download speed" in userinputglobal[0:14] or "download" in userinputglobal[0:8]:
      return downloadcheck()
    elif "joke" in userinputglobal[0:4] or "say joke" in userinputglobal[0:8] or "say a joke" in userinputglobal[0:10]:
      return sayJoke()
    elif 'eval' in userinputglobal[0:4] or 'evaluate' in userinputglobal[0:8]:
      return complexMath(userinputglobal)
    elif "about" in userinputglobal[0:6] or "abt" in userinputglobal[0:4]:
      return about()
    elif "upload speed" in userinputglobal[0:13] or "upload" in userinputglobal[0:6]:
      return uploadcheck()
    elif "restart" in userinputglobal[0:7] or "restrt" in userinputglobal[0:6]:
      return restrt()
    elif "remind" in userinputglobal[0:6] or "set reminder" in userinputglobal[0:12] or "reminder" in userinputglobal[0:8]:
      return reminder()
    elif "ip" in userinputglobal[0:2] or "ip address" in userinputglobal[0:10]:
      return ipaddress()
    elif "mac" in userinputglobal[0:3] or "mac address" in userinputglobal[0:11]:
      return macaddress()
    elif 'system' in userinputglobal:
      return platforminfo()
    else:
        try:
          return wlfrm(userinputglobal)
        except:
          return wikiped(userinputglobal)
  except:
    return "Something went wrong.."

eel.start('main.html', size = (471, 220))
