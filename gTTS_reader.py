#import gtts
import os
#from gtts import gTTS
#file=open("english.text","r")
#mytext=file.read().replace("\n"," ")

from gtts import gTTS

mytext = """Hello Everyone!
            I am Pavan's chatbot.
            My name is T-Rex"""

language='en'
output=gTTS(text=mytext, lang=language, slow=False)

# save the file
output.save("output.mp3")

# play the file 
os.system("start output.mp3")
#file.close()