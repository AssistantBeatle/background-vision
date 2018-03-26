import subprocess

def main():
    try:
        subprocess.call('start nvda',shell = True)
        #commands.activatemswordcommandset()
        #commander()
    except OSError:
        print('wrong command ,Such type of command doesnot exist')
        tts.say('wrong command ,Such type of command doesnot exist')
def stop_mousehover():
    try:
        subprocess.call('taskkill /im nvda.exe /f',shell = True)
        #commands.activatemswordcommandset()
        #commander()
    except OSError:
        print('wrong command ,Such type of command doesnot exist')
        tts.say('wrong command ,Such type of command doesnot exist')
