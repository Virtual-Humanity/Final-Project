# Function  definitions
from tkinter import messagebox
from tkinter import *


def populate_list(db, tools_tree_view, tool_name=''):
    for i in tools_tree_view.get_children():
        tools_tree_view.delete(i)
    for row in db.fetch(tool_name):
        tools_tree_view.insert('', 'end', values=row)


def populate_list2(db, tools_tree_view, query='select * from tools'):
    for i in tools_tree_view.get_children():
        tools_tree_view.delete(i)
    for row in db.fetch2(query):
        tools_tree_view.insert('', 'end', values=row)


def add_tool(db_field_entries, db, check_button_states, db_fields, tools_tree_view):
    for i, entry in enumerate(db_field_entries[:3]):
        if '' == entry.get():
            messagebox.showerror('Required Fields', 'Please include all fields, ' + db_fields[i] + ' is blank')
            return
    db.insert(*[i.get() for i in db_field_entries] + check_button_states)
    clear_text(db_field_entries)
    populate_list(db, tools_tree_view)


def select_tools(tools_tree_view, db_field_entries, selected_item):
    try:
        index = tools_tree_view.selection()[0]

        selected_item = tools_tree_view.item(index)['values']
        clear_text(db_field_entries)
        for i, entry in enumerate(db_field_entries):
            entry.insert(END, selected_item[i])
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


def remove_tool(db_field_entries, db, tools_tree_view, selected_item):
    db.remove(selected_item[0])
    clear_text(db_field_entries)
    populate_list(db, tools_tree_view)


def update_tool(db, selected_item, tools_tree_view, db_field_entries):
    db.update(selected_item[0], *[i.get() for i in db_field_entries])
    populate_list(db, tools_tree_view)


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
