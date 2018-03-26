from Speechmanager.speech_manager import speech as sp
import Speechmanager.analizer as al
from Speechmanager.TTS import tts
from Commander.commander import commander
import urllib2
from validcommands import commands as co

#body of mainloop
def mainloop():
    if internet_on():
        #activate system commandset
        co.activatesystemcommandset()
        command = sp.gstt()
        if command:
            command = al.analize(command)
            if command:
                #print(command)
                status=commander.main(command)
                if(status==-1):
                     return -1;
            else:
                mainloop()
        else:
            tts.say('Check settings again')
            print('Check settings again')

    else:
        raise Exception('check internet connection and try again')


#function for checking net connectivity
def internet_on():
    try:
        urllib2.urlopen('http://216.58.192.142', timeout=1)
        return True
    except urllib2.URLError as err:
        return False

#starting mainloop
mainloop()
