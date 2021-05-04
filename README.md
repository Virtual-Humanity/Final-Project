# Pentester's Toolbox

Our goal was to create an efficient quick reference tool for the many useful programs
one might need as a a Pentester/ Red Team. Whether in competition or real world application, 
Pentester's Toolbox keeps even the most obscure tools close at hand exactly when they are needed.

Our product is a tkinter GUI that displays a database of pentesting tools, allows filtering and sorting results,
allows for editing, removing, and adding entries into the backend Sqlite 3 database. While most of the code itself is GUI/Database related, 
the main research required for this was assembling and curating the list of tools, as well as categorizing them. 
The default dataset includes all the most popular tools and a few simple commands as
a reminder that you can add (or remove) any method that you personally find helpful.

Some aspects are still in rough phases, such as menus and the somewhat dated UI. 

To get started with our product, you can simply run `python main.py` with no arguments and go from there, the rest of using it should be fairly obvious.
The hashing and SQL features are unfinished, as they were fairly low priority. 

![Pentester's Toolbox UI](ui_screenshot.png "Pentester's Toolbox UI")

## Future Updates:
- hash tab
- sql tab
- Make visible fields copyable and links clickable. 
- add a context menu on right click 
- add New/ Import/ Export/ Save database options
