# Function  definitions
from tkinter import messagebox
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


def add_tool(db_field_entries, db, check_buttons, tools_tree_view):
    if '' == db_field_entries[0].get():
        messagebox.showerror('Required Fields', 'Name field is required')
        return
    check_button_states = [int(button.instate(['selected'])) for button in check_buttons]
    print(check_button_states)
    db.insert(*[i.get() for i in db_field_entries] + check_button_states)
    clear_text(db_field_entries)
    populate_list(db, tools_tree_view)


def select_tools(tools_tree_view, db_field_entries, check_button_states, db, action):
    def remove_tool(db_field_entries, db, tools_tree_view, selected_item):
        db.remove(selected_item[0][0])
        clear_text(db_field_entries)
        populate_list(db, tools_tree_view)

    def update_tool(db, selected_item, tools_tree_view, check_button_states, db_field_entries):
        db.update(selected_item[0][0], *[i.get() for i in db_field_entries] + check_button_states)
        populate_list(db, tools_tree_view)

    try:
        index = tools_tree_view.selection()[0]
        selected_item = db.fetch2(tools_tree_view.item(index)['values'][0])
        print(selected_item[0])
        if action == 'update':
            update_tool(db, selected_item, tools_tree_view, check_button_states, db_field_entries)
            clear_text(db_field_entries)
        else:
            clear_text(db_field_entries)
            for i, entry in enumerate(db_field_entries):
                entry.insert(END, selected_item[0][i + 1])
            if action == 'remove':
                remove_tool(db_field_entries, db, tools_tree_view, selected_item)
                clear_text(db_field_entries)
    except IndexError:
        pass


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
