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
# import PySimpleGUI as sg
from dbclass import *
# from functions import *
from tkinter import *
from tkinter import messagebox, ttk

# ------------------------------------------------------------------
# ---- CLASS -------------------------------------------------------
# ------------------------------------------------------------------
# Leaveing section as placeholder

# db = Database('tools.db')

# I was intending to do some database tricks to make this program faster and
# more scalable but with the amount of time we have left I'm probably going
# to revamp it to just one very long database entry with as much simple binary
# as possible.

# So it will go from
# COLUMNS[tool_id, tool_name, tool_type, os, free, description, link, notes]
# db.insert("Hashcat", "H", "2", "0", "Hashing tool", "", "")
# to something more like
# COLUMNS[tool_id, tool_name, "Description", link, notes, paid, WIN, NIX, OSx,
# OtherOS, "Open Source", "Decryption", "Hash Cracking", "SQL Injection", "Steganography",
# "Log/Traffic Analysis", "WiFi", "Web Apps", "Scan, Enum. Exploit", "Forensics/Reverse Eng."]
# db.insert("Hashcat","Advanced Password Recovery","","",0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0)
# db.insert("Hashcat","Advanced Password Recovery",".",".","0","0","1","0"
# "0","0","0","0","1","0","0","0","0","0","0","0","0","0","0","0")


# ------------------------------------------------------------------
# ---- DEFINITIONS -------------------------------------------------
# ------------------------------------------------------------------
db = Database('tools.db')


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
    for i, entry in enumerate(db_field_entries):
        if '' == entry.get():
            messagebox.showerror('Required Fields', 'Please include all fields, ' + db_fields[i] + ' is blank')
            return
    db.insert(*[i.get() for i in db_field_entries] + check_button_states)
    clear_text()
    populate_list()


def select_tools(event):
    try:
        index = tools_tree_view.selection()[0]
        selected_item = tools_tree_view.item(index)['values']
        clear_text()
        for i, entry in enumerate(db_field_entries):
            entry.insert(END, selected_item[i+1])           # <--- Controls field output, incremented one to skip id
    except IndexError:
        pass


# ======= UPDATE NEEDED ============ ---------------- <-------------- UPDATE NEEDED ******************
# This function should take in all the input fields, check buttons, find & output the best matches.
# Include ALL Hits in Vulnerabilities category
# ONLY hits in the OS category
# NOT hits in Paid/Free category UNLESS box is checked.
def search_by_elements(query='select * from tools'):
    for i in tools_tree_view.get_children():
        tools_tree_view.delete(i)
    for row in db.fetch2(query):
        tools_tree_view.insert('', 'end', values=row)
    # SELECT * from tools WHERE column (('free' == 0) && ('free' == Pay.get())
    # && ((Col[6-10] ==1) && (os_buttons[0-end] ==1))
    # && ((Col[10-end] ==1) && (db_fields[0-end] ==1))
    #
    # tool_elements = db_fields.get()
    # for i in tools_tree_view.get_children():
    #     tools_tree_view.delete(i)
    # if pay.get() == 1
    #     for i in
    # else
    #
    # for i in tools_tree_view.get_children():
    #     tools_tree_view.delete(i)
    # for row in db.fetch2(query):
    #     tools_tree_view.insert('', 'end', values=row)
    #
    # tool_elements = tool_elements_search_entry.get()
    # tool_elements_search_entry.delete(0, END)
    # populate_list(tool_elements)
    return


def remove_tool():
    index = tools_tree_view.selection()[0]
    selected_item = tools_tree_view.item(index)['values']
    db.remove(selected_item[0])
    clear_text()
    populate_list()


def update_tool():
    index = tools_tree_view.selection()[0]
    selected_item = tools_tree_view.item(index)['values']
    db.update(selected_item[0], *[i.get() for i in db_field_entries])
    clear_text()
    populate_list()


def clear_text():
    for entry in db_field_entries:
        entry.delete(0, END)


def search_tool_name():
    tool_name = tool_name_search_entry.get()
    tool_name_search_entry.delete(0, END)
    populate_list(tool_name)


def execute_query():
    query = query_search.get()
    populate_list2(query)


# ----------------------------------------------------------- #
# ----------   MAIN APP WINDOW   ---------------------------- #
# ----------------------------------------------------------- #

# Create the main window; set title and size
global selected_item
window = Tk()
window.title("Virtual Memory: A Red-Teaming Repo")
window.geometry('950x550')  # Pick standard window size

# ============================== #
# =====   DROP DOWN MENU   ===== #
# ============================== #
# ****************  UPDATE ITEM   ************************** <----------------- UPDATE ITEM
# The drop dowm menu is not functional
# Update to include a real funciton or two (At least a working Exit!)
menu = Menu(window)
new_item = Menu(menu, tearoff=0)
new_item.add_command(label='New')
new_item.add_separator()
new_item.add_command(label='Edit')
menu.add_cascade(label='File', menu=new_item)
window.config(menu=menu)

# ===================== #
# ==== TAB CONTROL ==== #
# ===================== #
# This section established the use of Tabs.
# The options supported by Label() method are:
# anchor, bg, bitmap, bd, cursor, font, fg, height, width, image,
# justify, relief, padx, pady, textvariable, underline and wraplength.
# options supported by grid() method are:
# column, columnspan, row, rowspan, padx, pady, ipadx, ipady and sticky.
tab_control = ttk.Notebook(window)
tab_names = ['Tool Box', 'Add Tool', 'Hashing', 'SQL']
tabs = [ttk.Frame(tab_control) for _ in range(len(tab_names))]
for tab, text in zip(tabs, tab_names):
    tab_control.add(tab, text=text)

tab_control.pack(expand=1, fill="both")

# ============================== #
# ==== TAB ZERO: TOOL SEARCH ==== #
# ============================== #

frame_search = Frame(tabs[0])
frame_search.grid(row=0, column=0, sticky=W)

Label(frame_search, text="Search by Name: ", font=('bold', 12)).grid(row=0, sticky=W, padx=5, pady=5)
tool_name_search_entry = Entry(frame_search, textvariable=StringVar())
tool_name_search_entry.grid(row=0, column=1, padx=5, sticky=E)

# Name to search for (tool_name_search_entry) is passed to search_tool_name
# calls populatelist(toolname) to output matching results
search_btn_tn = Button(frame_search, text='Search', width=12, command=search_tool_name)
search_btn_tn.grid(row=0, column=2, sticky=W)

query_search = StringVar()
# query_search.set("Select * from tools where os=iOS")
# query_search_entry = Entry(frame_search, textvariable=query_search, width=40)
# query_search_entry.grid(row=1, column=1, sticky=E)

# ==== TOOL DATABASE SEARCH FIELDS ==== #
search_fields = Frame(tabs[0])
search_fields.grid(row=1, column=0, sticky=W)

# ============UPDATE NEEDED ====================================<---------------------UPDATE HERE ******
# These fields should search for keyword matches if anything.
# Since we already have a name field to search by maybe
# only seach Description and notes for Keywords???
Label(search_fields, text="Search by Field: ", font=('bold', 12)).grid(row=0, sticky=W, padx=5, pady=5, columnspan=2)
db_fields = ["Name", "Description", "Link", "Notes"]
db_search_labels = [Label(search_fields, text=field, font=('bold', 10)) for field in db_fields]
db_search_entries = [Entry(search_fields, textvariable=StringVar()) for _ in range(len(db_fields))]
for i, label, entry in zip(range(len(db_search_labels)), db_search_labels, db_search_entries):
    label.grid(row=int(i / 2) + 1, column=(i % 2) * 2, sticky=E)
    entry.grid(row=int(i / 2) + 1, column=(i % 2) * 2 + 1, sticky=W)

# OS Select
os_set = Frame(tabs[0])
os_set.grid(row=2, sticky=W)
Label(os_set, text="System(s) Required: ", font=('bold', 12)).grid(row=0, sticky=W, padx=5, pady=5, columnspan=2)
os_texts = ["Windows", "Linux", "iOS", "Other"]
os_buttons = [ttk.Checkbutton(os_set, text=text,
                              variable=IntVar(), onvalue=1, offvalue=0) for text in os_texts]
for i in range(len(os_buttons)):
    os_buttons[i].state(['!alternate'])
    os_buttons[i].grid(column=i % 4, row=int(i / 4) + 1, sticky=W, padx=5, pady=5)
Pay = ttk.Checkbutton(os_set, text="Include Paid Products?", variable=IntVar(), onvalue=1,
                      offvalue=0)
Pay.state(['!alternate'])
Pay.grid(column=0, row=2, columnspan=3, sticky=W, padx=5, pady=5)

# db_fields += os_buttons
# db_fields += Pay  # <---- No idea if this works

# Vulnerability Category
problem_set = Frame(tabs[0])
problem_set.grid(row=1, column=2, rowspan=3, sticky=NW, padx=50)
Label(problem_set, text="Problem Category: ", font=('bold', 12)).grid(row=4, sticky=W, columnspan=2, padx=5, pady=5)
cat_texts = ["Crypto", "Scan_Enum", "Forensics_Rev Eng", "Hashes", "Maintaining Access", "Network Traffic",
             "Open Source", "Social Eng", "SQL", "Stego", "Web Apps", "WiFi", "Other"]
cat_buttons = [ttk.Checkbutton(problem_set, text=text, variable=IntVar(), onvalue=1, offvalue=0) for text in cat_texts]
for i in range(len(cat_buttons)):
    cat_buttons[i].state(['!alternate'])
    cat_buttons[i].grid(column=i % 4, row=int(i / 4) + 7, sticky=W, padx=5, pady=5)
# db_fields += cat_buttons  # <--- Also this
check_button_states = [int(Pay.instate(['selected']))] + \
                      [int(button.instate(['selected'])) for button in os_buttons] + \
                      [int(button.instate(['selected'])) for button in cat_buttons]
search_btns = Frame(tabs[0])
search_btns.grid(row=3, column=0, sticky=E)
search_btn = Button(search_btns, text='Search', width=12, command=search_by_elements)
search_btn.grid(row=0, column=0)

# search_query_btn = Button(search_entry2, text='Search Query', width=12, command=execute_query)
# search_query_btn.grid(row=1, column=2)

# ======  TABLE OUTPUT   ====== #
frame_tools = Frame(tabs[0])
frame_tools.grid(row=4, column=0, sticky=W, pady=20, padx=20, columnspan=3, rowspan=3)

columns = ['id', 'Name', 'OS Support', 'Uses', 'Notes']
description_output = StringVar()
link_output = StringVar()

tools_tree_view = ttk.Treeview(frame_tools, columns=columns, show="headings")
tools_tree_view.column("id", width=30)
tools_tree_view.column("Name", width=40)
tools_tree_view.column("OS Support", width=70)
tools_tree_view.column("Uses", width=120)
tools_tree_view.column("Notes", width=240)
for col in columns:
    tools_tree_view.heading(col, text=col)
tools_tree_view.bind('<<TreeviewSelect>>', select_tools)
tools_tree_view.pack(side="left", fill="y")
scrollbar = Scrollbar(frame_tools, orient='vertical')
scrollbar.configure(command=tools_tree_view.yview)
scrollbar.pack(side="right", fill="y")
tools_tree_view.config(yscrollcommand=scrollbar.set)

# ****************  UPDATE ITEM   ************************** <---------------------------  FIX/UPDATE NEEDED 2nd priority
#  For these I was hoping to have a separate text box outside of the tree-view table
# where the description and link of the selected item could be displayed
# Since both are probably too long to be helpfully shown in the table ........ Not super important. We can always character limit the field to fit
descShow = Label(frame_tools, textvariable=description_output, width=35)
# descShow.grid(row=6, column=0, columnspan=4)
linkShow = Label(frame_tools, textvariable=link_output, width=35)
# linkShow.grid(row=6, column=0, columnspan=4)
# my_str = StringVar(value="Output")  # assigning string data

# ****************  UPDATE ITEM   ************************** <---------------------------  Messed with it, probably broke it
frame_fields = Frame(tabs[0])
frame_fields.grid(row=4, column=2, sticky=E, padx=50)
Label(frame_fields, text="Update the Toolbox: ", font=('bold', 12)).grid(row=0, columnspan=3, sticky=W, padx=5, pady=5)

db_field_labels = [Label(frame_fields, text=field, font=('bold', 10)) for field in db_fields]
db_field_entries = [Entry(frame_fields, textvariable=StringVar()) for _ in range(len(db_fields))]
for i, label, entry in zip(range(len(db_field_labels)), db_field_labels, db_field_entries):
    label.grid(row=int(i / 2) + 1, column=(i % 2) * 2, sticky=E)
    entry.grid(row=int(i / 2) + 1, column=(i % 2) * 2 + 1, sticky=W)

frame_btns = Frame(tabs[0])
frame_btns.grid(row=5, column=2, pady=5, padx=70, sticky=NE)
button_dict = {'Add Tool': add_tool, 'Remove Tool': remove_tool, 'Update Tool': update_tool, 'Clear Input': clear_text}
buttons = [Button(frame_btns, text=i, width=10, command=button_dict[i]) for i in button_dict.keys()]
for i in range(len(buttons)):
    buttons[i].grid(row=int(i / 6), column=i % 6)

# =============================== #
# ==== TAB ONE: UPDATE TOOLS ==== #
# =============================== #
# Separate tab for adding new tools into the database
# Four Text Entry Boxes and all checkboxes
# ===== Tab One Layout =====#  Text Box Entry layout option

# ==== TOOL DATABASE INPUT/CONTROLS ==== #
# Functions should be modified to accept NULL values for Notes, Descriptions, and Link

# OS Select
os_set = Frame(tabs[1])
os_set.grid(row=1, sticky=W)
Label(os_set, text="System(s) Required: ", font=('bold', 12)).grid(row=0, sticky=W, padx=5, pady=5, columnspan=2)
os_texts = ["Windows", "Linux", "iOS", "Other"]
os_buttons = [ttk.Checkbutton(os_set, text=text, variable=IntVar(), onvalue=1, offvalue=0) for text in os_texts]
for i in range(len(os_buttons)):
    os_buttons[i].state(['!alternate'])
    os_buttons[i].grid(column=i % 4, row=int(i / 4) + 1, sticky=W, padx=5, pady=5)
Pay = ttk.Checkbutton(os_set, text="Include Paid Products?", variable=IntVar(), onvalue=1, offvalue=0)
Pay.state(['!alternate'])
Pay.grid(column=0, row=2, columnspan=3, sticky=W, padx=5, pady=5)
# OS0.place(x=75, y=100)

# Vulnerability Category
problem_set = Frame(tabs[1])
problem_set.grid(row=2, sticky=W)
Label(problem_set, text="Problem Category: ", font=('bold', 12)).grid(row=4, sticky=W, columnspan=2, padx=5, pady=5)
cat_texts = ["Crypto", "Scan/Enum", "Forensics/Rev Eng", "Hashes", "Maintaining Access", "Network Traffic",
             "Open Source", "Social Eng", "SQL", "Stego", "Web Apps", "WiFi", "Other"]
cat_buttons = [ttk.Checkbutton(problem_set, text=text, variable=IntVar(), onvalue=1, offvalue=0) for text in cat_texts]
for i in range(len(cat_buttons)):
    cat_buttons[i].state(['!alternate'])
    cat_buttons[i].grid(column=i % 4, row=int(i / 4) + 7, sticky=W, padx=5, pady=5)

frame_fields = Frame(tabs[1])
frame_fields.grid(row=3, column=0, sticky=W)
Label(frame_fields, text="Update the Toolbox: ", font=('bold', 12)).grid(row=0, columnspan=3, sticky=W, padx=5, pady=5)

db_field_labels = [Label(frame_fields, text=field, font=('bold', 10)) for field in db_fields]
db_field_entries2 = [Entry(frame_fields, textvariable=StringVar()) for _ in range(len(db_fields))]
for i, label, entry in zip(range(len(db_field_labels)), db_field_labels, db_field_entries2):
    label.grid(row=int(i / 2) + 1, column=(i % 2) * 2, sticky=E)
    entry.grid(row=int(i / 2) + 1, column=(i % 2) * 2 + 1, sticky=W)

frame_btns = Frame(tabs[1])
frame_btns.grid(row=4, column=0, pady=20)
button_dict = {'Add Tool': add_tool, 'Remove Tool': remove_tool, 'Update Tool': update_tool, 'Clear Input': clear_text}
buttons = [Button(frame_btns, text=i, width=10, command=button_dict[i]) for i in button_dict.keys()]
for i in range(len(buttons)):
    buttons[i].grid(row=int(i / 6), column=i % 6)

# ==================================== #
# ====  TAB TWO: Hash Identifier  ==== #
# ==================================== #

# ****************  UPDATE ITEM   ************************** <---------------------------  CODE NEEDED, 2nd Priority
# A tool to quickly identify, or rule out
# different types of Hashes based on formata
# ie: All alpha vs. alpha/num, hex v. dec v. oct,
# Recommend tool options (or just eliminate options)

lbl3 = Label(tabs[2], text='Enter the encrypted text: ').grid(column=0, row=0, padx=5, pady=5)

# ========================== #
# ====  TAB THREE: SQL  ==== #
# ========================== #
# ****************  UPDATE ITEM   ************************** <---------------------------  CODE NEEDED, 2nd Priority
# What input forms are available?
# Test SQL injections to rule out types of SQL databases/versions?
# Recommend tools

lbl4 = Label(tabs[3], text='SQL vulnerability finder: ').grid(column=0, row=0, padx=5, pady=5)

# =================================== #
# ====  ADD NEW TABS BELOW HERE  ==== #
# =================================== #

# ==================#
# ==== MAINLOOP ====#
# ==================#

# Populate data
populate_list()

window.mainloop()  # Endless loop that maintains the open GUI window

# ============================================= #
# ====  CODE GRAVEYARD, DELETE FROM FINAL  ==== #
# ============================================= #

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

# Importing Files
# from tkinter import filedialog
# file = filedialog.askopenfilename()
# files = filedialog.askopenfilenames()   # Multiple files at once
# file = filedialog.askopenfilename(filetypes = (("Text files","*.txt"),("all files","*.*")))   # Specify file types
# dir = filedialog.askdirectory()       # ask for directory
# from os import path
# file = filedialog.askopenfilename(initialdir= path.dirname(__file__))  # Setting initial directory for the filedialog

# def db_open(filename):
#    "Opens and close the database"
#    with lite.connect(filename) as conn:
#        print(f"I created my database named {filename}")

'''
Label1Tab1.grid(row=0, column=0, padx=15, pady=15)
Entry1Tab1.grid(row=0, column=1, padx=15, pady=15)

familyLabelTab1.grid(row=1, column=0, padx=15, pady=15)
familyEntryTab1.grid(row=1, column=1, padx=15, pady=15)

jobLabelTabOne.grid(row=2, column=0, padx=15, pady=15)
jobEntryTabOne.grid(row=2, column=1, padx=15, pady=15)

imgLabelTabOne.grid(row=0, column=2, rowspan=3, padx=15, pady=15)
'''
