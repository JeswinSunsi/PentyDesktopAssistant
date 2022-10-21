# Penty Desktop Assistant

[![GitHub version](https://badge.fury.io/gh/jeswinsunsi%2Fpentydesktopassistant.svg)](https://badge.fury.io/gh/jeswinsunsi%2Fpentydesktopassistant) 
![GitHub version](https://img.shields.io/badge/build-passing-green)

Penty is a proof-of-concept Desktop Assistant designed in Python Eel. Features for the POC include an email client, link shortener, browser, and a WolframAlpha bot. Since it runs on Eel, it supports a GUI window that runs on Chromium.

![pent start screen](https://github.com/JeswinSunsi/PentyDesktopAssistant/blob/master/PentSrc/src/web/Media/StartScrExample.PNG) 

## Prerequisites 

### Modules
The easiest way to get up and running with PIP. Requirements are in requirements.txt

### Others
Since the POC uses a few OS specific modules, only Windows 7 - 11 is fully supported.

The WolframAlpha API key can be accessed from (https://products.wolframalpha.com/simple-api/documentation/)

## Searchbar commands
Apart from answering simple questions, the search bar can also be used to perform quick actions when certain commands are typed in. The commands are not case sensitive.

![pent displays a joke](https://github.com/JeswinSunsi/PentyDesktopAssistant/blob/master/PentSrc/src/web/Media/JokeExample.PNG)

- **{Search term}**
  - You can search for almost anything and Penty will spew out a brief description of it. Stuff like when was x born, the national anthem of the Soviet Union, Who is Guido Van Rossum, all work perfectly.
- **IP**
  - Displays device IP
- **MAC**
  - Displays device MAC
- **Shorten {link address}**
  - Returns a shortened link through tinyurl.com
- **Shutdown/ shtdwn**
  - Shuts down the device
- **Restart/ restrt**
  - Restarts the device
- **Eval {math problem}**
  - Returns solutions to complex algebraic equations
- **Download speed/ download**
  - Displays the download speed
- **Upload speed/ upload**
  - Displays the upload speed
- **About**
  - Displays information on the POC
- **System**
  - Displays system specs & details
## Icon use
Usage (top-left, top-right, bottom-left, bottom-right)
- **Browser**
  - Opens a broswer with provided query.
- **Email client**
  - Runs a basic gmail client.
- **System**
  - Displays device specs & details.
- **Mail password manager**
  - Must be configured once before using the mailing client. Requires mail ID and a google generated app-password. More on this at https://support.google.com/accounts/answer/185833?hl=en
  
## Packaging Pent
Packaging Pent into a distributable is straightforward, and uses PyInstaller. Start by deleting *mailcreds.txt*. Once deleted, navigate to the source directory through the terminal and run - 

```python -m eel app.py web --onefile```

Most PyInstaller flags except --noconsole are supported. A hacky-workaround replacement is coded into *App.py*.
