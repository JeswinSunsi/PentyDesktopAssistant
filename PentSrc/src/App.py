
#!/usr/bin/env python

#imports
from tabnanny import check
import eel
from function import *

# Useful when packaging Penty into an exe, since --noconsole in pyinstaller returns an error for some reason.
def hideConsole():
  whnd = ctypes.windll.kernel32.GetConsoleWindow()
  if whnd != 0:
     ctypes.windll.user32.ShowWindow(whnd, 0)
hideConsole()


eel.init('web') # Initialize the 'web' folder where frontend and js is stored.


# The logic that connects it with the user io.
@eel.expose
def mainBackend(userinput):
  global userinputglobal
  userinputglobal = userinput.lower()

  # Function to check if query is present in userinputglobal
  def check_for_query(*args):
    return any(x in userinputglobal for x in args)

  # Main functions
  try:
    if check_for_query("download speed", "download"):
      return downloadcheck()
    elif check_for_query("joke", "say joke", "say a joke"):
      return sayJoke()
    elif check_for_query("eval", "evaluate"):
      return complexMath(userinputglobal)
    elif check_for_query("about", "abt"):
      return about()
    elif check_for_query("upload speed", "upload"):
      return uploadcheck()
    elif check_for_query("restart", "restrt"):
      return restrt()
    elif check_for_query("reminder", "remind", "set reminder"):
      return reminder()
    elif check_for_query("ip address", "ip"):
      return ipaddress()
    elif check_for_query("mac address", "mac"):
      return macaddress()
    elif check_for_query("system", "system info", "sys"):
      return platforminfo()
    else:
      try:
        return wlfrm(userinputglobal)
      except:
        return wikiped(userinputglobal)
  except:
    return "Something went wrong..."

eel.start('main.html', size = (471, 220))
