
import numpy as np
import random
from tkinter import *






all = ' !"#$%&\()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~'





def find_cypher():
    message = entry_message.get()
    len_m = len(message)
    
    f = np.random.randint(95, size = (len_m))

    j = 0
    cipher = [' '] * len_m 
    for i in f:
        cipher[j] = all[i]
        j += 1
    s = ""
    cypher = s.join(cipher)
    k= find_key(len_m, cipher, message)
    
    listbox.insert(2, cypher)
    
    return k, cypher
    
    



def find_key(len_m, cipher, message):
    j = 0
    k = np.zeros(len_m)
    for i in cipher:
        k[j] =  all.index(message[j]) - all.index(cipher[j])
        j = j + 1
    
    listbox.insert(1, str(k))
    return k




def print_option():
    global a
    if var1.get() == 1:
        a = 'a'
    elif var2.get() == 1:
        a = 'w'
    
    
    






def submit():
    
    
    filename = entry_file.get()
    file = filename + '.txt'

    fid = open(file, a)
    
    
    name = entry1.get()
    fid.write(f'\n{name}')
    full = listbox.get(0, END)
    fid.write('\n'+full[0])
    fid.write('\n'+full[1])
    fid.close()


   





def listbox_clear():
    listbox.delete(0, 'end')

    


window = Tk()

kvar = StringVar()
civar = StringVar()



listbox = Listbox(window, height = 2, width = 50, xscrollcommand=True, listvariable= kvar)
listbox.grid(row= 5, column = 1, pady = 20)



window_label = Label(text ="Name", font = 'FBI')
window_label.grid(row = 0, column = 0, padx = 20, pady = 20)

window_label = Label(text ="File", font = 'FBI')
window_label.grid(row = 0, column = 2)


window.title("Encrypter")
window.geometry("600x300")


entry1 = Entry(window)
entry1.grid(row = 0, column = 1)

entry_file = Entry(window)
entry_file.grid(row = 0, column = 3)


entry_message = Entry(window, width = 50, xscrollcommand=True)
entry_message.grid(row = 2, column =1, pady = 10)





message_label = Label(text = "Message", font= 'FBI')
message_label.grid(row = 2, column = 0)


button1 = Button(window, text="Save", command = lambda: submit())
button1.grid(row = 3, column = 2)


button_close = Button(window, text = "Close", command = window.destroy)
button_close.grid(row = 3, column = 3)

button_encrypt = Button(window, text = "Encrypt", command = lambda: find_cypher())
button_encrypt.grid(row = 3, column = 1)

button_clear = Button(window, text = "Clear", command = listbox_clear)
button_clear.grid(row = 6, column = 1)


var1 = IntVar()
var2 = IntVar()

check_print_app = Checkbutton(window, text = 'append', variable = var1, command=print_option)
check_print_app.grid(row = 1, column = 2)
check_print_new = Checkbutton(window, text = 'new file', variable = var2, command=print_option)
check_print_new.grid(row = 1, column = 3)

window.mainloop()


