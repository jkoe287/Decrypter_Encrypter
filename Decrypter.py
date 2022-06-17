from tkinter import *
import numpy as np
import random

#Define characters:
all = ' !"#$%&\()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~'

#this function calculates the index of the character in the all array to make the decrytion possible.
def get_index():
    k = key_entry.get()[1:(len(key_entry.get())-1)]

    f = []
    b = k.replace('.', '')
    
    for i in b.split():
        if i.find('-') == 0:
            in_ = i.replace('-', '')
            f.append(-abs(int(in_)))

        else:
            f.append(int(i))

    j = 0
    m = []

    for l in cipher_entry.get():
        m.append(all[f[j] + all.index(cipher_entry.get()[j])])
        j = j + 1
        
    message = ''.join(m)
    j = 1
    for i in range(0, len(message), 49):
        listbox_message.insert(j, message[i:i+49])
        j = j +1

    

#this function clears the listbox
def listbox_clear():
    listbox_message.delete(0, 'end')
    key_entry.delete(0, 'end')
    cipher_entry.delete(0, 'end')






#Window main loop.
app = Tk()

app.title("Decrypter")
app.configure(bg = 'black')
app.geometry('700x400')


key_label = Label(text = 'enter key', font = 'Courier 12', fg = 'white', bg = 'black')
key_label.grid(row = 0, column = 0, padx=30, pady = 20)

key_entry = Entry(fg = 'white',bg = 'black', width = 50, font = 'Courier')
key_entry.grid(row = 0, column = 1)

cipher_label = Label(text = 'enter cipher', font = 'Courier 12', fg = 'white', bg = 'black')
cipher_label.grid(row = 1, column = 0)

cipher_entry = Entry(fg = 'white', bg = 'black', width = 50, font = 'Courier')
cipher_entry.grid(row = 1, column = 1)

button_decrypt = Button(text = 'DECRYPT', bg = 'white', command= get_index) 
button_decrypt.grid(row = 2, column = 1, pady = 20)

listbox_message = Listbox(fg = 'black', font = 'Courier', width = 50, bg = 'white')
listbox_message.grid(row = 3, column = 1 )


button_clear = Button(text = 'CLEAR ALL', bg = 'white', command= listbox_clear)
button_clear.grid(row = 4, column = 1, pady = 20)



app.mainloop()
