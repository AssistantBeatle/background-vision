import speech_recognition as sr
from word import wordlib
from validcommands import commands
import Speechmanager.analizer as al
from Speechmanager.speech_manager import speech as sp
import subprocess
import time
from Speechmanager.TTS import tts
# Record Audio
r = sr.Recognizer()

boldActivator = False
underlineActivator = False
italicActivator = False

def main():
    try:
        subprocess.call('start winword',shell = True)
        commands.activatemswordcommandset()
        wordcommander()
    except OSError:
        print('wrong command ,Such type of command doesnot exist')
        tts.say('wrong command ,Such type of command doesnot exist')

def stopword():
    try:
        subprocess.call('taskkill /im winword.exe /t',shell = True)
        import index
        index.mainloop()
    except OSError:
        print('wrong command ,Such type of command doesnot exist')
        tts.say('wrong command ,Such type of command doesnot exist')

def wordcommander():
    while True:
        command = sp.gstt()
        if command:
            command = al.analize(command)
            if command:
                try:
                    print(command)
                    if(command == "read"):
                        wordlib.read()

                    elif(command == "write"):
                        wordlib.write()

                    elif(command == "save"):
                        wordlib.save()

                    elif(command == "select all"):
                        wordlib.select_all()

                    elif(command == "deselect"):
                        wordlib.deselect()

                    elif(command == "bold"):
                        boldActivator = True
                        wordlib.bold()

                    elif(command == "italic"):
                        italicActivator = True
                        wordlib.italic()

                    elif(command == "remove bold"):
                        if boldActivator is True:
                            wordlib.bold()
                            boldActivator = False

                    elif(command == "remove italic"):
                        if italicActivator is True:
                            wordlib.italic()
                            italicActivator = False

                    elif(command == "underline"):
                        underlineActivator = True
                        wordlib.underline()

                    elif(command == "remove underline"):
                        if underlineActivator is True:
                            wordlib.underline()
                            underlineActivator = False

                    elif(command == "close exit quit"):
                        wordlib.close()

                    elif(command == "copy"):
                        wordlib.copy()

                    elif(command == "paste"):
                        wordlib.paste()

                    elif(command == "decrease font size"):
                        wordlib.decrease_font_size()

                    elif(command == "increase font size"):
                        wordlib.increase_font_size()

                    elif(command == "cut text"):
                        wordlib.cut_text()

                    elif(command == "undo"):
                        wordlib.undo()

                    elif(command == "redo"):
                        wordlib.redo()

                    elif(command == "left align text"):
                        wordlib.left_align_text()

                    elif(command == "right align text"):
                        wordlib.right_align_text()

                    elif(command == "create new document"):
                        wordlib.create_new_document()

                    elif(command == "split document window"):
                        if(splitDocumentWindowActivator == False):
                            splitDocumentWindowActivator = True
                            wordlib.split_document_window()
                        else:
                            tts.say('split document window is already activated')

                    elif(command == "remove split document window"):
                        if(splitDocumentWindowActivator == True):
                            wordlib.split_document_window()

                    elif(command == "print document"):
                        wordlib.print_document()

                    elif(command == "double underline"):
                        if (doubleUnderlineActivator == False):
                            doubleUnderlineActivator = True
                            wordlib.double_underline()
                        else:
                            tts.say('double underline is already activated')

                    elif(command == "remove double underline"):
                        if doubleUnderlineActivator is True:
                            wordlib.double_underline()
                            underlineActivator = False

                    elif(command == "apply subscript"):
                        if (subscriptActivator == False):
                            subscriptActivator = True
                            wordlib.subscript()
                        else:
                            tts.say('subscript is already activated')

                    elif(command == "remove subscript"):
                        if subscriptActivator is True:
                            wordlib.subscript()
                            subscriptActivator = False

                    elif(command == "apply superscript"):
                        if (superscriptActivator == False):
                            superscriptActivator = True
                            wordlib.superscript()
                        else:
                            tts.say('superscript is already activated')

                    elif(command == "remove superscript"):
                        if superscriptActivator is True:
                            wordlib.superscript()
                            superscriptActivator = False

                    elif(command == "one character right"):
                        wordlib.one_char_right()

                    elif(command == "one character left"):
                        wordlib.one_char_left()

                    elif(command == "one word left"):
                        wordlib.one_word_left()

                    elif(command == "one word right"):
                        wordlib.one_word_right()

                    elif(command == "one paragraph up"):
                        wordlib.one_para_up()

                    elif(command == "one paragraph down"):
                        wordlib.one_para_down()

                    elif(command == "one line up"):
                        wordlib.one_line_up()

                    elif(command == "one line down"):
                        wordlib.one_line_down()

                    elif(command == "go to end of line"):
                        wordlib.end_of_line()

                    elif(command == "go to beginning of line"):
                        wordlib.beg_of_line()

                    elif(command == "go to end of document"):
                        wordlib.end_of_document()

                    elif(command == "go to beginning of document"):
                        wordlib.beg_of_document()

                    elif(command == "delete one left character"):
                        wordlib.delete_one_char_left()

                    elif(command == "delete one right character"):
                        wordlib.delete_one_char_right()

                    elif(command == "delete one left word"):
                        wordlib.delete_one_word_left()

                    elif(command == "delete one right word"):
                        wordlib.delete_one_word_right()

                    elif(command == 'close msword'):
                        break
                except ValueError:
                    print('ValueError: key is a string, but its length is not 1')
                    tts.say('ValueError: key is a string, but its length is not 1')

            else:
                print('analizer doesnot work, Check its settings')
                tts.say('analizer doesnot work, Check its settings')
        else:
            print('error in google speech recognition')
            tts.say('error in google speech recognition')
    #stop msword
    stopword()
