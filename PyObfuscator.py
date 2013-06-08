#!/usr/bin/env python

from Tkinter import *
import Tkinter
import tkMessageBox
import base64
import tkFileDialog

root = Tkinter.Tk()
root.geometry("400x300")

#Custom functions here
def encode():
    location1 = tkFileDialog.askopenfile(mode = "r")
    data1 = location1.read()
    save1 = tkFileDialog.asksaveasfile(mode = "w")
    save1.write(base64.standard_b64encode(data1))
    save1.close()

def decode():
    location2 = tkFileDialog.askopenfile(mode = "r")
    data2 = location2.read()
    save2 = tkFileDialog.asksaveasfile(mode = "w")
    save2.write(base64.standard_b64decode(data2))
    save2.close()

#labels here
label_1 = Label(root,text = "Obfuscate Python file here:")
label_2 = Label(root, text = "Decrypt Python file here:")

#buttons here
button_1 = Button(text = "Obfuscate Python file", command = encode)
button_2 = Button(text = "Decrypt Python file", command = decode)


button_1.pack()
button_1.place(x = 150, y = 40)
button_2.pack()
button_2.place(x = 140, y = 100)
label_1.pack()
label_1.place(x = 0, y = 40)
label_2.pack()
label_2.place(x = 0, y = 100)

root.mainloop()
