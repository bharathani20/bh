import os
import pytesseract
import gtts
import image

def image():
	os.system(home/cl218/bharat/+"1.jpg")
lang = "english"
f=open("ourstories.txt",'r')
spell = gtts.gTTS(f.read())

spell.save("welcome.mp3")
os.system("mpg321 welcome.mp3")