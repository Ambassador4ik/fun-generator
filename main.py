import translator as tr
import generator as g
import seed as s
import pyperclip
import tkinter as tk
import tkinter.scrolledtext as st
from tkinter import *


def grab_seed():
    global seed
    pyperclip.copy(seed)


def clear():
    text.delete(1.0, END)
    global line
    global translated_line
    line = ''
    translated_line = ''
    update_seed()


def gen():
    global line
    global translated_line
    global seed
    update_seed()
    text.delete(1.0, END)
    line = g.generate(seed)
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


def update_seed():
    global seed
    seed = seed_entry.get()
    if seed == '':
        seed = s.gen_seed()


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

grab_seed_button = Button(window, text="Grab seed", width=10, command=grab_seed)
grab_seed_button.place(anchor=NE, x=590, y=330)

seed_entry = Entry(window, width=96)
seed_entry.place(x=10, y=365)

seed = seed_entry.get()
if seed == '':
    seed = s.gen_seed()

window.mainloop()
