# Cyber Security Tactics and Techniques compilation
# Final Project for

# Credits
# GUI help from https://likegeeks.com/python-gui-examples-tkinter-tutorial/
# https://pypi.org/project/PySimpleGUI/
# https://realpython.com/pysimplegui-python/
# https://www.tutorialsteacher.com/python/create-gui-using-tkinter-python
# https://www.geeksforgeeks.org/python-create-a-gui-marksheet-using-tkinter/
# https://www.geeksforgeeks.org/python-tkinter-tutorial/#applications
# https://www.tutorialspoint.com/python/python_gui_programming.htm
# https://www.python4networkengineers.com/posts/python-intermediate/create_a_tkinter_gui_with_sqlite_backend/
# https://www.dbsofts.com/articles/ms_excel_to_sqlite/     ESF Database Migration Toolkit: DMToolkit
# or https://www.sqlitetutorial.net/sqlite-import-csv/

# python -m pip install pysimplegui
#

# imports
import tkinter
from tkinter import *
from tkinter import Menu
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter.ttk import Treeview
from tkinter import ttk  # Contains Notebook
# import PySimpleGUI as sg


# Importing Files Anyone?
# from tkinter import filedialog
# file = filedialog.askopenfilename()
# files = filedialog.askopenfilenames()   # Multiple files at once
# file = filedialog.askopenfilename(filetypes = (("Text files","*.txt"),("all files","*.*")))   # Specify file types
# dir = filedialog.askdirectory()       # ask for directory
# from os import path
# file = filedialog.askopenfilename(initialdir= path.dirname(__file__))     # Setting initial directory for the filedialog

# Function  definitions
def ButtonClicked():
    res = "Welcome to " + txt.get()
    lbl.configure(text=res)
    messagebox.showinfo('Information Processed', 'No Help Found.')
    # messagebox.showwarning('Message title', 'Message content')    # Maybe...
    # messagebox.showerror('Message title', 'Message content')      # Maaaaybe...
    # lbl.configure(text="Button was clicked !!")
    # res = messagebox.askquestion('Message title','Message content')
    # res = messagebox.askyesno('Message title','Message content')
    # res = messagebox.askyesnocancel('Message title','Message content')
    # res = messagebox.askokcancel('Message title','Message content')
    # res = messagebox.askretrycancel('Message title','Message content')


def RadioClicked():
    # Add actions here
    print(selected.get())


# Creat the main window; set title and size
window = Tk()
window.title("Virtual Memory: A Red-Teaming Repo")
window.geometry('550x800')  # Pick standard window size

# Add a Menu
menu = Menu(window)
new_item = Menu(menu)  # Disable Tearoff Feature with: new_item = Menu(menu, tearoff=0)
new_item.add_command(label='New')
new_item.add_separator()
new_item.add_command(label='Edit')
menu.add_cascade(label='File', menu=new_item)
window.config(menu=menu)

# =============
# Tab control
# =============
# The options supported by Label() method are:
# anchor, bg, bitmap, bd, cursor, font, fg, height, width, image, justify, relief, padx, pady, textvariable, underline and wraplength.
# options supported by grid() method are:
# column, columnspan, row, rowspan, padx, pady, ipadx, ipady and sticky.
tab_control = ttk.Notebook(window)

tab_control.pack(expand = 1, fill ="both")

tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Tool Box')
tab_control.pack(expand = 1, fill ="both")
# Position content inside tab with x-y orientation

ttk.Label(tab1, text='Tool Selection Helper').grid(column=0, row=0, padx=5, pady=5)

# ==== Tab 1 Widgets ====#
# OS Select
ttk.Label(tab1, text="Own System(s): ").grid(column=0, row=1, padx=5, pady=5)

v0 = IntVar()
v1 = IntVar()
v2 = IntVar()
v3 = IntVar()
OS0 = Checkbutton(tab1, text="Windows", variable=v1, onvalue=1, offvalue=0)
OS1 = Checkbutton(tab1, text="Linux", variable=v2, onvalue=2, offvalue=3)
OS2 = Checkbutton(tab1, text="iOS", variable=v3, onvalue=4, offvalue=5)
OS3 = Checkbutton(tab1, text="Other", variable=v0, onvalue=6, offvalue=7)
OS0.grid(column=0, row=3, padx=5, pady=5)
OS1.grid(column=1, row=3, padx=5, pady=5)
OS2.grid(column=2, row=3, padx=5, pady=5)
OS3.grid(column=3, row=3, padx=5, pady=5)
'''
OS0.place(x=75, y=100)
OS1.place(x=150, y=100)
OS2.place(x=225, y=100)
OS3.place(x=300, y=100)
'''

# OS Select
ttk.Label(tab1, text="Target System(s): ").grid(column=0, row=4, padx=5, pady=5)

v0_tar = IntVar()
v1_tar = IntVar()
v2_tar = IntVar()
v3_tar = IntVar()
OS4 = Checkbutton(tab1, text="Windows", variable=v1_tar, onvalue=1, offvalue=0)
OS5 = Checkbutton(tab1, text="Linux", variable=v2_tar, onvalue=1, offvalue=0)
OS6 = Checkbutton(tab1, text="iOS", variable=v3_tar, onvalue=1, offvalue=0)
OS7 = Checkbutton(tab1, text="Other", variable=v0_tar, onvalue=1, offvalue=0)
OS4.grid(column=0, row=5, padx=5, pady=5)
OS5.grid(column=1, row=5, padx=5, pady=5)
OS6.grid(column=2, row=5, padx=5, pady=5)
OS7.grid(column=3, row=5, padx=5, pady=5)

# Vulnerability Category
ttk.Label(tab1, text="Problem Category: ").grid(column=0, row=6, padx=5, pady=5)
c0 = IntVar()
c1 = IntVar()
c2 = IntVar()
c3 = IntVar()
c4 = IntVar()
c5 = IntVar()
c6 = IntVar()
c7 = IntVar()
c8 = IntVar()
c9 = IntVar()
c10 = IntVar()
Cat0 = Checkbutton(tab1, text="Open Source", variable=c0, onvalue=1, offvalue=0)
Cat1 = Checkbutton(tab1, text="Decryption", variable=c1, onvalue=1, offvalue=0)
Cat2 = Checkbutton(tab1, text="Hash Cracking", variable=c2, onvalue=1, offvalue=0)
Cat3 = Checkbutton(tab1, text="SQL Injection", variable=c3, onvalue=1, offvalue=0)
Cat4 = Checkbutton(tab1, text="Steganography", variable=c4, onvalue=1, offvalue=0)
Cat5 = Checkbutton(tab1, text="Decryption", variable=c5, onvalue=1, offvalue=0)
Cat6 = Checkbutton(tab1, text="Log/Traffic Analysis", variable=c6, onvalue=1, offvalue=0)
Cat7 = Checkbutton(tab1, text="WiFi", variable=c7, onvalue=1, offvalue=0)
Cat8 = Checkbutton(tab1, text="Web Apps", variable=c8, onvalue=1, offvalue=0)
Cat9 = Checkbutton(tab1, text="Scan, Enum. Exploit", variable=c9, onvalue=1, offvalue=0)
Cat10 = Checkbutton(tab1, text="Forensics/Reverse Eng.", variable=c10, onvalue=1, offvalue=0)

Cat0.grid(column=0, row=7, padx=5, pady=5)
Cat1.grid(column=1, row=7, padx=5, pady=5)
Cat2.grid(column=2, row=7, padx=5, pady=5)
Cat3.grid(column=3, row=7, padx=5, pady=5)
Cat4.grid(column=0, row=8, padx=5, pady=5)
Cat5.grid(column=1, row=8, padx=5, pady=5)
Cat6.grid(column=2, row=8, padx=5, pady=5)
Cat7.grid(column=3, row=8, padx=5, pady=5)
Cat8.grid(column=0, row=9, padx=5, pady=5)
Cat9.grid(column=1, row=9, padx=5, pady=5)
Cat10.grid(column=2, row=9, padx=5, pady=5)

# ==== Hash Identification/Guessing ====#
# Identify $#$ Hachcat numbers
# salt/pw formats
# hash lengths to hash type guesses
# ==== Tab Two Widgets ====#
tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text='Hashing')
ttk.Label(tab2, text='Hash Identification: ').grid(column=0, row=0, padx=5, pady=5)

# ===== Tab Two Layout =====#  Text Box Entry layout option
'''
Label1Tab1.grid(row=0, column=0, padx=15, pady=15)
Entry1Tab1.grid(row=0, column=1, padx=15, pady=15)

familyLabelTab1.grid(row=1, column=0, padx=15, pady=15)
familyEntryTab1.grid(row=1, column=1, padx=15, pady=15)

jobLabelTabOne.grid(row=2, column=0, padx=15, pady=15)
jobEntryTabOne.grid(row=2, column=1, padx=15, pady=15)

imgLabelTabOne.grid(row=0, column=2, rowspan=3, padx=15, pady=15)
'''

# ==== Guess the Crypto ====#
# All alpha or alnum? hex, dec, oct?
# Looks like square or other etc.?
# Recommend tool options (or eleminate bad options)
tab3 = ttk.Frame(tab_control)
tab_control.add(tab3, text='Decryption')
lbl3 = Label(tab3, text='Enter the encrypted text: ').grid(column=0, row=0, padx=5, pady=5)

# ==== What system is running? ====#
# What input forms are available?
# Test SQL injections to rule out types of SQL databases/versions?
# Recommend tools
tab4 = ttk.Frame(tab_control)
tab_control.add(tab4, text='SQL')
lbl4 = Label(tab4, text='SQL vulnerability finder: ').grid(column=0, row=0, padx=5, pady=5)

'''
# Header 'label'
lbl = Label(window, text="Hello", font=("Arial Bold", 18)).grid(column=0, row=0)

# Text box example
txt = Entry(window, width=10).grid(column=1, row=0)  # Add (  state='disabled') to disable txt entry
#txt.focus()  # .focus() sets the pointer here automatically when loaded


# Button Example Code
# To Use, or Not to Use
btn = Button(window, text="Click Me", bg="grey", fg="red", command=ButtonClicked).grid(column=2, row=0)

# Drop down ('Combobox') example
combo = tk.ttk.Combobox(window)
combo['values'] = (1, 2, 3, 4, 5, "Text")
combo.current(1)  # set the selected item
combo.grid(column=0, row=3)
combo.get()

# Check button Example
chk_state = IntVar()
chk_state = BooleanVar()
chk_state.set(True)  # set check state
chk = Checkbutton(window, text='Choose', var=chk_state)
chk.grid(column=0, row=5)

chk_state.set(0)  # uncheck
chk_state.set(1)  # check

# Radio Button example                                            # Different names for every button
selected = IntVar()
rad1 = Radiobutton(window, text='First', value=1, variable=selected)
rad2 = Radiobutton(window, text='Second', value=2, variable=selected)
rad3 = Radiobutton(window, text='Third', value=3, variable=selected)
radBtn = Button(window, text="Click Me", command=RadioClicked)
rad1.grid(column=0, row=7)
rad2.grid(column=1, row=7)
rad3.grid(column=2, row=7)
radBtn.grid(column=3, row=0)

scrollTxt = scrolledtext.ScrolledText(window, width=40, height=10)
scrollTxt.grid(column=0, row=9)
scrollTxt.insert(INSERT, 'A prompt for text')
# scrollTxt.delete(1.0,END)     # To Clear Text

# Spinbox example
var = IntVar()
var.set(36)
spin = Spinbox(window, from_=0, to=100, width=5,
               textvariable=var)  # Number range and width, specifies default value (36)
spin.grid(column=0, row=9)

#tab_control.pack(expand=1, fill='both')  # Pack Makes it visible
'''

window.mainloop()  # Endless loop that maintains the open GUI window

'''
class App():                      # https://stackoverflow.com/questions/58078771/tkinter-how-to-create-a-tab-and-move-content-to-it  :AD WAN
    def __init__(self,master):
        #Frames
        # Make the notebook
        nb = ttk.Notebook(root)
        nb.pack()

        # Make 1st tab
        right_frame = Frame(nb,)
        # Add the tab
        nb.add(right_frame, text="First tab")

        # Make 2nd tab
        left_frame = Frame(nb)
        # Add 2nd tab
        nb.add(left_frame, text="Second tab")

        nb.select(left_frame)

        nb.enable_traversal()

        var1 = IntVar()
        var1a = IntVar()

        #Displaying checkboxes and assigning to variables
        self.Checkbox = Checkbutton(right_frame, text="Ingredients present in full (any allergens in bold with allergen warning if necessary)", variable=var1)
        self.Checkbox.grid(column = 1, row = 1, sticky = W)
        self.Checkbox2 = Checkbutton(right_frame, variable = var1a)
        self.Checkbox2.grid(column = 0, row = 1, sticky = W)

       ###FRAME 2###
        #widgets
        self.msg1 = Label(left_frame, text = "Choose here")
        self.msg1.grid(column = 0, row = 0)


        # THIS IS THE THIRD FRAME
        self.bottomframe = Frame(master, bg="red", width=400, height=200)
        self.bottomframe.pack(side=BOTTOM, fill=BOTH)

        self.label3 = Label(self.bottomframe, text="THIS IS THE THIRD FRAME")
        # self.label3.grid(column=0, row=0)
        self.label3.pack()            


root = Tk()
root.minsize(890, 400)
root.title("test only")
app = App(root)
root.mainloop()
'''

