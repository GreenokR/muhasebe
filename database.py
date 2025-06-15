import sqlite3

def connect():
    conn = sqlite3.connect("kasa.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS transactions (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 type TEXT NOT NULL,
                 description TEXT NOT NULL,
                 amount REAL NOT NULL,
                 date TEXT NOT NULL
                 )''')
    conn.commit()
    conn.close()

def add_transaction(tx_type, description, amount, date):
    conn = sqlite3.connect("kasa.db")
    c = conn.cursor()
    c.execute("INSERT INTO transactions (type, description, amount, date) VALUES (?, ?, ?, ?)",
              (tx_type, description, amount, date))
    conn.commit()
    conn.close()

def get_all_transactions():
    conn = sqlite3.connect("kasa.db")
    c = conn.cursor()
    c.execute("SELECT * FROM transactions")
    rows = c.fetchall()
    conn.close()
    return rows

def get_balance():
    conn = sqlite3.connect("kasa.db")
    c = conn.cursor()
    c.execute("SELECT type, amount FROM transactions")
    rows = c.fetchall()
    conn.close()
    gelir = sum([r[1] for r in rows if r[0] == "Gelir"])
    gider = sum([r[1] for r in rows if r[0] == "Gider"])
    return gelir - gider
