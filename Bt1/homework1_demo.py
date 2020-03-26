import tkinter as tk
from tkinter import messagebox
import os
import threading
import pyaudio
import wave
import nltk
import argparse
from nltk import word_tokenize,sent_tokenize


arr = [] # this is the array store the tokenized senteced from the text
def open_file(file_name): #add a flag value for to consider making an array or not later on
    f = open(file_name,"r")
    f1 = f.readlines()
    #reading papper in as file then you tokenize to split sentence
    #add sentence to the list arr
    for x in f1:
        a_list = nltk.tokenize.sent_tokenize(x)
        arr.extend(a_list)

def Read(): #This function is used to token
    parser = argparse.ArgumentParser()
    parser.add_argument("filename" , help = "this will read some file", type = str)

    args = parser.parse_args()
    if args.filename:
        open_file(args.filename)
        # print(arr)
#todo:make a button to get the text
class Record():
    isrecording = False #flag for recording
    index = 0 
    #this index is to count the avaible sentences
    #upon reach arr.end() this will help make the program stop
    chunk = 1024 
    sample_format = pyaudio.paInt16 
    channels = 2
    fs = 44100  
    filename = "" #this to record self.file 
###notice if you don't include the self, all the variance is undefined


    frames = [] #this array store ongoing record voice
    def __init__(self, master):
        self.isrecording = False
        self.button1 = tk.Button(main, text='Start Recording',command=self.startrecording)
        self.button2 = tk.Button(main, text='Save Record',command=self.stoprecording)
        self.button3 = tk.Button(main, text='Delete Previou Record',command=self.destroyprevprogress)
        self.button4 = tk.Button(main, text='Stop Recording',command=self.destroyprogress)
        self.button1.pack()
        self.button2.pack()
        self.button3.pack()
        self.button4.pack()

    def startrecording(self):
        self.isrecording = True
        if self.isrecording: 
            self.p = pyaudio.PyAudio()  
            self.stream = self.p.open(format=self.sample_format,channels=self.channels,rate=self.fs,frames_per_buffer=self.chunk,input=True)
            # print('Recording')
            ########
            t = threading.Thread(target=self.record)
            t.start()
            ###move the threading up before the messagebox 
            ###else get a nasty error
            if(self.index < len(arr)):
                # print(arr[self.index])
                messagebox.showinfo("Record Status", "The sentence" + "\n" + arr[self.index])
            else:
                messagebox.showinfo("Record Status", "There is nothing left to record")
            self.index += 1
            print(self.index)
            ######

    def stoprecording(self):
        if self.isrecording:
            self.isrecording = False
            # print('Recording complete!')
            self.filename = "sentence" + str(self.index) + ".wav"
            # creating wav file
            wf = wave.open(self.filename, 'wb')
            wf.setnchannels(self.channels)
            wf.setsampwidth(self.p.get_sample_size(self.sample_format))
            wf.setframerate(self.fs)
            wf.writeframes(b''.join(self.frames))
            wf.close()
            self.frames.clear() 
            # to clear the frame array and kill the previous record
            # with out destroying the entire record progress
            # print("Recorded file: " + self.filename) 
            if(self.index == len(arr)):
                main.destroy()
                messagebox.showinfo("Record Status", "Recording complete! \n Recorded file: " + self.filename \
                    + "\n This is the last record in the file")
                print("This is the last sentence of the file")
            else:
                messagebox.showinfo("Record Status", "Recording complete! \n Recorded file: " + self.filename)

        else:
                messagebox.showinfo("Record Status", "No record avaible")

    def destroyprevprogress(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)
            messagebox.showinfo("Record Status", "Deleted recorded file: " + self.filename)
            self.filename = ""
            self.index -= 1
        else:
            messagebox.showinfo("Record Status", "No file to delete")

    def destroyprogress(self): # make another function and button to destroy progress
        main.destroy()

    def record(self):
        while self.isrecording:
            data = self.stream.read(self.chunk)
            self.frames.append(data)
		
Read() 
## reading file function
## this function implemented argument
## make you input paper file
main = tk.Tk()
main.title('recorder')
main.geometry('500x200')
app = Record(main)


main.mainloop() # repeat until stop record
