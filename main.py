# Cyber Security Tactics and Techniques compilation
# Final Project for 

# Credits
# GUI help from https://likegeeks.com/python-gui-examples-tkinter-tutorial/
# https://pypi.org/project/PySimpleGUI/
# https://realpython.com/pysimplegui-python/

#python -m pip install pysimplegui
#

# imports
from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter import Menu
from tkinter import ttk
import PySimpleGUI as sg

# Importing Files Anyone?
# from tkinter import filedialog
# file = filedialog.askopenfilename()
# files = filedialog.askopenfilenames()   # Multiple files at once
# file = filedialog.askopenfilename(filetypes = (("Text files","*.txt"),("all files","*.*")))   # Specify file types
# dir = filedialog.askdirectory()       # ask for directory
# from os import path
# file = filedialog.askopenfilename(initialdir= path.dirname(__file__))     # Setting initial directory for the filedialog
# https://www.tutorialsteacher.com/python/create-gui-using-tkinter-python
# https://www.geeksforgeeks.org/python-create-a-gui-marksheet-using-tkinter/
# https://www.geeksforgeeks.org/python-create-a-gui-marksheet-using-tkinter/
# https://www.geeksforgeeks.org/python-tkinter-tutorial/#applications
# https://www.tutorialspoint.com/python/python_gui_programming.htm
# https://www.python4networkengineers.com/posts/python-intermediate/create_a_tkinter_gui_with_sqlite_backend/

# Function  definitions
def Buttonclicked():
  res = "Welcome to " + txt.get()
  lbl.configure(text= res)
  messagebox.showinfo('Information Processed','No Help Found.')
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
  
  
window = Tk()

window.title("Virtual Memory: A Red-Teaming Repo")
window.geometry('350x200')                                        # Pick standard window size

# Add a Menu
menu = Menu(window)
new_item = Menu(menu)                                             # Disable Tearoff Feature with: new_item = Menu(menu, tearoff=0)
new_item.add_command(label='New')
new_item.add_separator()
new_item.add_command(label='Edit')
menu.add_cascade(label='File', menu=new_item)
window.config(menu=menu)

# Tab control 
#============
# Input for Target info
# Type: SQL, HASH, WebApp, Cracking, etc
# -> SQL: any Target information known, inputs available
#       -> Output list of options for SQL code
# Type: Hash
# -> Type of hash known?
#    -> Guess type. 
#    -> Output tool options
#   

tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Welcome')
lbl1 = Label(tab1, text= 'Tool Selection Helper')                 # Add content to tab
lbl1.grid(column=0, row=0, padx=5, pady=5)                        # Position content inside tab with x-y orientation
#v1 = IntVar()
#v2 = IntVar()
#C1 = Checkbutton(window, text = "Cricket", variable = v1)
##C2 = Checkbutton(window, text = "Tennis", variable = v2)
#C1.place(x=100, y=100)
#C2.place(x=180, y=100)

# Hash Identification/Guessing
# Identify $#$ Hachcat numbers
# salt/pw formats
# hash lengths to hash type guesses
tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text='Hashing')
lbl2 = Label(tab2, text= 'Hash Identification: ')
lbl2.grid(column=0, row=0, padx=5, pady=5)

# Guess the Crypto
# All alpha or alnum? hex, dec, oct?
# Looks like square or other etc.?
# Recommend tool options (or eleminate bad options)
tab3 = ttk.Frame(tab_control)
tab_control.add(tab3, text='Decryption')
lbl3 = Label(tab3, text= 'Enter the encrypted text: ')
lbl3.grid(column=0, row=0, padx=5, pady=5)

# What system is running?
# What input forms are available?
# Test SQL injections to rule out types of SQL databases/versions?
# Recommend tools
tab4 = ttk.Frame(tab_control)
tab_control.add(tab4, text='SQL')
lbl4 = Label(tab4, text= 'SQL vulnerability finder: ')
lbl4.grid(column=0, row=0, padx=5, pady=5)

tab_control.pack(expand=1, fill='both')                           # Pack Makes it visible

# Header 'label'
lbl = Label(window, text="Hello", font=("Arial Bold", 18))
lbl.grid(column=0, row=0)

# Text box example      
txt = Entry(window,width=10)                                      # Add (  state='disabled') to disable txt entry
txt.grid(column=1, row=0)                                           
txt.focus()                                                       # .focus() sets the pointer here automatically when loaded

# Button Example Code
# To Use, or Not to Use
btn = Button(window, text="Click Me", bg="grey", fg="red", command=ButtonClicked)
btn.grid(column=2, row=0)                                         # Column 1 (not 0, else it will obscure header label) 

# Drop down ('Combobox') example
combo = Combobox(window)
combo['values']= (1, 2, 3, 4, 5, "Text")
combo.current(1) #set the selected item
combo.grid(column=0, row=3)
combo.get()

# Check button Example
chk_state = IntVar()
chk_state = BooleanVar()
chk_state.set(True) #set check state
chk = Checkbutton(window, text='Choose', var=chk_state)
chk.grid(column=0, row=5)

chk_state.set(0) #uncheck
chk_state.set(1) #check

# Radio Button example                                            # Different names for every button
selected = IntVar()
rad1 = Radiobutton(window,text='First', value=1, variable=selected)       
rad2 = Radiobutton(window,text='Second', value=2, variable=selected)
rad3 = Radiobutton(window,text='Third', value=3, variable=selected)
rad1.grid(column=0, row=7)
rad2.grid(column=1, row=7)
rad3.grid(column=2, row=7)
radBtn.grid(column=3, row=0)

radBtn = Button(window, text="Click Me", command=RadioClicked)

scrollTxt = scrolledtext.ScrolledText(window,width=40,height=10)
scrollTxt.grid(column=0,row=9)
scrollTxt.insert(INSERT,'A prompt for text')
# scrollTxt.delete(1.0,END)     # To Clear Text

# Spinbox example
var =IntVar()
var.set(36)
spin = Spinbox(window, from_=0, to=100, width=5, textvariable=var)       # Number range and width, specifies default value (36)
spin.grid(column=0,row=9)

window.mainloop()     # Endless loop that maintains the open GUI window
