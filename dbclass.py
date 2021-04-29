import sqlite3


class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS tools (tool_id INTEGER PRIMARY KEY, Name text, "
            "Description text, Link text, Notes text, free integer, "
            "Windows integer, Linux integer, iOS integer, Other_OS integer, Crypto integer, Scan_Enum integer, "
            "Forensics_Rev_Eng integer, Hashes integer, Maintaining_Access integer, "
            "Network_Traffic integer, Open_Source integer, Social_Eng integer, "
            "SQL integer, Stego integer, Web_Apps integer, WiFi integer, Other integer)")
        self.conn.commit()

    def fetch(self, fields=None):
        if fields is None:
            self.cur.execute("SELECT * FROM tools WHERE Name LIKE ?", ('%%',))
        else:
            query_part_one = "SELECT * FROM tools WHERE"
            query_part_two = []
            for i in fields.keys():
                if type(fields[i]) == str:
                    query_part_two += ['%' + fields[i] + '%']
                    query_part_one += " " + i + " LIKE ?"
                else:
                    query_part_two += [fields[i]]
                    query_part_one += " " + i + "=?"
            print(query_part_one, query_part_two)
            self.cur.execute(query_part_one, (*query_part_two,))
        rows = self.cur.fetchall()
        return rows

    def fetch_single(self, tool_id):
        self.cur.execute(
            "SELECT * FROM tools WHERE tool_id=?", (tool_id,))
        rows = self.cur.fetchall()
        return rows

    def insert(self, Name, Description, Link, Notes, free, Windows, Linux, iOS, Other_OS, Crypto, Scan_Enum,
               Forensics_Rev_Eng, Hashes, Maintaining_Access, Network_Traffic, Open_Source, Social_Eng,
               SQL, Stego, Web_Apps, WiFi, Other):
        self.cur.execute("INSERT INTO tools VALUES (NULL, "
                         "?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                         (Name, Description, Link, Notes, free, Windows, Linux, iOS, Other_OS, Crypto, Scan_Enum,
                          Forensics_Rev_Eng, Hashes, Maintaining_Access, Network_Traffic, Open_Source, Social_Eng, SQL,
                          Stego, Web_Apps, WiFi, Other))
        self.conn.commit()

    def remove(self, tool_id):
        self.cur.execute("DELETE FROM tools WHERE tool_id=?", (tool_id,))
        self.conn.commit()

    def update(self, tool_id, Name, Description, Link, Notes, free, Windows, Linux, iOS, Other_OS, Crypto, Scan_Enum,
               Forensics_Rev_Eng, Hashes, Maintaining_Access, Network_Traffic, Open_Source, Social_Eng, SQL, Stego,
               Web_Apps, WiFi, Other):
        self.cur.execute(
            "UPDATE tools SET Name = ?, Description = ?, Link = ?, Notes= ?, free = ?, Windows = ?, Linux = ?, iOS = ?,"
            "Other_OS = ?, Crypto = ?, Scan_Enum = ?, Forensics_Rev_Eng = ?, Hashes = ?, Maintaining_Access = ?, "
            "Network_Traffic = ?, Open_Source = ?, Social_Eng = ?, SQL = ?, Stego = ?, Web_Apps = ?, "
            "WiFi = ?, Other = ? WHERE tool_id = ?",
            (Name, Description, Link, Notes, free, Windows, Linux, iOS, Other_OS, Crypto, Scan_Enum, Forensics_Rev_Eng,
             Hashes, Maintaining_Access, Network_Traffic, Open_Source, Social_Eng, SQL, Stego, Web_Apps, WiFi, Other,
             tool_id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
