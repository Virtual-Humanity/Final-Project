import sqlite3


class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS tools (tool_id INTEGER PRIMARY KEY, tool_name text, "
            "description text, link text, notes text, free integer, win integer, nix integer, osx integer, etcOS integer, Crypto integer, Scan_Enum integer, "
            "Forensics_Rev_Eng integer, Hashes integer, Maintaining_Access integer, Network_Traffic integer, Open_Source integer, Social_Eng integer, "
            "SQL integer, Stego integer, Web_Apps integer, WiFi integer, Other integer)")
        self.conn.commit()

    def fetch(self, tool_name=''):
        self.cur.execute(
            "SELECT * FROM tools WHERE tool_name LIKE ?", ('%' + tool_name + '%',))
        rows = self.cur.fetchall()
        return rows

    def fetch2(self, query):
        self.cur.execute(query)
        rows = self.cur.fetchall()
        return rows

    def insert(self, tool_name, description, link, notes, free, win, nix, osx, etcOS, Crypto, Scan_Enum, Forensics_Rev_Eng, Hashes, Maintaining_Access, Network_Traffic, Open_Source, Social_Eng, SQL, Stego, Web_Apps, WiFi, Other):
        self.cur.execute("INSERT INTO tools VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                         (tool_name, description, link, notes, free, win, nix, osx, etcOS, Crypto, Scan_Enum, Forensics_Rev_Eng, Hashes, Maintaining_Access, Network_Traffic, Open_Source, Social_Eng, SQL, Stego, Web_Apps, WiFi, Other))
        self.conn.commit()

    def remove(self, tool_id):
        self.cur.execute("DELETE FROM tools WHERE tool_id=?", (tool_id,))
        self.conn.commit()

    def update(self, tool_name, description, link, notes, free, win, nix, osx, etcOS, Crypto, Scan_Enum, Forensics_Rev_Eng, Hashes, Maintaining_Access, Network_Traffic, Open_Source, Social_Eng, SQL, Stego, Web_Apps, WiFi, Other):
        self.cur.execute(
            "UPDATE tools SET tool_name = ?, description = ?, link = ?, notes= ?, free = ?, win = ?, nix = ?"
            "etcOS = ?, Crypto = ?, Scan/Enum = ?, Forensics/Rev_Eng = ?, Hashes = ?, Maintaining_Access = ?, Network_Traffic = ? "
            "Open_Source = ?, Social_Eng = ?, SQL = ?, Stego = ?, Web_Apps = ?, WiFi = ?, Other = ? WHERE tool_id = ?",
            (tool_name, description, link, notes, free, win, nix, osx, etcOS, Crypto, Scan_Enum, Forensics_Rev_Eng, Hashes, Maintaining_Access, Network_Traffic, Open_Source, Social_Eng, SQL, Stego, Web_Apps, WiFi, Other))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
