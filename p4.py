import os
import pytesseract
import gtts
import image
import tempfile
import subprocess



def image():
	os.system(home/cl218/bharat/+"1.jpg")
lang = "english"
f=open("ourstories.txt",'r')
spell = gtts.gTTS(f.read())

spell.save("welcome.mp3")
os.system("mpg321 welcome.mp3")
def ocr(path):
    temp = tempfile.NamedTemporaryFile(delete=False)

    process = subprocess.Popen(['tesseract', path, temp.name], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    process.communicate()

    with open(temp.name + '.txt', 'r') as handle:
        contents = handle.read()

    os.remove(temp.name + '.txt')
    os.remove(temp.name)

    return contents

str = ocr('/home/cl218/Desktop/d.jpeg')
print(str)