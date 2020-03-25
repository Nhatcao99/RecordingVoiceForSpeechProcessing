import tkinter as tk
import threading
import pyaudio
import wave
import nltk
import argparse
from nltk import word_tokenize,sent_tokenize


arr = [] # this is the array store the tokenized senteced from the text
index  = 0
def open_file(file_name): #add a flag value for to consider making an array or not later on
    f = open(file_name,"r")
    f1 = f.readlines()
    # nltk.download('punkt')
    for x in f1:
        arr.extend(list(sent_tokenize(x)))

def Read(): #This function is used to token
    parser = argparse.ArgumentParser()
    parser.add_argument("filename" , help = "this will read some file", type = str)

    args = parser.parse_args()
    if args.filename:
        open_file(args.filename)
        # print(arr)
#todo:make a button to get the text
class Record():
    index = 0
    chunk = 1024 
    sample_format = pyaudio.paInt16 
    channels = 2
    fs = 44100  
    
    frames = [] 
    def __init__(self, master):
        self.isrecording = False
        self.button1 = tk.Button(main, text='Start Recording',command=self.startrecording)
        self.button2 = tk.Button(main, text='Save Record',command=self.stoprecording)
        self.button3 = tk.Button(main, text='Stop Recording',command=self.destroyprogress)
        self.button1.pack()
        self.button2.pack()
        self.button3.pack()

    def startrecording(self):
        self.p = pyaudio.PyAudio()  
        self.stream = self.p.open(format=self.sample_format,channels=self.channels,rate=self.fs,frames_per_buffer=self.chunk,input=True)
        self.isrecording = True
        print('Recording')
        t = threading.Thread(target=self.record)
        t.start()

    def stoprecording(self):
        self.isrecording = False
        print('recording complete')
        self.filename=input('the filename?')
        self.filename = self.filename+".wav"
        wf = wave.open(self.filename, 'wb')
        wf.setnchannels(self.channels)
        wf.setsampwidth(self.p.get_sample_size(self.sample_format))
        wf.setframerate(self.fs)
        wf.writeframes(b''.join(self.frames))
        wf.close()

    def destroyprogress(self): # make another function and button to destroy progress
        main.destroy()

    def record(self):
        while self.isrecording:
            data = self.stream.read(self.chunk)
            self.frames.append(data)
		
# Read() ## reading file function
main = tk.Tk()
main.title('recorder')
main.geometry('200x50')
app = Record(main)
# if(index < len(arr)):
#     print(arr)
# else:
#     print("Nothing Else to record.")
# index += 1

main.mainloop() # repeat until stop record
