# Cyber Security Tactics and Techniques compilation
# Final Project 

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

# imports
import tkinter
from dbclass.py import *
from functions.py import *
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

# ===================== #
# ==== TAB CONTROL ==== #
# ===================== #
# The options supported by Label() method are:
# anchor, bg, bitmap, bd, cursor, font, fg, height, width, image, justify, relief, padx, pady, textvariable, underline and wraplength.
# options supported by grid() method are:
# column, columnspan, row, rowspan, padx, pady, ipadx, ipady and sticky.
tab_control = ttk.Notebook(window)

tab_control.pack(expand = 1, fill ="both")

tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Tool Box')
tab_control.add(tab2, text='Hashing')
tab_control.pack(expand = 1, fill ="both")
# Position content inside tab with x-y orientation

ttk.Label(tab1, text='Search: ', font=('bold', 12)).grid(column=0, row=0, padx=5, pady=5)
searchFor = StringVar()
searchFor.set("Feeling lucky?")
search_entry = Entry(tab1, textvariable=searchFor)
search_entry.grid(row=0, column=1)

# ============================== #
# ==== TAB ONE: TOOL SEARCH ==== #
# ============================== #
ttk.Label(tab1, text="Own System(s): ", font=('bold', 10)).grid(column=0, row=1, padx=5, pady=5)

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
ttk.Label(tab1, text="Target System(s): ", font=('bold', 10)).grid(column=0, row=4, padx=5, pady=5)

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
ttk.Label(tab1, text="Problem Category: ", font=('bold', 10)).grid(column=0, row=6, padx=5, pady=5)
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

frame_tools = ttk.Frame(tab1)
frame_tools.grid(row=11, column=0, pady=20, padx=20, columnspan=4)

columns = ['Type', 'Name', 'OS', 'Notes']
tools_tree_view = Treeview(frame_tools, columns=columns, show="headings")
tools_tree_view.column("Type", width=40)
tools_tree_view.column("Name", width=40)
tools_tree_view.column("OS", width=70)
tools_tree_view.column("Notes", width=340)
for col in columns[0:]:
    tools_tree_view.heading(col, text=col)
tools_tree_view.bind('<<TreeviewSelect>>', select_tools)
tools_tree_view.pack(side="left", fill="y")
scrollbar = Scrollbar(frame_tools, orient='vertical')
scrollbar.configure(command=tools_tree_view.yview)
scrollbar.pack(side="right", fill="y")
tools_tree_view.config(yscrollcommand=scrollbar.set)

# ==== TOOL DATABASE CONTROLS ==== #
frame_btns = Frame(app)
frame_btns.grid(row=13, column=0)

add_btn = Button(frame_btns, text='Add Tool', width=12, command=add_tool)
add_btn.grid(row=0, column=0, pady=20)

remove_btn = Button(frame_btns, text='Remove Tool', width=12, command=remove_tool)
remove_btn.grid(row=0, column=1)

update_btn = Button(frame_btns, text='Update Tool', width=12, command=update_tool)
update_btn.grid(row=0, column=2)

clear_btn = Button(frame_btns, text='Clear Input', width=12, command=clear_text)
clear_btn.grid(row=0, column=3)

search_btn = Button(frame_search, text='Search', width=12, command=search_toolName)
search_btn.grid(row=0, column=2)

search_query_btn = Button(frame_search, text='Search Query', width=12, command=execute_query)
search_query_btn.grid(row=1, column=2)

# ========================= #
# ==== TAB TWO: HASHES ==== #
# ========================= #
# Identify $#$ Hachcat numbers
# salt/pw formats
# hash lengths to hash type guesses
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

# ============================= #
# ====  TAB THREE: CRYPTO  ==== #
# ============================= #
# All alpha or alnum? hex, dec, oct?
# Looks like square or other etc.?
# Recommend tool options (or eleminate bad options)
tab3 = ttk.Frame(tab_control)
tab_control.add(tab3, text='Decryption')
lbl3 = Label(tab3, text='Enter the encrypted text: ').grid(column=0, row=0, padx=5, pady=5)

# ========================= #
# ====  TAB FOUR: SQL  ==== #
# ========================= #
# What input forms are available?
# Test SQL injections to rule out types of SQL databases/versions?
# Recommend tools
tab4 = ttk.Frame(tab_control)
tab_control.add(tab4, text='SQL')
lbl4 = Label(tab4, text='SQL vulnerability finder: ').grid(column=0, row=0, padx=5, pady=5)

# Populate data
populate_list()

#==================#
#==== MAINLOOP ====#
#==================#
window.mainloop()  # Endless loop that maintains the open GUI window



