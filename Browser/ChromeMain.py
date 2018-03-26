from chrome import chromelib
from validcommands import commands
import Speechmanager.analizer as al
from Speechmanager.speech_manager import speech as sp
import subprocess
import time
from Speechmanager.TTS import tts

def main():
    try:
        subprocess.call('start chrome',shell = True)
        commands.activatebrowsercommandset()
        chromecommander()
    except OSError:
        print('wrong command ,Such type of command doesnot exist')
        tts.say('wrong command ,Such type of command doesnot exist')

def chromecommander():
    while True:
        command = sp.gstt()
        if command:
            command = al.analize(command)
            if command:
                try:
                    print(command)

                    if(command == "write"):
                        chromelib.write()

                    elif(command == "open new window"):
                        chromelib.OpenNewWindow()

                    elif(command == "open new incognito window"):
                        chromelib.OpenNewIncognitoWindow()

                    elif(command == "open new tab"):
                        chromelib.OpenNewTab()

                    elif(command == "reopen last closed tab"):
                        chromelib.ReopenLastClosedTab()

                    elif(command == "jump to next open tab"):
                        chromelib.JumpToNextOpenTab()

                    elif(command == "jump to previous open tab"):
                        chromelib.JumpToPreviousOpenTab()

                    elif(command == "minimize current window"):
                        chromelib.MinimizeCurrentWindow()

                    elif(command == "close current window"):
                        chromelib.CloseCurrentWindow()

                    elif(command == "close current tab"):
                        chromelib.CloseCurrentTab()

                    elif(command == "quit chrome"):
                        chromelib.QuitChrome()
                        break

                    elif(command == "stop loading page"):
                        chromelib.StopLoadingPage()

                    elif(command == "print current page"):
                        chromelib.PrintCurrentPage()

                    elif(command == "save current page"):
                        chromelib.SaveCurrentPage()

                    elif(command == "reload current page"):
                        chromelib.ReloadCurrentPage()

                    elif(command == "everything on page bigger"):
                        chromelib.EverythingOnPageBigger()

                    elif(command == "everything on page smaller"):
                        chromelib.EverythingOnPageSmaller()

                    elif(command == "everything on page of default size"):
                        chromelib.EverythingOnPageDefaultSize()

                    elif(command == "delete previous word"):
                        chromelib.DeletePreviousWord()

                    elif(command == "go to top of page"):
                        chromelib.GoToTopOfPage()

                    elif(command == "go to end of page"):
                        chromelib.GoToEndOfPage()

                    elif(command == "open chrome menu"):
                        chromelib.OpenChromeMenu()

                    elif(command == "open find bar"):
                        chromelib.OpenFindBar()

                    elif(command == "jump to next match of find bar search"):
                        chromelib.JumpToNextMatchOfFindBarsearch()

                    elif(command == "jump to previous match of find bar search"):
                        chromelib.JumpToPreviousMatchOfFindBarsearch()

                    elif(command == "clear browsing data option"):
                        chromelib.ClearBrowsingDataOption()

                    time.sleep(1)

                except ValueError:
                    print('ValueError: key is a string, but its length is not 1')
                    tts.say('ValueError: key is a string, but its length is not 1')


            else:
                print('analizer doesnot work, Check its settings')
                tts.say('analizer doesnot work, Check its settings')
        else:
            print('error in google speech recognition')
            tts.say('error in google speech recognition')
