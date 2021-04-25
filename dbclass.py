import sqlite3


class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS tools (tool_id INTEGER PRIMARY KEY, tool_name text, "
            "tool_type text, os integer, free integer, description text, link text, notes text)")
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

    def insert(self, tool_name, tool_type, os, free, description, link, notes):
        self.cur.execute("INSERT INTO tools VALUES (NULL, ?, ?, ?, ?, ?, ?, ?)",
                         (tool_name, tool_type, os, free, description, link, notes))
        self.conn.commit()

    def remove(self, tool_id):
        self.cur.execute("DELETE FROM tools WHERE tool_id=?", (tool_id,))
        self.conn.commit()

    def update(self, tool_id, tool_name, tool_type, os, free, description, link, notes):
        self.cur.execute(
            "UPDATE tools SET tool_name = ?, tool_type = ?, os = ?, "
            "free= ?, description = ?, link = ?, notes = ? WHERE tool_id = ?",
            (tool_name, tool_type, os, free, description, link, notes, tool_id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
