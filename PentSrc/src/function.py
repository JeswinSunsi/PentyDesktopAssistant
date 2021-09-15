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

# Wolfram Alpha module
@eel.expose
def wlfrm(userinputglobal):
  client = wolframalpha.Client('34U93P-WGR36VG7WE') # Add your wolfram Alpha App ID Key here 
  # A later edit (On 15th Sept 2021 1:25pm GMT+4) - I wrote this code when I was 14 and I didn't know what secrets and .env variables were and now I'm too lazy to remove the wolframalpha secret key so please don't misuse or spam it dear kind internet stranger..
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
