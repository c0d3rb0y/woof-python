# import all of ye tkinter lands and also ttk
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
import time
# create window 
global textbox

root = Tk() 

backupf = open("backupf.howl", "a")
backupf.close()

# stuffs
root.geometry("600x300")
root.minsize(height=560)
root.title("Woof Editor")
root.iconbitmap("dog.ico")
root.resizable(False, False)

# add scrollbar functionallity
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)

Font = ("Bahnschrift Light", 12, "normal")

# add text
text_info = Text(root, yscrollcommand=scrollbar.set, fg="white", bg="#23272A", insertbackground="white")
text_info.pack(fill=BOTH)
#def gettextloop():
#    textbox = text_info.get("1.0",'end-1c')
#    print(textbox)
#    root.after(1000, gettextloop)

def saveas():
    textbox = text_info.get("1.0",'end-1c')
    print("Text to save:", textbox)
    text_info.delete("1.0", "end")
    text_info.insert("1.0", "What is the file's name?\n");
    buton = Button(root, text="Save .howl", command = savetofile);
    buton.place(x=0,y=275)

def savetofile():
    savetext = textbox;
    fname = text_info.get("2.0", 'end-1c')
    print("File name:", fname)
    text_info.delete("1.0", "end")
    text_info.insert("1.0", "Saving...")
    ext = ".howl"
    fname += ext
    print("File to save:",fname)
    sfile = open(fname, "a")
    sfile.write(savetext)
    sfile.close()
    text_info.delete("1.0", "end")
    text_info.insert("1.0", "File saved.")
    text_info.delete("1.0", "end")
    buton = Button(root, text="Save", command = saveas);
    buton.place(x=0,y=275)

def openfile2():
    fname = text_info.get("2.0", 'end-1c')
    ext = ".howl"
    fname += ext
    ofile = open(fname, "r")
    readtext = ofile.read()
    text_info.delete("1.0", "end")
    text_info.insert("1.0", readtext)
    buton2 = Button(root, text="Open", command = openfile);
    buton2.place(x=0,y=250)

def openfile():
    textbox = text_info.get("1.0",'end-1c')
    backupf = open("backupf.howl", "w+")
    backupf.write(textbox);
    backupf.close()
    text_info.delete("1.0", "end")
    text_info.insert("1.0", "What is the file's name?\n");
    buton2 = Button(root, text="Open", command = openfile2);
    buton2.place(x=0,y=250)

# add button
buton = Button(root, text="Save", command = saveas);
buton.place(x=0,y=275)
buton2 = Button(root, text="Open", command = openfile);
buton2.place(x=0,y=250)
# start
text_info.configure(font = Font)
#root.after(1000, gettextloop)
root.mainloop()
