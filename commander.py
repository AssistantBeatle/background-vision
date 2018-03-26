from Word import wordmain
from Mousehover import mousehover
from Speechmanager.TTS import tts
from Browser import ChromeMain
class commander:
    @staticmethod
    def main(command):
        print(command)
        if(command == "open msword"):
            wordmain.main()
        if(command == "start mousehover"):
            mousehover.main()
        if(command == "stop mousehover"):
            mousehover.stop_mousehover()
        if(command == "open chrome"):
            ChromeMain.main()
        if(command == "exit"):
            return
        else:
            tts.say('error')
            print('error')
