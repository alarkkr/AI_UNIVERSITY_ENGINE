import sqlite3

class SQLiteMemory:

    def __init__(self):
        self.conn = sqlite3.connect("memory/session_memory.db")
        self.create_table()

    def create_table(self):
        self.conn.execute("""
        CREATE TABLE IF NOT EXISTS memory (
            question TEXT,
            answer TEXT
        )
        """)

    def add(self, q, a):
        self.conn.execute("INSERT INTO memory VALUES (?, ?)", (q, a))
        self.conn.commit()

    def search(self, q):
        cursor = self.conn.execute(
            "SELECT answer FROM memory WHERE question=?",
            (q,)
        )
        row = cursor.fetchone()
        return row[0] if row else None