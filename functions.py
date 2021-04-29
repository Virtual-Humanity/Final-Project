# Function  definitions
from tkinter import messagebox, ttk
from tkinter import *


def populate_list(db, tools_tree_view, tool_name=''):
    for i in tools_tree_view.get_children():
        tools_tree_view.delete(i)
    for row in db.fetch(tool_name):
        row = list(row)
        print(row)
        row_modded = row[:2] + [row[6:10]] + [row[10:]] + [row[4]]
        print(row_modded)
        tools_tree_view.insert('', 'end', values=row_modded)


def populate_list2(db, tools_tree_view, query='select * from tools'):
    for i in tools_tree_view.get_children():
        tools_tree_view.delete(i)
    for row in db.fetch2(query):
        row_modded = row[:1] + [row[6:9]] + [row[10:]] + row[4]
        tools_tree_view.insert('', 'end', values=row_modded)


def select_tools(tools_tree_view, db_field_entries, db, action):
    try:
        print(tools_tree_view.selection())
        for index in range(len(tools_tree_view.selection()) - 1, -1, -1):
            selected_item = db.fetch2(tools_tree_view.item(tools_tree_view.selection()[index])['values'][0])
            clear_text(db_field_entries)
            for i, entry in enumerate(db_field_entries):
                entry.insert(END, selected_item[0][i + 1])
            if action == 'remove':
                db.remove(selected_item[0][0])
        if action != '':
            clear_text(db_field_entries)
            populate_list(db, tools_tree_view)
    except IndexError:
        pass


def single_tool_window(tools_tree_view, text_entry_fields, os_texts, cat_texts, db, update):
    def add_tool():
        if '' == at_entries[0].get():
            messagebox.showerror('Required Fields', 'Name field is required')
            return
        check_button_states = [int(button.instate(['selected'])) for button in at_check_buttons]
        print(check_button_states)
        db.insert(*[i.get() for i in at_entries] + check_button_states)
        window.destroy()
        populate_list(db, tools_tree_view)

    def save_changes():
        db.update(selected_item[0][0], *[i.get() for i in at_entries] + [
            int(button.instate(['selected'])) for button in at_check_buttons])
        window.destroy()
        populate_list(db, tools_tree_view)

    window = Tk()
    window.title("Single Tool View")
    tab_control = ttk.Notebook(window)
    tab = ttk.Frame(tab_control)
    selected_item = db.fetch2(tools_tree_view.item(tools_tree_view.selection()[0])['values'][0]) if update else []
    tab_control.add(tab, text='View Tool' if update else 'Add Tool')
    tab_control.pack(expand=1, fill="both")
    at_title_frame, at_os_checks_frame, at_category_checks_frame, at_text_fields_frame, at_buttons_frame = \
        Frame(tab), Frame(tab), Frame(tab), Frame(tab), Frame(tab)

    # Grids
    at_title_frame.grid(row=0, sticky=W)
    at_os_checks_frame.grid(row=1, sticky=W)
    at_category_checks_frame.grid(row=2, sticky=W)
    at_text_fields_frame.grid(row=3, column=0, sticky=W)
    at_buttons_frame.grid(row=4, column=0, pady=20)

    # Labels
    Label(at_title_frame, text="Full Tool View", font=('bold', 18, 'underline')).grid(row=0, columnspan=3, sticky=W,
                                                                                      padx=5, pady=5)
    Label(at_os_checks_frame, text="System(s) Required: ", font=('bold', 12)).grid(row=0, sticky=W, padx=5, pady=5,
                                                                                   columnspan=2)
    Label(at_category_checks_frame, text="Category: ", font=('bold', 12)).grid(row=4, sticky=W, columnspan=2,
                                                                               padx=5, pady=5)
    Label(at_text_fields_frame, text="Specific Details: ", font=('bold', 12)).grid(row=0, columnspan=3, sticky=W,
                                                                                   padx=5, pady=5)
    for i, field in enumerate(text_entry_fields):
        Label(at_text_fields_frame, text=field, font=('bold', 10)).grid(row=int(i) + 1,
                                                                        column=1, sticky=E)

    # Check Buttons
    at_os_checks = [ttk.Checkbutton(at_os_checks_frame, text=text, variable=IntVar(), onvalue=1, offvalue=0) for
                    text in os_texts]
    at_pay_check = ttk.Checkbutton(at_os_checks_frame, text="Enterprise Product (Paid/Subscription based)",
                                   variable=IntVar(), onvalue=1, offvalue=0)
    at_category_checks = [ttk.Checkbutton(at_category_checks_frame, text=text, variable=IntVar(), onvalue=1,
                                          offvalue=0) for text in cat_texts]

    # Check Button gridding
    for i, check in enumerate(at_os_checks):
        check.grid(column=i % 4, row=int(i / 4) + 1, sticky=W, padx=5, pady=5)
    at_pay_check.grid(column=0, row=2, columnspan=3, sticky=W, padx=5, pady=5)
    for i, check in enumerate(at_category_checks):
        check.grid(column=i % 4, row=int(i / 4) + 7, sticky=W, padx=5, pady=5)

    # Holder for all check buttons in this frame
    at_check_buttons = [at_pay_check] + at_os_checks + at_category_checks
    for i, check in enumerate(at_check_buttons):
        check.state(['!alternate'])
        if update and selected_item[0][i+5]:
            check.state(['selected'])

    # Entries
    at_entries = [Entry(at_text_fields_frame, textvariable=StringVar()) for _ in text_entry_fields]
    for i, entry in enumerate(at_entries):
        entry.grid(row=i + 1, column=2, sticky=W)
        if update:
            entry.insert(END, selected_item[0][i + 1])

    # Buttons
    at_button_dict = {'Save Changes': lambda: save_changes()} if update else {'Add Tool': lambda: add_tool()}
    at_button_dict['Clear Input'] = lambda: clear_text(at_entries)
    for i, key in enumerate(at_button_dict.keys()):
        Button(at_buttons_frame, text=key, width=10,
               command=at_button_dict[key]).grid(row=0, column=i % len(at_button_dict.keys()))
    window.mainloop()


# ======= UPDATE NEEDED ============ ---------------- <-------------- UPDATE NEEDED ******************
# This function should take in all the input fields, check buttons, find & output the best matches.
# Include ALL Hits in Vulnerabilities category
# ONLY hits in the OS category
# NOT hits in Paid/Free category UNLESS box is checked.
def search_by_elements(db, tools_tree_view, query='select * from tools'):
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


def clear_text(db_field_entries):
    for entry in db_field_entries:
        entry.delete(0, END)


def search_tool_name(db, tools_tree_view, tool_name_search_entry):
    tool_name = tool_name_search_entry.get()
    tool_name_search_entry.delete(0, END)
    populate_list(db, tools_tree_view, tool_name)


def execute_query(db, tools_tree_view, query_search):
    query = query_search.get()
    populate_list2(db, tools_tree_view, query)
