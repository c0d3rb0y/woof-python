# import all of ye tkinter lands and also ttk
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
# create window 
root = Tk() 
 
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
    print(textbox)

# add button
buton = Button(root, text="Save", command = saveas);
buton.place(x=0,y=275)
# start
text_info.configure(font = Font)
#root.after(1000, gettextloop)
root.mainloop()
