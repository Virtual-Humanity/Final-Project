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
# import tkinter
import sqlite3
# from dbclass.py import *
# from functions.py import *
from tkinter import *
from tkinter import Menu
from tkinter import messagebox
# from tkinter import scrolledtext
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
# file = filedialog.askopenfilename(initialdir= path.dirname(__file__))  # Setting initial directory for the filedialog

# ------------------------------------------------------------------
# ---- CLASS -------------------------------------------------------
# ------------------------------------------------------------------
# noinspection PyShadowingNames
class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS tools (tool_id INTEGER PRIMARY KEY, tool_name text, "
            "tool_type text, os integer, free integer, description text, link text, notes text)")
        self.conn.commit()

    def fetch(self, tool_name=''):
        self.cur.execute(
            "SELECT * FROM tools WHERE tool_name LIKE ?", ('%' + tool_name + '%',))
        rows = self.cur.fetchall()
        return rows

    def fetch2(self, query):
        self.cur.execute(query)
        rows = self.cur.fetchall()
        return rows

    def insert(self, tool_name, tool_type, os, free, description, link, notes):
        self.cur.execute("INSERT INTO tools VALUES (NULL, ?, ?, ?, ?, ?, ?, ?)",
                         (tool_name, tool_type, os, free, description, link, notes))
        self.conn.commit()

    def remove(self, tool_id):
        self.cur.execute("DELETE FROM tools WHERE tool_id=?", (tool_id,))
        self.conn.commit()

    def update(self, tool_id, tool_name, tool_type, os, free, description, link, notes):
        self.cur.execute(
            "UPDATE tools SET tool_name = ?, tool_type = ?, os = ?, "
            "free= ?, description = ?, link = ?, notes = ? WHERE tool_id = ?",
            (tool_name, tool_type, os, free, description, link, notes, tool_id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()


db = Database('tools.db')
# db.insert("rtr001", "Cisco", "512", "256")
# db.insert("rtr002", "Cisco", "1024", "256")
# db.insert("rtr003", "Cisco", "2048", "256")
# db.insert("rtr004", "Juniper", "2048", "256")
# db.insert("rtr005", "Huawei", "2048", "256")

# ------------------------------------------------------------------
# ---- DEFINITIONS -------------------------------------------------
# ------------------------------------------------------------------

# def db_open(filename):
#    "Opens and close the database"
#    with lite.connect(filename) as conn:
#        print(f"I created my database named {filename}")

# db = Database('tools.db')


def populate_list(tool_name=''):
    for i in tools_tree_view.get_children():
        tools_tree_view.delete(i)
    for row in db.fetch(tool_name):
        tools_tree_view.insert('', 'end', values=row)


def populate_list2(query='select * from tools'):
    for i in tools_tree_view.get_children():
        tools_tree_view.delete(i)
    for row in db.fetch2(query):
        tools_tree_view.insert('', 'end', values=row)


def add_tool():
    if tool_type_text.get() == '' or tool_name_text.get() == '' or os_text.get() == '' or free_text.get() == '' \
            or description_text.get() == '' or link_text.get() == '' or notes_text.get() == '':
        messagebox.showerror('Required Fields', 'Please include all fields')
        return
    db.insert(tool_name_text.get(), tool_type_text.get(), os_text.get(), free_text.get(), description_text.get(),
              link_text.get(), notes_text.get())
    clear_text()
    populate_list()


def select_tools():
    try:
        global selected_item
        index = tools_tree_view.selection()[0]
        selected_item = tools_tree_view.item(index)['values']
        tool_name_entry.delete(0, END)
        tool_name_entry.insert(END, selected_item[1])
        tool_type_entry.delete(0, END)
        tool_type_entry.insert(END, selected_item[2])
        os_entry.delete(0, END)
        os_entry.insert(END, selected_item[3])
        notes_entry.delete(0, END)
        notes_entry.insert(END, selected_item[4])
    except IndexError:
        pass


def search_by_elements():
    return


def remove_tool():
    db.remove(selected_item[0])
    clear_text()
    populate_list()


def update_tool():
    db.update(selected_item[0], tool_name_text.get(), tool_type_text.get(), os_text.get(), free_text.get(),
              description_text.get(), link_text.get(), notes_text.get())
    populate_list()


def clear_text():
    tool_type_entry.delete(0, END)
    tool_name_entry.delete(0, END)
    os_entry.delete(0, END)
    free_entry.delete(0, END)
    description_entry.delete(0, END)
    link_entry.delete(0, END)
    notes_entry.delete(0, END)


def search_tool_name():
    tool_name = tool_name_search.get()
    populate_list(tool_name)


def execute_query():
    query = query_search.get()
    populate_list2(query)


# ----------------------------------------------------------
# ----------   MAIN   --------------------------------------
# ----------------------------------------------------------

# Create the main window; set title and size
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
# anchor, bg, bitmap, bd, cursor, font, fg, height, width, image, 
# justify, relief, padx, pady, textvariable, underline and wraplength.
# options supported by grid() method are:
# column, columnspan, row, rowspan, padx, pady, ipadx, ipady and sticky.
tab_control = ttk.Notebook(window)

tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control)

tab_control.add(tab1, text='Tool Box')
tab_control.add(tab2, text='Hashing')
tab_control.add(tab3, text='Decryption')
tab_control.add(tab4, text='SQL')

tab_control.pack(expand=1, fill="both")

# ============================== #
# ==== TAB ONE: TOOL SEARCH ==== #
# ============================== #
frame_search = ttk.Frame(tab1)
frame_search.grid(row=0, sticky=W)

lbl_search = ttk.Label(frame_search, text='Search by Name', font=('bold', 12))
lbl_search.grid(row=0, sticky=W, padx=5, pady=5)
tool_name_search = StringVar()
# tool_name_search.set("Hashcat")
tool_name_search_entry = Entry(frame_search, textvariable=tool_name_search)
tool_name_search_entry.grid(row=0, column=1, sticky=E)

search_btn_tn = Button(tool_name_search_entry, text='Search', width=12, command=search_tool_name)
search_btn_tn.grid(row=0, column=2)

# lbl_search = ttk.Label(frame_search, text='Search by Query', font=('bold', 12))
# lbl_search.grid(row=1, sticky=W, padx=5, pady=5)
query_search = StringVar()
# query_search.set("Select * from tools where os=iOS")
# query_search_entry = Entry(frame_search, textvariable=query_search, width=40)
# query_search_entry.grid(row=1, column=1, sticky=E)

# ==== TOOL DATABASE SEARCH FIELDS ==== #
search_fields = Frame(tab1)
search_fields.grid(row=1, column=0, sticky=W)
ttk.Label(search_fields, text="Search by Field: ", font=('bold', 12)).grid(row=0, sticky=W, padx=5, pady=5,
                                                                           columnspan=2)

# NAME
tool_name_text = StringVar()
tool_name_label = Label(search_fields, text='Name', font=('bold', 10))
tool_name_label.grid(row=1, column=0, sticky=E)
tool_name_entry = Entry(search_fields, textvariable=tool_name_text)
tool_name_entry.grid(row=1, column=1, sticky=W)
# TYPE
tool_type_text = StringVar()
tool_type_label = Label(search_fields, text='Type', font=('bold', 10))
tool_type_label.grid(row=1, column=2, sticky=E)
tool_type_entry = Entry(search_fields, textvariable=tool_type_text)
tool_type_entry.grid(row=1, column=3, sticky=W)
# OS
os_text = StringVar()
os_label = Label(search_fields, text='OS', font=('bold', 10))
os_label.grid(row=2, column=0, sticky=E)
os_entry = Entry(search_fields, textvariable=os_text)
os_entry.grid(row=2, column=1, sticky=W)
# NOTES
notes_text = StringVar()
notes_label = Label(search_fields, text='Notes', font=('bold', 10))
notes_label.grid(row=2, column=2, sticky=E)
notes_entry = Entry(search_fields, textvariable=notes_text)
notes_entry.grid(row=2, column=3, sticky=W)
# FREE
free_text = StringVar()
free_label = Label(search_fields, text='Free', font=('bold', 10))
free_label.grid(row=3, column=0, sticky=E)
free_entry = Entry(search_fields, textvariable=free_text)
free_entry.grid(row=3, column=1, sticky=W)
# DESCRIPTION
description_text = StringVar()
description_label = Label(search_fields, text='Description', font=('bold', 10))
description_label.grid(row=3, column=2, sticky=E)
description_entry = Entry(search_fields, textvariable=description_text)
description_entry.grid(row=3, column=3, sticky=W)
# LINK
link_text = StringVar()
link_label = Label(search_fields, text='Link', font=('bold', 10))
link_label.grid(row=4, column=0, sticky=E)
link_entry = Entry(search_fields, textvariable=link_text)
link_entry.grid(row=4, column=1, sticky=W)

search_btns = Frame(tab1)
search_btns.grid(row=3, column=0)
search_btn = Button(text='Search', width=12, command=search_by_elements)
# search_btn.grid(row=0, column=2)

# search_query_btn = Button(search_entry2, text='Search Query', width=12, command=execute_query)
# search_query_btn.grid(row=1, column=2)


# OS Select
os_set = ttk.Frame(tab1)
os_set.grid(row=3, sticky=W)
ttk.Label(os_set, text="System(s) Required: ", font=('bold', 12)).grid(row=0, sticky=W, padx=5, pady=5, columnspan=2)

v0_tar = IntVar()
v1_tar = IntVar()
v2_tar = IntVar()
v3_tar = IntVar()
OS4 = Checkbutton(os_set, text="Windows", font=('bold', 10), variable=v1_tar, onvalue=1, offvalue=0)
OS5 = Checkbutton(os_set, text="Linux", font=('bold', 10), variable=v2_tar, onvalue=1, offvalue=0)
OS6 = Checkbutton(os_set, text="iOS", font=('bold', 10), variable=v3_tar, onvalue=1, offvalue=0)
OS7 = Checkbutton(os_set, text="Other", font=('bold', 10), variable=v0_tar, onvalue=1, offvalue=0)
OS4.grid(column=0, row=1, sticky=W, padx=5, pady=5)
OS5.grid(column=1, row=1, sticky=W, padx=5, pady=5)
OS6.grid(column=2, row=1, sticky=W, padx=5, pady=5)
OS7.grid(column=3, row=1, sticky=W, padx=5, pady=5)
v4_pay = IntVar()
Pay = Checkbutton(os_set, text="Include Paid Products?", font=('bold', 10), variable=v4_pay, onvalue=1, offvalue=0)
Pay.grid(column=0, row=2, columnspan=3, sticky=W, padx=5, pady=5)
# OS0.place(x=75, y=100)

# Vulnerability Category
problem_set = ttk.Frame(tab1)
problem_set.grid(row=4, sticky=W)
ttk.Label(problem_set, text="Problem Category: ", font=('bold', 12)).grid(row=4, sticky=W, columnspan=2, padx=5, pady=5)
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
Cat0 = Checkbutton(problem_set, text="Open Source", variable=c0, onvalue=1, offvalue=0)
Cat1 = Checkbutton(problem_set, text="Decryption", variable=c1, onvalue=1, offvalue=0)
Cat2 = Checkbutton(problem_set, text="Hash Cracking", variable=c2, onvalue=1, offvalue=0)
Cat3 = Checkbutton(problem_set, text="SQL Injection", variable=c3, onvalue=1, offvalue=0)
Cat4 = Checkbutton(problem_set, text="Steganography", variable=c4, onvalue=1, offvalue=0)
Cat5 = Checkbutton(problem_set, text="Decryption", variable=c5, onvalue=1, offvalue=0)
Cat6 = Checkbutton(problem_set, text="Log/Traffic Analysis", variable=c6, onvalue=1, offvalue=0)
Cat7 = Checkbutton(problem_set, text="WiFi", variable=c7, onvalue=1, offvalue=0)
Cat8 = Checkbutton(problem_set, text="Web Apps", variable=c8, onvalue=1, offvalue=0)
Cat9 = Checkbutton(problem_set, text="Scan, Enum. Exploit", variable=c9, onvalue=1, offvalue=0)
Cat10 = Checkbutton(problem_set, text="Forensics/Reverse Eng.", variable=c10, onvalue=1, offvalue=0)

Cat0.grid(column=0, row=7, sticky=W, padx=5, pady=5)
Cat1.grid(column=1, row=7, sticky=W, padx=5, pady=5)
Cat2.grid(column=2, row=7, sticky=W, padx=5, pady=5)
Cat3.grid(column=3, row=7, sticky=W, padx=5, pady=5)
Cat4.grid(column=0, row=8, sticky=W, padx=5, pady=5)
Cat5.grid(column=1, row=8, sticky=W, padx=5, pady=5)
Cat6.grid(column=2, row=8, sticky=W, padx=5, pady=5)
Cat7.grid(column=3, row=8, sticky=W, padx=5, pady=5)
Cat8.grid(column=0, row=9, sticky=W, padx=5, pady=5)
Cat9.grid(column=1, row=9, sticky=W, padx=5, pady=5)
Cat10.grid(column=2, row=9, sticky=W, padx=5, pady=5)

frame_tools = ttk.Frame(tab1)
frame_tools.grid(row=5, column=0, sticky=W, pady=20, padx=20, columnspan=4)

columns = ['Name', 'Uses', 'OS Support', 'Notes']
description_output = StringVar()
link_output = StringVar()
# add one Label
descShow = ttk.Label(frame_tools, textvariable=description_output, width=35)
descShow.grid(row=6, column=0, columnspan=4)
linkShow = ttk.Label(frame_tools, textvariable=link_output, width=35)
linkShow.grid(row=6, column=0, columnspan=4)

tools_tree_view = Treeview(frame_tools, columns=columns, show="headings")
tools_tree_view.column("Name", width=40)
tools_tree_view.column("Uses", width=40)
tools_tree_view.column("OS Support", width=70)
tools_tree_view.column("Notes", width=340)
for col in columns[0:]:
    tools_tree_view.heading(col, text=col)
tools_tree_view.bind('<<TreeviewSelect>>', select_tools)
# tools_tree_view.pack(side="left", fill="y")
scrollbar = Scrollbar(frame_tools, orient='vertical')
scrollbar.configure(command=tools_tree_view.yview)
# scrollbar.pack(side="right", fill="y")
tools_tree_view.config(yscrollcommand=scrollbar.set)

my_str = StringVar(value="Output")  # assigning string data

# ==== TOOL DATABASE INPUT/CONTROLS ==== #
frame_fields = Frame(tab1)
frame_fields.grid(row=6, column=0)
ttk.Label(frame_fields, text="Update Database: ", font=('bold', 12)).grid(row=0, sticky=W, padx=5, pady=5, columnspan=2)

# NAME
tool_name_text = StringVar()
tool_name_label = Label(frame_fields, text='Name', font=('bold', 10))
tool_name_label.grid(row=1, column=0, sticky=E)
tool_name_entry = Entry(frame_fields, textvariable=tool_name_text)
tool_name_entry.grid(row=1, column=1, sticky=W)
# TYPE
tool_type_text = StringVar()
tool_type_label = Label(frame_fields, text='Type', font=('bold', 10))
tool_type_label.grid(row=1, column=2, sticky=E)
tool_type_entry = Entry(frame_fields, textvariable=tool_type_text)
tool_type_entry.grid(row=1, column=3, sticky=W)
# OS
os_text = StringVar()
os_label = Label(frame_fields, text='OS', font=('bold', 10))
os_label.grid(row=2, column=0, sticky=E)
os_entry = Entry(frame_fields, textvariable=os_text)
os_entry.grid(row=2, column=1, sticky=W)
# NOTES
notes_text = StringVar()
notes_label = Label(frame_fields, text='Notes', font=('bold', 10))
notes_label.grid(row=2, column=2, sticky=E)
notes_entry = Entry(frame_fields, textvariable=notes_text)
notes_entry.grid(row=2, column=3, sticky=W)
# FREE
free_text = StringVar()
free_label = Label(frame_fields, text='Free', font=('bold', 10))
free_label.grid(row=3, column=0, sticky=E)
free_entry = Entry(frame_fields, textvariable=free_text)
free_entry.grid(row=3, column=1, sticky=W)
# DESCRIPTION
description_text = StringVar()
description_label = Label(frame_fields, text='Description', font=('bold', 10))
description_label.grid(row=3, column=2, sticky=E)
description_entry = Entry(frame_fields, textvariable=description_text)
description_entry.grid(row=3, column=3, sticky=W)
# LINK
link_text = StringVar()
link_label = Label(frame_fields, text='Link', font=('bold', 10))
link_label.grid(row=4, column=0, sticky=E)
link_entry = Entry(frame_fields, textvariable=link_text)
link_entry.grid(row=4, column=1, sticky=W)
frame_btns = Frame(tab1)
frame_btns.grid(row=7, column=0)

add_btn = Button(frame_btns, text='Add Tool', width=10, command=add_tool)
add_btn.grid(row=0, column=0, pady=20)

remove_btn = Button(frame_btns, text='Remove Tool', width=10, command=remove_tool)
remove_btn.grid(row=0, column=1)

update_btn = Button(frame_btns, text='Update Tool', width=10, command=update_tool)
update_btn.grid(row=0, column=2)

clear_btn = Button(frame_btns, text='Clear Input', width=10, command=clear_text)
clear_btn.grid(row=0, column=3)

# search_btn = Button(search_entry, text='Search', width=12, command=search_tool_name)
# search_btn.grid(row=0, column=2)

# search_query_btn = Button(search_entry, text='Search Query', width=12, command=execute_query)
# search_query_btn.grid(row=1, column=2)

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
# Recommend tool options (or eliminate bad options)
lbl3 = Label(tab3, text='Enter the encrypted text: ').grid(column=0, row=0, padx=5, pady=5)

# ========================= #
# ====  TAB FOUR: SQL  ==== #
# ========================= #
# What input forms are available?
# Test SQL injections to rule out types of SQL databases/versions?
# Recommend tools
lbl4 = Label(tab4, text='SQL vulnerability finder: ').grid(column=0, row=0, padx=5, pady=5)

# ==================#
# ==== MAINLOOP ====#
# ==================#
# if __name__ == '__main__':
#     conn = lite.connect("dataFile.db")
#     conn.close
#
#     db_open("db1.db")
#     statement = ('CREATE TABLE %s (tool_id INTEGER, filename TEXT);')
#     tables = ['source', 'query']
#
#     database = 'io.db'
#     statements = [statement % table for table in tables]
#
#     setup
#     db = Database('toolDatabase.db')
#     conn = sqlite3.connect(db)
#     cur = conn.cursor()
#     cur.execute(
#         "CREATE TABLE IF NOT EXISTS tools (tool_id INTEGER PRIMARY KEY, tool_name text, "
#         "tool_type text, os integer, notes text)")
#     conn.commit()

# Populate data
populate_list()

window.mainloop()  # Endless loop that maintains the open GUI window

# def ButtonClicked():
#    res = "Welcome to " + txt.get()
#    lbl.configure(text=res)
#    messagebox.showinfo('Information Processed', 'No Help Found.')
#    messagebox.showwarning('Message title', 'Message content')    # Maybe...
#    messagebox.showerror('Message title', 'Message content')      # Maaaaybe...
#    lbl.configure(text="Button was clicked !!")
#    res = messagebox.askquestion('Message title','Message content')
#    res = messagebox.askyesno('Message title','Message content')
#    res = messagebox.askyesnocancel('Message title','Message content')
#    res = messagebox.askokcancel('Message title','Message content')
#    res = messagebox.askretrycancel('Message title','Message content')
