import sqlite3

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS routers (id INTEGER PRIMARY KEY, toolName text, toolType text, os integer, notes integer)")
        self.conn.commit()

    def fetch(self, toolName=''):
        self.cur.execute(
            "SELECT * FROM routers WHERE toolName LIKE ?", ('%'+toolName+'%',))
        rows = self.cur.fetchall()
        return rows

    def fetch2(self, query):
        self.cur.execute(query)
        rows = self.cur.fetchall()
        return rows

    def insert(self, toolName, toolType, os, notes):
        self.cur.execute("INSERT INTO routers VALUES (NULL, ?, ?, ?, ?)",
                         (toolName, toolType, os, notes))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM routers WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, toolName, toolType, os, notes):
        self.cur.execute("UPDATE routers SET toolName = ?, toolType = ?, os = ?, notes = ? WHERE id = ?",
                         (toolName, toolType, os, notes, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
