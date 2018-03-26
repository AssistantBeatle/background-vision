from threading  import Thread
from Speechmanager.speech_manager import speech as sp
#import index
def background():
  while(True):
   print("in background thread\n")
   #x=input("do you want to change\n")
   #if x=="yes":
   #co.activatesystemcommandset()
   command = sp.gstt()
   if command=="listen":


     t=Thread(target=assistant,args="")
     t.start()
     t.join()

def assistant():
    print("in assistant")
    from index import mainloop
    re=mainloop()
    #if(re==-1):
     #   break

    #x=input("do you want to close\n")
    #if x=="yes":
     # break;
print("starting background thread\n")
b=Thread(target=background,args="")
b.start()
b.join()