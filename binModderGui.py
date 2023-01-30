import os
import binmodder as bm
import bindetect as bd
from tkinter import *
from tkinter import scrolledtext
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from ctypes import windll
#fix blurry text
import tkinter as tk
from tkinter import ttk
windll.shcore.SetProcessDpiAwareness(1)

#Window Settings
root = tk.Tk()
root.geometry('1000x550+50+50')
root.title("binmodder by Kroete")
root.resizable(False,False)

#tk Vars
myString =tk.StringVar(root)
googleTransVar = tk.BooleanVar(root)
binPath = tk.StringVar(root)
txtPath = tk.StringVar(root)
txtPathRep = tk.StringVar(root)
stringAdded = False

#callbacks

def binmodCallback():
    if googleTransVar.get() == True:
        with open(txtPath.get(), 'r') as f:
            txtContent = f.read()
            bm.placeStringLength(binPath.get(), bm.replaceBinStrings(binFile=binPath.get(), 
                                    binStringsArray=bm.separateStrings(txtContent), 
                                    stringReplacements=bm.separateStrings(bm.breakStrings(txtContent)), 
                                    returnReplacements=True))
        f.close()
    else:
        with open(txtPath.get(), 'r') as f:
            txtContent = f.read()
            with open(txtPathRep.get(), 'r') as rep:
                txtContentRep = rep.read()
                bm.placeStringLength(binPath.get(), bm.replaceBinStrings(binFile=binPath.get(), 
                binStringsArray=bm.separateStrings(txtContent), 
                stringReplacements=bm.separateStrings(txtContentRep)))
    showinfo(
        title="Done!",
        message="Done!"
    )

def gof2transCheck():
    if googleTransVar.get() == True:
        open_button3.configure(state='disable')
    elif googleTransVar.get() == False:
        open_button3.configure(state='enable')
        textBoxRep.delete(1.0, END)
    
def detect():
    if binPath.get() == '':
        showinfo(
            title='Error',
            message='No .bin file has been selected'
        )

#entry box and Submit button
text1 = tk.Label(
    root,
    text=".bin file:"
)

selectedBin = tk.Label(
    root,
    text="None",
    anchor='w'
)

def select_bin():
    filetypes = (
        ('binary file', '*.bin'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)

    showinfo(
        title='Selected File',
        message=filename
    )

    selectedBin.config(text = os.path.basename(filename))
    global binPath
    binPath.set(filename)

open_button = ttk.Button(
    root,
    text='Choose .bin file',
    command=select_bin
)

text1.grid(row=1, column=3, sticky='w')
selectedBin.grid(row=2, column=3, sticky='w')
open_button.grid(row=3, column=3, sticky='w')


#txt button 1
text1 = tk.Label(
    root,
    text="Strings file:"
)

def select_txt():
    filetypes = (
        ('Text file', '*.txt'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)

    showinfo(
        title='Selected File',
        message=filename
    )

    global txtPath
    txtPath.set(filename)
    textBox.delete(1.0,END)
    
    with open(filename, 'r') as f:
        textBox.configure(state='normal')
        textBox.insert(INSERT, f.read())
        textBox.configure(state='disabled')
    f.close()

open_button2 = ttk.Button(
    root,
    text='Choose strings to be replaced',
    command=select_txt
)

textBox = scrolledtext.ScrolledText(root, height=10, width=35, state='normal')

text1.grid(row=1, column=0, sticky='w')
open_button2.grid(row=2, column=0, sticky='w')

#txt button 2
text2 = tk.Label(
    root,
    text="Replacements file:"
)


def select_txtrep():
    filetypes = (
        ('Text file', '*.txt'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)

    showinfo(
        title='Selected File',
        message=filename
    )

    global txtPathRep
    txtPathRep.set(filename)
    textBoxRep.delete(1.0,END)
    selectedTextRep.configure(text=os.path.basename(filename))

    with open(filename, 'r') as f:
        textBoxRep.configure(state='normal')
        textBoxRep.insert(INSERT, f.read())
        textBoxRep.configure(state='disabled')
    f.close()

open_button3 = ttk.Button(
    root,
    text='Choose replacements',
    command=select_txtrep
)

selectedTextRep = ttk.Label(
    root,
    text="None",
    anchor='w'
)

text2.grid(row=4, column=0, sticky='w')
open_button3.grid(row=6, column=0, sticky='w')
selectedTextRep.grid(row=5, column = 0, sticky='w')

textBoxRep = scrolledtext.ScrolledText(root, height=10, width=35, state='normal')


textBox.grid(row=1, column=2, rowspan=3)
textBoxRep.grid(row=4, column=2, rowspan=3)


#googletrans checkbox
gtCheck = ttk.Checkbutton(
    root,
    text = "Enable gof2translate",
    variable = googleTransVar,
    onvalue=True,
    offvalue=False,
    command=gof2transCheck
)

button2 = tk.Button(
    root,
    text='Replace',
    command=binmodCallback
)

detectButton = ttk.Button(
    root,
    text='Detect Strings',
    command=detect
)

gtCheck.grid(row=4, column=3, sticky='w')
detectButton.grid(row=5, column=3, sticky='w')
button2.grid(row=6, column=3, sticky='w')

root.mainloop()

