import sqlite3


class Database:
    def __init__(self, db):
        from os.path import isfile
        is_created = isfile(db)
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS tools (tool_id INTEGER PRIMARY KEY, name text, "
            "description text, link text, notes text, free integer, "
            "windows integer, linux integer, ios integer, other_os integer, crypto integer, scan_enum integer, "
            "forensics_rev_eng integer, hashes integer, maintaining_Access integer, "
            "network_traffic integer, open_source integer, social_eng integer, "
            "sql integer, stego integer, web_apps integer, wifi integer, other integer)")
        self.conn.commit()
        if not is_created:
            from csv import reader
            with open('tools.txt', newline='', encoding='utf-8-sig') as csv_file:
                db_csv = reader(csv_file, delimiter=',', quotechar='"')
                for row in db_csv:
                    self.insert(*row[:22])

    def fetch(self, fields=None):
        if fields is None:
            self.cur.execute("SELECT * FROM tools WHERE name LIKE ?", ('%%',))
        else:
            query = "SELECT * FROM tools WHERE "
            query_start = len(query)
            for i in fields.keys():
                query += ("" if len(query) == query_start else " AND ") + i.replace('-', '_').lower() + \
                         (" LIKE " + '\'%' + fields[i] + '%\'' if type(fields[i]) == str else " = " + str(fields[i]))
            self.cur.execute(query)
        return self.cur.fetchall()

    def fetch_single(self, tool_id):
        self.cur.execute("SELECT * FROM tools WHERE tool_id=?", (tool_id,))
        return self.cur.fetchall()

    def insert(self, name, description, link, notes, free, windows, linux, ios, other_os, crypto, scan_enum,
               forensics_rev_eng, hashes, maintaining_access, network_traffic, open_source, social_eng, sql, stego,
               web_apps, wifi, other):
        self.cur.execute("INSERT INTO tools VALUES (NULL, "
                         "?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                         (name, description, link, notes, free, windows, linux, ios, other_os, crypto, scan_enum,
                          forensics_rev_eng, hashes, maintaining_access, network_traffic, open_source, social_eng, sql,
                          stego, web_apps, wifi, other))
        self.conn.commit()

    def remove(self, tool_id):
        self.cur.execute("DELETE FROM tools WHERE tool_id=?", (tool_id,))
        self.conn.commit()

    def update(self, tool_id, name, description, link, notes, free, windows, linux, ios, other_os, crypto, scan_enum,
               forensics_rev_eng, hashes, maintaining_access, network_traffic, open_source, social_eng, sql, stego,
               web_apps, wifi, other):
        self.cur.execute(
            "UPDATE tools SET name = ?, description = ?, link = ?, notes= ?, free = ?, windows = ?, linux = ?, ios = ?,"
            "other_os = ?, crypto = ?, scan_enum = ?, forensics_rev_eng = ?, hashes = ?, maintaining_access = ?, "
            "network_traffic = ?, open_source = ?, social_eng = ?, sql = ?, stego = ?, web_apps = ?, wifi = ?, "
            "other = ? WHERE tool_id = ?",
            (name, description, link, notes, free, windows, linux, ios, other_os, crypto, scan_enum,
             forensics_rev_eng, hashes, maintaining_access, network_traffic, open_source, social_eng, sql, stego,
             web_apps, wifi, other, tool_id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
