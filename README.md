# Penty Desktop Assistant

Penty is a Desktop Assistant programmed with JS and Python for its backend and HTML and CSS as its front. It has some cool in-built features, like an emailer, link shortener and a quick-open browser. The main highlight is that it can fetch simple answers from the web, such as the temperature, birthdates, and other quick answers and display them in a visually pleasing window. It uses a Python module named Eel to connect the backend to the GUI (https://github.com/samuelhwilliams/Eel/)

![pent start screen](https://github.com/JeswinSunsi/PentyDesktopAssistant/blob/master/PentSrc/src/web/Media/StartScrExample.PNG)

## Prerequisites 

### Modules
Until you package Penty into an executable, you will have to manually import a lot of modules. The easiest way to do this is with PIP.
```pip install Eel, wolframalpha, wikipedia, pyshorteners, speedtest-cli, win10toast, getmac, pyjokes```

### Others
You will need a google app password for the mailer (https://support.google.com/accounts/answer/185833?hl=en)
If you need the added functionality of WolframAlpha, you'll have to get a free API Key (https://products.wolframalpha.com/simple-api/documentation/)

## Searchbar commands
Apart from answering simple questions, the searchbar can also be used to perform some quick actions when certain commands are typed out. All the commands work in both upper and lowercases.

![pent displays a joke](https://github.com/JeswinSunsi/PentyDesktopAssistant/blob/master/PentSrc/src/web/Media/JokeExample.PNG)

- **IP**
  - This shows the lan IP of the device
- **MAC**
  - Shows out the MAC address
- **Shorten {link address}**
  - Shortens the provided link automatically through tinyurl.com. Do not type out the angle brackets.
- **Shutdown/ shtdwn**
  - Quick command to shutdown the device
- **Restart/ restrt**
  - Quick command to restart the device
- **Eval {math problem}**
  - Uses WolframAlpha to solve complex math problems.
- **Download speed/ download**
  - Shows the download speed (May not be completely accurate)
- **Upload speed/ upload**
  - Shows the upload speed (May not be completely accurate)
- **About**
  - Displays a quick 'About Penty'
- **System**
  - Displays the System details (Operating system, Architecture, etc.)
  
## Icon use
There are four main icons on the main page. These support the main script for more functions.
Usage (from top-left, top-right, bottom-left, bottom-right)
- **Quick Browser**
  - This can come handy when Pent cannot understand your question, cannot display a suitable answer, or the user just wants to quickly open the browser
- **Gmail Sender**
  - For quick mailings. Only supports Google Mail and plain text mails as of yet.
- **System**
  - A quick way to get your device specs.
- **Mail password changer**
  - Should be configured once before first time usage of the inbuilt mailer. Requires the user's mail ID and a google generated app passwords. More on this at https://support.google.com/accounts/answer/185833?hl=en
