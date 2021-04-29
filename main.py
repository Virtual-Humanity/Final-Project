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
from functions import *
from tkinter import ttk
from dbclass import *

# ------------------------------------------------------------------
# ---- CLASS -------------------------------------------------------
# ------------------------------------------------------------------
# Leaveing section as placeholder

# db = Database('tools.db')

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


# ----------------------------------------------------------- #
# ----------   MAIN APP WINDOW   ---------------------------- #
# ----------------------------------------------------------- #

# Create the main window; set title and size
class Window(Tk):
    def __init__(self):
        super().__init__()
        self.title("Virtual Memory: A Red-Teaming Repo")
        # window.geometry('950x550')  # Pick standard window size
        # ============================== #
        # =====   DROP DOWN MENU   ===== #
        # ============================== #
        # ****************  UPDATE ITEM   ************************** <----------------- UPDATE ITEM
        # The drop dowm menu is not functional
        # Update to include a real funciton or two (At least a working Exit!)
        menu = Menu(self)
        new_item = Menu(menu, tearoff=0)
        new_item.add_command(label='New')
        new_item.add_separator()
        new_item.add_command(label='Edit')
        menu.add_cascade(label='File', menu=new_item)
        self.config(menu=menu)

        # ===================== #
        # ==== TAB CONTROL ==== #
        # ===================== #
        tab_control = ttk.Notebook(self)
        tab_names = ['Toolbox', 'Hashing', 'SQL']
        tabs = [ttk.Frame(tab_control) for _ in tab_names]
        for tab, text in zip(tabs, tab_names):
            tab_control.add(tab, text=text)
        tab_control.pack(expand=1, fill="both")

        # ============================== #
        # ==== TAB ZERO: TOOL SEARCH ==== #
        # ============================== #

        frame_search = Frame(tabs[0])
        frame_search.grid(row=0, column=0, sticky=W)
        frame_tools = Frame(tabs[0])
        frame_tools.grid(row=4, column=0, pady=20, padx=20, columnspan=5)
        search_fields = Frame(tabs[0])
        search_fields.grid(row=1, column=0, sticky=W)
        os_set = Frame(tabs[0])
        os_set.grid(row=2, sticky=W)
        search_btns = Frame(tabs[0])
        search_btns.grid(row=3, columnspan=3)
        problem_set = Frame(tabs[0])
        problem_set.grid(row=1, column=2, rowspan=3, sticky=NW, padx=50)
        Label(frame_search, text="Search by Name: ", font=('bold', 12)).grid(row=0, sticky=W, padx=5, pady=5)
        tool_name_search_entry = Entry(frame_search, textvariable=StringVar())
        tool_name_search_entry.grid(row=0, column=1, padx=5, sticky=E)

        # Name to search for (tool_name_search_entry) is passed to search_tool_name
        # calls populatelist(toolname) to output matching results

        columns = ['id', 'Name', 'OS Support', 'Uses', 'Notes']
        tools_tree_view = ttk.Treeview(frame_tools, columns=columns, show="headings")
        tools_tree_view.column("id", width=30)
        tools_tree_view.column("Name", width=40)
        tools_tree_view.column("OS Support", width=70)
        tools_tree_view.column("Uses", width=120)
        tools_tree_view.column("Notes", width=240)
        for col in columns:
            tools_tree_view.heading(col, text=col)
        tools_tree_view.bind('<<TreeviewSelect>>', lambda event: select_tools(tools_tree_view, db_search_entries,
                                                                              db, action=''))
        tools_tree_view.bind("<Double-1>", lambda event: single_tool_window(tools_tree_view, text_entry_fields,
                                                                            os_texts, cat_texts, db, 1))
        tools_tree_view.pack(side="left", fill="y")
        scrollbar = Scrollbar(frame_tools, orient='vertical')
        scrollbar.configure(command=tools_tree_view.yview)
        scrollbar.pack(side="right", fill="y")
        tools_tree_view.config(yscrollcommand=scrollbar.set)

        search_btn_tn = Button(frame_search, text='Search', width=12,
                               command=lambda: search_tool_name(db, tools_tree_view,
                                                                tool_name_search_entry))
        search_btn_tn.grid(row=0, column=2, sticky=W)

        # query_search = StringVar()
        # query_search.set("Select * from tools where os=iOS")
        # query_search_entry = Entry(frame_search, textvariable=query_search, width=40)
        # query_search_entry.grid(row=1, column=1, sticky=E)

        # ==== TOOL DATABASE SEARCH FIELDS ==== #

        # ============UPDATE NEEDED ====================================<---------------------UPDATE HERE ******
        # These fields should search for keyword matches if anything.
        # Since we already have a name field to search by maybe
        # only seach Description and notes for Keywords???
        Label(search_fields, text="Filter by Field: ", font=('bold', 12)).grid(row=0, sticky=W, padx=5, pady=5,
                                                                               columnspan=2)
        text_entry_fields = ["Name", "Description", "Link", "Notes"]
        db_search_labels = [Label(search_fields, text=field, font=('bold', 10)) for field in text_entry_fields]
        db_search_entries = [Entry(search_fields, textvariable=StringVar()) for _ in range(len(text_entry_fields))]
        for i, label, entry in zip(range(len(db_search_labels)), db_search_labels, db_search_entries):
            label.grid(row=int(i / 2) + 1, column=(i % 2) * 2, sticky=E)
            entry.grid(row=int(i / 2) + 1, column=(i % 2) * 2 + 1, sticky=W)

        # OS Select

        Label(os_set, text="Filter by OS", font=('bold', 12)).grid(row=0, sticky=W, padx=5, pady=5,
                                                                   columnspan=2)
        os_texts = ["Windows", "Linux", "iOS", "Other"]
        os_buttons = [ttk.Checkbutton(os_set, text=text,
                                      variable=IntVar(), onvalue=1, offvalue=0) for text in os_texts]
        for i in range(len(os_buttons)):
            os_buttons[i].state(['!alternate'])
            os_buttons[i].grid(column=i % 4, row=int(i / 4) + 1, sticky=W, padx=5, pady=5)
        Pay = ttk.Checkbutton(os_set, text="Enterprise Product (Paid/Subscription based)", variable=IntVar(), onvalue=1,
                              offvalue=0)
        Pay.state(['!alternate'])
        Pay.grid(column=0, row=2, columnspan=3, sticky=W, padx=5, pady=5)

        # Vulnerability Category

        Label(problem_set, text="Filter by Category: ", font=('bold', 12)).grid(row=4, sticky=W, columnspan=2, padx=5,
                                                                                pady=5)
        cat_texts = ["Crypto", "Scan_Enum", "Forensics_Rev Eng", "Hashes", "Maintaining Access", "Network Traffic",
                     "Open Source", "Social Eng", "SQL", "Stego", "Web Apps", "WiFi", "Other"]
        cat_buttons = [ttk.Checkbutton(problem_set, text=text, variable=IntVar(), onvalue=1, offvalue=0) for text in
                       cat_texts]
        for i in range(len(cat_buttons)):
            cat_buttons[i].state(['!alternate'])
            cat_buttons[i].grid(column=i % 4, row=int(i / 4) + 7, sticky=W, padx=5, pady=5)
        check_button_states = [int(Pay.instate(['selected']))] + \
                              [int(button.instate(['selected'])) for button in os_buttons] + \
                              [int(button.instate(['selected'])) for button in cat_buttons]

        button_dict = {
            'Search': lambda: search_by_elements(db, tools_tree_view),
            'Remove Tool': lambda: select_tools(tools_tree_view, db_search_entries, db,
                                                action='remove'),
            'Add Tool': lambda: single_tool_window(tools_tree_view, text_entry_fields, os_texts, cat_texts, db, 0),
            'Clear Input': lambda: clear_text(db_search_entries)}
        buttons = [Button(search_btns, text=i, width=15,
                          command=button_dict[i]) for i in button_dict.keys()]
        for i in range(len(buttons)):
            buttons[i].grid(row=int(i / 6), column=i % 6)

        populate_list(db, tools_tree_view)

        # search_query_btn = Button(search_entry2, text='Search Query', width=12, command=execute_query)
        # search_query_btn.grid(row=1, column=2)

        # ======  TABLE OUTPUT   ====== #

        # ****************  UPDATE ITEM   ************************** <---------------------------
        # FIX/UPDATE NEEDED 2nd priorit
        #  For these I was hoping to have a separate text box outside of the tree-view table
        # where the description and link of the selected item could be displayed
        # Since both are probably too long to be helpfully shown in the table ........ Not super important.
        # We can always character limit the field to fit
        # descShow = Label(frame_tools, textvariable=description_output, width=35)
        # descShow.grid(row=6, column=0, columnspan=4)
        # linkShow = Label(frame_tools, textvariable=link_output, width=35)
        # linkShow.grid(row=6, column=0, columnspan=4)
        # my_str = StringVar(value="Output")  # assigning string data

        # ****************  UPDATE ITEM   ************************** <---------------------------

        # =============================== #
        # ==== TAB ONE: UPDATE TOOLS ==== #
        # =============================== #
        # Separate tab for adding new tools into the database
        # Four Text Entry Boxes and all checkboxes
        # ===== Tab One Layout =====#  Text Box Entry layout option

        # ==== TOOL DATABASE INPUT/CONTROLS ==== #
        # Functions should be modified to accept NULL values for Notes, Descriptions, and Link

        # Frames

        # ==================================== #
        # ====  TAB TWO: Hash Identifier  ==== #
        # ==================================== #

        # ****************  UPDATE ITEM   ************************** <---------------------------
        # CODE NEEDED, 2nd Priority
        # A tool to quickly identify, or rule out
        # different types of Hashes based on formata
        # ie: All alpha vs. alpha/num, hex v. dec v. oct,
        # Recommend tool options (or just eliminate options)

        lbl3 = Label(tabs[1], text='Enter the encrypted text: ').grid(column=0, row=0, padx=5, pady=5)

        # ========================== #
        # ====  TAB THREE: SQL  ==== #
        # ========================== #
        # ****************  UPDATE ITEM   ************************** <---------------------------
        # CODE NEEDED, 2nd Priority
        # What input forms are available?
        # Test SQL injections to rule out types of SQL databases/versions?
        # Recommend tools

        lbl4 = Label(tabs[2], text='SQL vulnerability finder: ').grid(column=0, row=0, padx=5, pady=5)




# =================================== #
# ====  ADD NEW TABS BELOW HERE  ==== #
# =================================== #

# ==================#
# ==== MAINLOOP ====#
# ==================#

# Populate data
if __name__ == "__main__":
    window = Window()
    window.mainloop()

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
