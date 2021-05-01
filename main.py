# Cyber Security Tactics and Techniques compilation
# Final Project

# Thanks to all those who freely distributed the knowledge that made this possible
# --------------------------------------------------------------------------------
# likegeeks.com         geeksforgeeks.org           python4networkengineers.com
# tutorialsteacher.com  tutorialspoint.com          and so many more.

# Example Database entry for populating test data
# db.insert("Hashcat","Advanced Password Recovery","","",0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0)

# import
from tkinter import ttk, messagebox
from tkinter import *
from dbclass import *


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
        self.title("Pentester's Toolbox")
        # window.geometry('950x550')  # Pick standard window size
        # ============================== #
        # =====   DROP DOWN MENU   ===== #
        # ============================== #
        # ****************  UPDATE ITEM   ************************** <----------------- UPDATE ITEM
        # The drop dowm menu is not functional
        # Update to include a real funciton or two (At least a working Exit!)

        # ===================== #
        # ==== TAB CONTROL ==== #
        # ===================== #
        tab_control = ttk.Notebook(self)
        tabs = [ttk.Frame(tab_control) for _ in self.tab_names]
        for tab, text in zip(tabs, self.tab_names):
            tab_control.add(tab, text=text)
        tab_control.pack(expand=1, fill="both")

        # =============================== #
        # ==== TAB ZERO: TOOL SEARCH ==== #
        # =============================== #
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

        # Tree View
        columns = ['id', 'Name', 'Descriptions', 'Link', 'Notes']
        tools_tree_view = ttk.Treeview(tree_view_frame, column=columns, show="headings")
        tools_tree_view.column("id", width=30)
        tools_tree_view.column("Name", width=100)
        tools_tree_view.column("Descriptions", width=350)
        tools_tree_view.column("Link", width=100)
        tools_tree_view.column("Notes", width=250)
        for col in columns[1:]:
            tools_tree_view.heading(col, text=col)

        tools_tree_view.bind('<<TreeviewSelect>>', lambda event: self.select_tools(tools_tree_view,
                                                                                   entries, check_buttons, False))
        tools_tree_view.bind("<Double-1>", lambda event: self.single_tool_window(tools_tree_view, True))
        tools_tree_view.pack(side="left", fill="y")
        scrollbar = Scrollbar(tree_view_frame, orient='vertical')
        scrollbar.configure(command=tools_tree_view.yview)
        scrollbar.pack(side="right", fill="y")
        tools_tree_view.config(yscrollcommand=scrollbar.set)

        # Check Buttons
        os_checks = [ttk.Checkbutton(os_checks_frame, text=text, variable=IntVar(), onvalue=1, offvalue=0)
                     for text in self.os_texts]
        pay_check = ttk.Checkbutton(os_checks_frame, text="Paid/Subscription Products",
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
        # In Progress
        lbl3 = Label(tabs[1], text='Enter a Hash: Under Construction').grid(column=0, row=0, padx=5, pady=5)

        # ========================== #
        # ====  TAB THREE: SQL  ==== #
        # ========================== #
        # In Progress
        lbl4 = Label(tabs[2], text='SQL vulnerability finder: Under Construction').grid(column=0, row=0, padx=5, pady=5)
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
            #row = row[:2] + [os] + [row[10:]] + [row[4]]
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
                        entry.insert(END, selected_item[0][i+1])
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
        pay_check = ttk.Checkbutton(os_checks_frame, text="Paid/Subscription Product)",
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


    # Frames
db = Database('tools.db')
'''
# COLUMNS[tool_id, tool_name, "Description", link, notes, paid, WIN, NIX, OSx, OtherOS, "Open Source", "Decryption", "Hash Cracking", "SQL Injection", "Steganography", "Log/Traffic Analysis", "WiFi", "Web Apps", "Scan, Enum. Exploit", "Forensics/Reverse Eng."]
db.insert("Dirbuster","Directory traversal discovery tool","https://sourceforge.net/projects/dirbuster/","none",0,1,1,1,1,0,0,0,0,0,0,0,1,0,0,0,0,0)
db.insert("dnsenum", "Perl script that enumerates DNS information","https://github.com/fwaeytens/dnsenum","Perl",0,1,1,1,1,0,0,0,0,0,0,0,1,0,0,0,0,0)
db.insert("dnsmap", "Subdomain brute-forcing","https://github.com/resurrecting-open-source-projects/dnsmap","none",0,1,1,1,1,0,0,0,0,0,0,0,1,0,0,0,0,0)
db.insert("dnsrecon", "DNS Enumeration Script","https://github.com/darkoperator/dnsrecon","Python3.6+  Ruby",0,1,1,1,1,0,0,0,0,0,0,0,1,0,0,0,0,0)
db.insert("dorkbot(dork-cli)","Command-line Google dork tool","https://github.com/utiso/dorkbot","Python  SQLite",0,1,1,1,1,0,0,0,0,0,0,1,0,0,0,0,0,0)
db.insert("dorks", "Google hack database automation tool","https://github.com/USSCltd/dorks","phantom js",0,1,1,1,1,0,0,0,0,0,0,1,0,0,0,0,0,0)
db.insert("Dradis","Team PenTest Checklist","https://github.com/dradis/dradis-ce","none",0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0)
db.insert("Digital Invisible Ink Tool","Steganography encode/decoder","https://www.sophos.com/en-us/threat-center/threat-analyses/controlled-applications/Digital%20Invisible%20Ink%20Toolkit.aspx","none",0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,1,0,0)
db.insert("DumpsterDiver","Analyze big volumes of various file types in search of hardcoded secrets","https://github.com/securing/DumpsterDiver","none",0,1,1,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0)
db.insert("EggShell","iOS/macOS/Linux Remote Administration Tool","https://github.com/neoneggplant/EggShell","none",0,0,1,1,1,0,0,0,0,1,0,0,0,0,0,0,0,1)
db.insert("Ettercap suite","MitM attacks; active/passive prot. dissection- ARP poisoning; live server injection-","https://www.ettercap-project.org/","none",0,1,1,1,1,0,0,0,0,0,1,0,0,0,0,0,1,0)
db.insert("evilginx2","Standalone man-in-the-middle attack framework","https://github.com/kgretzky/evilginx2","none",0,0,1,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0)
db.insert("EvilOSX","An evil RAT (Remote Administration Tool) for macOS / OS X","https://github.com/Marten4n6/EvilOSX","none",0,1,1,1,1,0,0,0,0,1,0,0,0,0,0,0,0,1)
db.insert("exif.regex.info","Photo Metadata Viewer","none","none",0,1,1,1,1,0,0,0,0,0,0,1,0,0,0,1,0,0)
db.insert("Explorer Suite","PE editor  process viewer","https://ntcore.com/?page_id=345","rebuilder hex editor import adder signature scanner signature manager  extension support  scripting  disassembler  dependency walker etc.",0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,0)
db.insert("faraday","Collaborative Penetration Test and Vulnerability Management Platform","https://github.com/infobyte/faraday","none",0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1)
db.insert("fcrackzip","A braindead program for cracking encrypted ZIP archives","https://github.com/hyc/fcrackzip","none",0,1,1,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0)
db.insert("fierce","DNS Analysis perl script","https://github.com/mschwager/fierce","none",0,1,1,1,1,0,0,0,0,0,0,0,1,0,0,0,0,0)
db.insert("file","n/a","none","none",0,0,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0)
db.insert("fluxion","Phish for WPA/WPA2 keys","https://github.com/FluxionNetwork/fluxion","none",0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1)
db.insert("FOCA","Find metadata and hidden information in the documents.","https://github.com/ElevenPaths/FOCA","none",0,1,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0)
db.insert("frida-extract","RunPE extraction tool","https://github.com/OALabs/frida-extract","MALWARE  Do Not Extract!  Windows32 bit only",0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0)
db.insert("Futurama code","Futurama Code Keyboard","gotfuturamanonecom/Interactive/AlienCodec/","none",0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0)
db.insert("Fuzzdb","Dictionary of fuzzing attack patterns and primitives","https://github.com/owlinrye/fuzzdb","none",0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1)
db.insert("gdb","GNU Debug,https://www.gnu.org/software/gdb/download/","none",0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0)
db.insert("ghidra","software reverse engineering suite by NSA","https://ghidra-sre.org/","none",0,1,1,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0)
db.insert("git","scm","https://git-scm.com/downloads","none",0,1,1,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0)
db.insert("Gophish","Open-Source Phishing Framework","https://getgophish.com/","none",0,1,1,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0)
db.insert("GromWeb","MD5 & SHA conversion and reverse lookup service.","none","none",0,1,1,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0)
db.insert("Hash Analyzer","Hash Analyzer","https://wwwnonetunnelsupnonecom/hash-analyzer/","none",0,1,1,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0)
db.insert("Hashcat","Advanced Password Recovery","https://github.com/hashcat/hashcat","none",0,1,1,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0)
db.insert("Hcon STF","Toolset for gaining solid anonymity; web app testing assessments Easy & collaborative OS","http://www.hcon.in/downloads.html","none",0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1)
db.insert("hexdump","Get raw hex output","https://github.com/**Many**","hexdump -C file",0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,1,0,0)
db.insert("hieroglyphic-typewriter","Heiroglyphic Keyboard translator","discoveringegyptnonecom/egyptian-hieroglyphic-writing/hieroglyphic-typewriter/","none",0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0)
db.insert("HiddenEyeReborn","Modern phishing tool with advanced functionality","https://github.com/Open-Security-Group-OSG/HiddenEyeReborn","none",0,1,1,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0)
db.insert("Hping","Network tool able to send custom TCP/IP packets","hping.org","none",0,1,1,1,1,0,0,0,0,0,0,0,1,0,0,0,0,0)
db.insert("THC-Hydra","When you need to crack a password online- such as an SSH or FTP login- IMAP- IRC- RDP","https://github.com/vanhauser-thc/thc-hydra","none",0,1,1,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0)
db.insert("IBM Security AppScan","Enable Dev.& QA testing during SDLC process. Risk/Vuln management. Info Access Control","none","none",1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1)
db.insert("IDA_Pro","Disassembler and Debugger","https://www.hex-rays.com/ida-pro","none",0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,0)
db.insert("ExifTool","Read- Write and Edit Exif metadata","https://exiftool.org/install.html","none",0,1,1,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0)
db.insert("image-match","Quickly search over billions of images","https://github.com/EdjoLabs/image-match","none",0,1,1,1,1,0,0,0,0,0,0,1,0,0,0,0,0,0)
db.insert("infernal-twin","Automated wireless hacking tool","https://github.com/entropy1337/infernal-twin","none",0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1)
db.insert("insidePro","n/a","http://findernoneinsideprononecom/","none",0,1,1,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0)
db.insert("InSpectre","Examine Windows for Meltdown and Spectre attack","https://www.grc.com/inspectre.htm","none",0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1)
db.insert("Invoke-PSImage","Embeds a PowerShell script in the pixels of a PNG file","https://github.com/peewpw/Invoke-PSImage","none",0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0)
'''

if __name__ == "__main__":
    window = Window()
    window.mainloop()
