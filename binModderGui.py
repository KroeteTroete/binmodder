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

#https://stackoverflow.com/a/58009290
class OptionDialog(Toplevel):
    """
        This dialog accepts a list of options.
        If an option is selected, the results property is to that option value
        If the box is closed, the results property is set to zero
    """
    def __init__(self,parent,title,question,options):
        Toplevel.__init__(self,parent)
        self.title(title)
        self.question = question
        self.transient(parent)
        self.protocol("WM_DELETE_WINDOW",self.cancel)
        self.options = options
        self.result = '_'
        self.createWidgets()
        self.grab_set()
        ## wait.window ensures that calling function waits for the window to
        ## close before the result is returned.
        self.wait_window()
    def createWidgets(self):
        frmQuestion = Frame(self)
        Label(frmQuestion,text=self.question).grid()
        frmQuestion.grid(row=1)
        frmButtons = Frame(self)
        frmButtons.grid(row=2)
        column = 0
        for option in self.options:
            btn = Button(frmButtons,text=option,command=lambda x=option:self.setOption(x))
            btn.grid(column=column,row=0)
            column += 1 
    def setOption(self,optionSelected):
        self.result = optionSelected
        self.destroy()
    def cancel(self):
        self.result = None
        self.destroy()


#Window Settings
root = tk.Tk()
root.geometry('1000x550+50+50')
root.title("binmodder by Kroete")
root.resizable(False,False)

#Variables
myString =tk.StringVar(root)
googleTransVar = tk.BooleanVar(root)
binPath = tk.StringVar(root)
txtPath = tk.StringVar(root)
txtPathRep = tk.StringVar(root)
usedBD = False
BDcontent = []
BDcontentList = []


#callbacks

def binmodCallback():
    global usedBD
    print(f"usedBD = {usedBD}")
    print(f"gt = {googleTransVar.get()}")
    if googleTransVar.get()==True and usedBD==False:
        with open(txtPath.get(), 'r') as f:
            txtContent = f.read()
            bm.placeStringLength(binPath.get(), bm.replaceBinStrings(binFile=binPath.get(), 
                                    binStringsArray=bm.separateStrings(txtContent), 
                                    stringReplacements=bm.separateStrings(bm.breakStrings(txtContent)), 
                                    returnReplacements=True))
        f.close()

    elif googleTransVar.get()==False and usedBD==False:
        with open(txtPath.get(), 'r') as f:
            txtContent = f.read()
            with open(txtPathRep.get(), 'r') as rep:
                txtContentRep = rep.read()
                bm.placeStringLength(binPath.get(), bm.replaceBinStrings(binFile=binPath.get(), 
                binStringsArray=bm.separateStrings(txtContent), 
                stringReplacements=bm.separateStrings(txtContentRep)))
            rep.close()
        f.close()

    elif googleTransVar.get()==True and usedBD==True:
        bm.placeStringLength(binPath.get(), bm.replaceBinStrings(binFile=binPath.get(), 
                                    binStringsArray=BDcontentList, 
                                    stringReplacements=bm.separateStrings(bm.breakStrings(BDcontent)), 
                                    returnReplacements=True))

    elif usedBD==True and googleTransVar.get()==False:
        bm.placeStringLength(binPath.get(), bm.replaceBinStrings(binFile=binPath.get(), 
                binStringsArray=BDcontentList, 
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
    global BDcontent
    global BDcontentList
    global usedBD
    if binPath.get() == '':
        showinfo(
            title='Error',
            message='No .bin file has been selected'
        )
    else:
        dlg = OptionDialog(
            root, 
            '.bin type', 
            'Please select a .bin type',
            ['names']) #TODO Add systems and stations bin structures to bindetect and the detect() method
        detectedStringsList = bd.detectStrings(binPath.get(),dlg.result, 'list') 
        detectedStrings = bd.detectStrings(binPath.get(),dlg.result, 'string')     
        textBox.configure(state='normal')
        textBox.insert(INSERT, detectedStrings)
        textBox.configure(state='disabled')
        usedBD = True
        BDcontentList = detectedStringsList
        BDcontent = detectedStrings

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

