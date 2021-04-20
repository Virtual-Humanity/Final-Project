
def populate_list(toolName=''):
    for i in tool_tree_view.get_children():
        tool_tree_view.delete(i)
    for row in db.fetch(toolName):
        tool_tree_view.insert('', 'end', values=row)

def populate_list2(query='select * from tools'):
    for i in tool_tree_view.get_children():
        tool_tree_view.delete(i)
    for row in db.fetch2(query):
        tool_tree_view.insert('', 'end', values=row)

def add_tool():
    if toolType_text.get() == '' or toolName_text.get() == '' or os_text.get() == '' or notes_text.get() == '':
        messagebox.showerror('Required Fields', 'Please include all fields')
        return
    db.insert(toolName_text.get(), toolType_text.get(), os_text.get(), notes_text.get())
    clear_text()
    populate_list()

def select_tool(event):
    try:
        global selected_item
        index = tool_tree_view.selection()[0]
        selected_item = tool_tree_view.item(index)['values']
        toolName_entry.delete(0, END)
        toolName_entry.insert(END, selected_item[1])
        toolType_entry.delete(0, END)
        toolType_entry.insert(END, selected_item[2])
        os_entry.delete(0, END)
        os_entry.insert(END, selected_item[3])
        notes_entry.delete(0, END)
        notes_entry.insert(END, selected_item[4])
    except IndexError:
        pass

def remove_tool():
    db.remove(selected_item[0])
    clear_text()
    populate_list()

def update_tool():
    db.update(selected_item[0], toolName_text.get(), toolType_text.get(), os_text.get(), notes_text.get())
    populate_list()

def clear_text():
    toolType_entry.delete(0, END)
    toolName_entry.delete(0, END)
    os_entry.delete(0, END)
    notes_entry.delete(0, END)

def search_toolName():
    toolName = toolName_search.get()
    populate_list(toolName)

def execute_query():
    query = query_search.get()
    populate_list2(query)
