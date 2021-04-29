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

from tkinter import ttk, messagebox
from tkinter import *
from dbclass import *


# ------------------------------------------------------------------
# ---- CLASS -------------------------------------------------------
# ------------------------------------------------------------------


# COLUMNS[tool_id, tool_name, tool_type, os, free, description, link, notes]
# db.insert("Hashcat", "H", "2", "0", "Hashing tool", "", "")
# to something more like
# COLUMNS[tool_id, tool_name, "Description", link, notes, paid, WIN, NIX, OSx,
# OtherOS, "Open Source", "Decryption", "Hash Cracking", "SQL Injection", "Steganography",
# "Log/Traffic Analysis", "WiFi", "Web Apps", "Scan, Enum. Exploit", "Forensics/Reverse Eng."]
# db.insert("Hashcat","Advanced Password Recovery","","",0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0)
# db.insert("Hashcat","Advanced Password Recovery",".",".","0","0","1","0"
# "0","0","0","0","1","0","0","0","0","0","0","0","0","0","0","0")


def clear_text(entries):
    for entry in entries:
        entry.delete(0, END)


class Window(Tk):
    tab_names = ['Toolbox', 'Hashing', 'SQL']
    columns = ['id', 'Name', 'OS Support', 'Uses', 'Notes']
    text_entry_fields = ["Name", "Description", "Link", "Notes"]
    cat_texts = ["Crypto", "Scan_Enum", "Forensics_Rev_Eng", "Hashes", "Maintaining_Access", "Network_Traffic",
                 "Open_Source", "Social_Eng", "SQL", "Stego", "Web_Apps", "WiFi", "Other"]
    os_texts = ["Windows", "Linux", "iOS", "Other_OS"]
    db = Database('tools.db')

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
        tabs = [ttk.Frame(tab_control) for _ in self.tab_names]
        for tab, text in zip(tabs, self.tab_names):
            tab_control.add(tab, text=text)
        tab_control.pack(expand=1, fill="both")

        # ============================== #
        # ==== TAB ZERO: TOOL SEARCH ==== #
        # ============================== #
        # Frames
        tree_view_frame, os_checks_frame, category_checks_frame, text_fields_frame, buttons_frame = \
            Frame(tabs[0]), Frame(tabs[0]), Frame(tabs[0]), Frame(tabs[0]), Frame(tabs[0])

        # Grids
        os_checks_frame.grid(row=2, sticky=W)
        category_checks_frame.grid(row=1, column=2, rowspan=3, sticky=NW, padx=50)
        text_fields_frame.grid(row=1, column=0, sticky=W)
        buttons_frame.grid(row=3, columnspan=3)
        tree_view_frame.grid(row=4, column=0, pady=20, padx=20, columnspan=5)
        # Labels
        Label(text_fields_frame, text="Filter by Field: ", font=('bold', 12)).grid(row=0, sticky=W, padx=5, pady=5,
                                                                                   columnspan=2)
        Label(os_checks_frame, text="Filter by OS", font=('bold', 12)).grid(row=0, sticky=W, padx=5, pady=5,
                                                                            columnspan=2)
        for i, field in enumerate(self.text_entry_fields):
            Label(text_fields_frame, text=field, font=('bold', 10)).grid(row=int(i / 2) + 1, column=(i % 2) * 2,
                                                                         sticky=E)
        Label(category_checks_frame, text="Filter by Category: ", font=('bold', 12)).grid(row=4, sticky=W,
                                                                                          columnspan=2, padx=5, pady=5)
        # Entries
        entries = [Entry(text_fields_frame, textvariable=StringVar()) for _ in self.text_entry_fields]
        for i, entry in enumerate(entries):
            entry.grid(row=int(i / 2) + 1, column=(i % 2) * 2 + 1, sticky=W)
        # Name to search for (tool_name_search_entry) is passed to search_tool_name
        # calls populatelist(toolname) to output matching results
        # Tree View
        tools_tree_view = ttk.Treeview(tree_view_frame, columns=self.columns, show="headings")
        for col in self.columns:
            tools_tree_view.column(col, width=200)
            tools_tree_view.heading(col, text=col)
        tools_tree_view.bind('<<TreeviewSelect>>', lambda event: self.select_tools(tools_tree_view,
                                                                                   entries, check_buttons, False))
        tools_tree_view.bind("<Double-1>", lambda event: self.single_tool_window(tools_tree_view, True))
        tools_tree_view.pack(side="left", fill="y")
        scrollbar = Scrollbar(tree_view_frame, orient='vertical')
        scrollbar.configure(command=tools_tree_view.yview)
        scrollbar.pack(side="right", fill="y")
        tools_tree_view.config(yscrollcommand=scrollbar.set)

        # query_search = StringVar()
        # query_search.set("Select * from tools where os=iOS")
        # query_search_entry = Entry(name_search_frame, textvariable=query_search, width=40)
        # query_search_entry.grid(row=1, column=1, sticky=E)

        # ==== TOOL DATABASE SEARCH FIELDS ==== #

        # ============UPDATE NEEDED ====================================<---------------------UPDATE HERE ******
        # These fields should search for keyword matches if anything.
        # Since we already have a name field to search by maybe
        # only seach Description and notes for Keywords???

        # Check Buttons
        os_checks = [ttk.Checkbutton(os_checks_frame, text=text, variable=IntVar(), onvalue=1, offvalue=0)
                     for text in self.os_texts]
        pay_check = ttk.Checkbutton(os_checks_frame, text="Enterprise Product (Paid/Subscription based)",
                                    variable=IntVar(), onvalue=1, offvalue=0)
        category_checks = [ttk.Checkbutton(category_checks_frame, text=text, variable=IntVar(), onvalue=1,
                                           offvalue=0) for text in self.cat_texts]

        # Check Button gridding
        for i, check in enumerate(os_checks):
            check.grid(column=i % 4, row=int(i / 4) + 1, sticky=W, padx=5, pady=5)
        pay_check.grid(column=0, row=2, columnspan=3, sticky=W, padx=5, pady=5)
        for i, check in enumerate(category_checks):
            check.grid(column=i % 4, row=int(i / 4) + 7, sticky=W, padx=5, pady=5)

        # Holder for all check buttons in this frame
        check_buttons = [pay_check] + os_checks + category_checks
        for i, check in enumerate(check_buttons):
            check.state(['!alternate'])

        # Buttons
        button_dict = {
            'Search': lambda: self.populate_list(tools_tree_view, check_buttons=check_buttons, entries=entries),
            'Remove Tool': lambda: self.select_tools(tools_tree_view, entries, check_buttons, True),
            'Add Tool': lambda: self.single_tool_window(tools_tree_view, False),
            'Clear Input': lambda: self.clear_search(tools_tree_view, entries)}
        for i, key in enumerate(button_dict.keys()):
            Button(buttons_frame, text=key, width=10,
                   command=button_dict[key]).grid(row=0, column=i % len(button_dict.keys()))

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
        self.populate_list(tools_tree_view)

    def populate_list(self, tools_tree_view, check_buttons=None, entries=None):
        for i in tools_tree_view.get_children():
            tools_tree_view.delete(i)
        fields = {}
        if check_buttons is not None or entries is not None:
            if check_buttons is not None:
                for i, check in enumerate(check_buttons):
                    if check.instate(['selected']):
                        fields[[['free'] + self.os_texts + self.cat_texts][0][i]] = 1
            if entries is not None:
                for i, entry in enumerate(entries):
                    if entry.get() != '':
                        fields[self.text_entry_fields[i]] = entry.get()
        if fields != {}:
            rows = self.db.fetch(fields=fields)
        else:
            rows = self.db.fetch()
        for row in rows:
            row = list(row)
            os = []
            for i, text in zip(row[6:10], self.os_texts):
                if i:
                    os.append(text)
            row = row[:2] + [os] + [row[10:]] + [row[4]]
            tools_tree_view.insert('', 'end', values=row)

    def select_tools(self, tools_tree_view, entries, check_buttons, remove):
        try:
            for index in range(len(tools_tree_view.selection()) - 1, -1, -1):
                selected_item = self.db.fetch_single(
                    tools_tree_view.item(tools_tree_view.selection()[index])['values'][0])
                if remove:
                    self.db.remove(selected_item[0][0])
                else:
                    for i, check in enumerate(check_buttons):
                        if selected_item[0][i + 5]:
                            check.state(['selected'])
                        else:
                            check.state(['!selected'])
                    clear_text(entries)
                    for i, entry in enumerate(entries):
                        entry.insert(END, selected_item[0][i + 1])
            if remove:
                clear_text(entries)
                for i, check in enumerate(check_buttons):
                    check.state(['!selected'])
                self.populate_list(tools_tree_view)
        except IndexError:
            pass

    def single_tool_window(self, tools_tree_view, update):
        def add_tool():
            if '' == entries[0].get():
                messagebox.showerror('Required Fields', 'Name field is required')
                return
            check_button_states = [int(button.instate(['selected'])) for button in check_buttons]
            self.db.insert(*[i.get() for i in entries] + check_button_states)
            window.destroy()
            self.populate_list(tools_tree_view)

        def save_changes():
            self.db.update(selected_item[0][0], *[i.get() for i in entries] + [
                int(button.instate(['selected'])) for button in check_buttons])
            window.destroy()
            self.populate_list(tools_tree_view)

        window = Tk()
        window.title("Single Tool View")
        tab_control = ttk.Notebook(window)
        tab = ttk.Frame(tab_control)
        selected_item = self.db.fetch_single(
            tools_tree_view.item(tools_tree_view.selection()[0])['values'][0]) if update else []
        tab_control.add(tab, text='View Tool' if update else 'Add Tool')
        tab_control.pack(expand=1, fill="both")
        title_frame, os_checks_frame, category_checks_frame, text_fields_frame, buttons_frame = \
            Frame(tab), Frame(tab), Frame(tab), Frame(tab), Frame(tab)

        # Grids
        title_frame.grid(row=0, sticky=W)
        os_checks_frame.grid(row=1, sticky=W)
        category_checks_frame.grid(row=2, sticky=W)
        text_fields_frame.grid(row=3, column=0, sticky=W)
        buttons_frame.grid(row=4, column=0, pady=20)

        # Labels
        Label(title_frame, text="Full Tool View" if update else "Add Tool",
              font=('bold', 18, 'underline')).grid(row=0, columnspan=3, sticky=W, padx=5, pady=5)
        Label(os_checks_frame, text="System(s) Required: ",
              font=('bold', 12)).grid(row=0, sticky=W, padx=5, pady=5, columnspan=2)
        Label(category_checks_frame, text="Category: ",
              font=('bold', 12)).grid(row=4, sticky=W, columnspan=2, padx=5, pady=5)
        Label(text_fields_frame, text="Specific Details: ",
              font=('bold', 12)).grid(row=0, columnspan=3, sticky=W, padx=5, pady=5)
        for i, field in enumerate(self.text_entry_fields):
            Label(text_fields_frame, text=field,
                  font=('bold', 10)).grid(row=int(i) + 1, column=1, sticky=E)

        # Check Buttons
        os_checks = [ttk.Checkbutton(os_checks_frame, text=text, variable=IntVar(), onvalue=1, offvalue=0) for
                     text in self.os_texts]
        pay_check = ttk.Checkbutton(os_checks_frame, text="Enterprise Product (Paid/Subscription based)",
                                    variable=IntVar(), onvalue=1, offvalue=0)
        category_checks = [ttk.Checkbutton(category_checks_frame, text=text, variable=IntVar(), onvalue=1,
                                           offvalue=0) for text in self.cat_texts]

        # Check Button gridding
        for i, check in enumerate(os_checks):
            check.grid(column=i % 4, row=int(i / 4) + 1, sticky=W, padx=5, pady=5)
        pay_check.grid(column=0, row=2, columnspan=3, sticky=W, padx=5, pady=5)
        for i, check in enumerate(category_checks):
            check.grid(column=i % 4, row=int(i / 4) + 7, sticky=W, padx=5, pady=5)

        # Holder for all check buttons in this frame
        check_buttons = [pay_check] + os_checks + category_checks
        for i, check in enumerate(check_buttons):
            check.state(['!alternate'])
            if update and selected_item[0][i + 5]:
                check.state(['selected'])

        # Entries
        entries = [Entry(text_fields_frame, textvariable=StringVar()) for _ in self.text_entry_fields]
        for i, entry in enumerate(entries):
            entry.grid(row=i + 1, column=2, sticky=W)
            if update:
                entry.insert(END, selected_item[0][i + 1])

        # Buttons
        button_dict = {'Save Changes': lambda: save_changes()} if update else {'Add Tool': lambda: add_tool()}
        button_dict['Clear Input'] = lambda: clear_text(entries)
        for i, key in enumerate(button_dict.keys()):
            Button(buttons_frame, text=key, width=10,
                   command=button_dict[key]).grid(row=0, column=i % len(button_dict.keys()))
        window.mainloop()

    def clear_search(self, tools_tree_view, entries):
        clear_text(entries)
        self.populate_list(tools_tree_view)
    # ======= UPDATE NEEDED ============ ---------------- <-------------- UPDATE NEEDED ******************
    # This function should take in all the input fields, check buttons, find & output the best matches.
    # Include ALL Hits in Vulnerabilities category
    # ONLY hits in the OS category
    # NOT hits in Paid/Free category UNLESS box is checked.
    # search_query_btn = Button(search_entry2, text='Search Query', width=12, command=execute_query)
    # search_query_btn.grid(row=1, column=2)

    # ======  TABLE OUTPUT   ====== #

    # ****************  UPDATE ITEM   ************************** <---------------------------
    # FIX/UPDATE NEEDED 2nd priority
    #  For these I was hoping to have a separate text box outside of the tree-view table
    # where the description and link of the selected item could be displayed
    # Since both are probably too long to be helpfully shown in the table ........ Not super important.
    # We can always character limit the field to fit
    # descShow = Label(tree_view_frame, textvariable=description_output, width=35)
    # descShow.grid(row=6, column=0, columnspan=4)
    # linkShow = Label(tree_view_frame, textvariable=link_output, width=35)
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


if __name__ == "__main__":
    window = Window()
    window.mainloop()
