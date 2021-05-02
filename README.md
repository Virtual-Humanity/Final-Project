# Pentester's Toolbox

Our goal was to create a useful tool that was essentially a collation of all the useful tools 
one might need as a a Pentester/ Red Team. There have been times in competitions and other such things
where we have found that having such an easily searchable tool would be quite useful. 

Our product is a tkinter GUI that displays a database of pentesting tools, allows filtering and sorting results,
allows for editing, removing, and adding entries into the backend Sqlite 3 database. While most of the code itself is GUI/Database related, 
the main research required for this was assembling and curating the list of tools, as well as categorizing them. 

Some aspects are still in rough phases, such as menus and the somewhat dated UI. 

To get started with our product, you can simply run `python main.py` with no arguments and go from there, the rest of using it should be fairly obvious.
The hashing and SQL features are unfinished, as they were fairly low priority. 

![Pentester's Toolbox UI](ui_screenshot.png "Pentester's Toolbox UI")

## Future Updates:
- hash tab
- sql tab
- Make visible fields copyable and links clickable. 
- add a context menu on right click 
- 
- Menu:  New/ Import/ Export/ Save Current Database Options
