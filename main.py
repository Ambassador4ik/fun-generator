import translator as tr
import generator as g
import pyperclip
import tkinter as tk
import tkinter.scrolledtext as st
from tkinter import messagebox
from tkinter import *


def info():
    messagebox.showinfo('Info', 'Fun Generator by Ambassador4ik \nVersion 0.0.1')


def clear():
    text.delete(1.0, END)


def gen():
    text.delete(1.0, END)
    global line
    global translated_line
    line = g.generate()
    translated_line = tr.translate(line)
    text.insert(tk.INSERT, translated_line)


def shuffle():
    text.delete(1.0, END)
    global line
    global translated_line
    translated_line = tr.translate(g.shuffle(line))
    text.insert(tk.INSERT, translated_line)


def update():
    text.delete(1.0, END)
    global line
    global translated_line
    translated_line = tr.translate(g.update(line))
    text.insert(tk.INSERT, translated_line)


def grab_text():
    global translated_line
    pyperclip.copy(translated_line)


line = ''
translated_line = ''

window = tk.Tk()
window.title('Fun Generator by Ambassador4ik')
window.geometry('600x400+400+300')
window.resizable(False, False)
window.config(bg='#ffffff')

text = st.ScrolledText(window, width=80, height=17, font=("Calibri", 11), wrap=WORD, bg='#dbfaff')
text.place(x=10, y=10)

gen_button = Button(window, text="Generate", width=10, command=gen)
gen_button.place(x=10, y=330)

shuffle_button = Button(window, text="Shuffle", width=10, command=shuffle)
shuffle_button.place(x=110, y=330)

seed_button = Button(window, text="Update", width=10, command=update)
seed_button.place(x=210, y=330)

clear_button = Button(window, text="Clear", width=10, command=clear)
clear_button.place(anchor=NE, x=390, y=330)

grab_text_button = Button(window, text="Grab Text", width=10, command=grab_text)
grab_text_button.place(anchor=NE, x=490, y=330)

info_button = Button(window, text="Info", width=10, command=info)
info_button.place(anchor=NE, x=590, y=330)

window.mainloop()
