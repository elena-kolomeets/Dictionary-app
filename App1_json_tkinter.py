"""This app is an English dictionary
with tkinter GUI based on json data file
It searches for the word given by the user
and suggests 3 similar words if it's not found
Search is available with the GUI button or keyboard 'Enter' button
"""

import json
import difflib
import tkinter as tk
from tkinter import messagebox

dictionary = json.load(open('data.json'))

window = tk.Tk()
window.title('Word definitions')
window.configure(background='white')


def get_word(akey):
    akey = akey.lower()
    if akey in dictionary:
        mylist = []
        for aword in dictionary[akey]:
            mylist.append(aword)
        return mylist
    elif akey.title() in dictionary:
        mylist = []
        for aword in dictionary[akey.title()]:
            mylist.append(aword)
        return mylist
    elif akey.upper() in dictionary:
        mylist = []
        for aword in dictionary[akey.upper()]:
            mylist.append(aword)
        return mylist
    elif len(difflib.get_close_matches(akey, dictionary.keys(), cutoff=0.8)) > 0:
        thekey = difflib.get_close_matches(akey, dictionary.keys(), cutoff=0.8, n=3)
        hint = messagebox.askyesno('Hint', 'Did you mean "%s"?' % thekey[0])
        if hint:
            for aword in dictionary[thekey[0]]:
                return aword
        else:
            if len(thekey) > 1:
                hint = messagebox.askyesno('Hint', 'Did you mean "%s"?' % thekey[1])
                if hint:
                    for aword in dictionary[thekey[1]]:
                        return aword
                else:
                    if len(thekey) > 2:
                        hint = messagebox.askyesno('Hint', 'Did you mean "%s"?' % thekey[2])
                        if hint:
                            for aword in dictionary[thekey[2]]:
                                return aword
                        else:
                            return 'The word does not exist. Please double check it.'
                    else:
                        return 'The word does not exist. Please double check it.'
            else:
                return 'The word does not exist. Please double check it.'
    else:
        return 'The word does not exist. Please double check it.'


def button_click(event=None):
    t1.delete(1.0, tk.END)
    if e1_var.get() != '':
        result = get_word(e1_var.get())
        if isinstance(result, list):
            for word in result:
                t1.insert(tk.END, word+'\n')
        else:
            t1.insert(tk.END, result)
    e1.delete(0, tk.END)


l1 = tk.Label(window, background='white', text='Find definitions of English words and abbreviations with this app',
              font=('Times New Roman', 12))
l1.grid(row=0, column=1)

b1 = tk.Button(window, background='white', text='Search', command=button_click, width=10, font=('Times New Roman', 12))
b1.grid(row=2, column=1, pady=5)
window.bind('<Return>', button_click)


def del_entry(event):
    e1.delete(0, tk.END)
    e1.focus_set()


e1_var = tk.StringVar()
e1 = tk.Entry(window, textvariable=e1_var, width=30)
e1.insert(0, 'Enter a word or abbreviation')
e1.configure(font=('Times New Roman', 12))
e1.bind('<Button-1>', del_entry)
e1.grid(row=1, column=1, pady=5)

t1 = tk.Text(window, height=7, width=50, font=('Times New Roman', 12))
t1.grid(row=3, column=1, pady=5, padx=(5, 0))

s1 = tk.Scrollbar(window)
s1.grid(row=3, column=2, pady=5, padx=(0, 5), ipady=44, sticky=tk.W)

t1.configure(yscrollcommand=s1.set)
s1.configure(command=t1.yview)

window.mainloop()
