import sqlite3

DB_PATH = "data/expense_tracker.db"

def connection():
    """Connects the app with the db file and creates/return the cursor"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    return conn, cursor

def add_table():
    """Create the table if there is no table on file"""
    conn,cursor = connection()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description TEXT NOT NULL,
        amount FLOAT NOT NULL,
        date DATETIME DEFAULT CURRENT_TIMESTAMP,
        category TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()

def add_expense(description,amount,category):
    conn,cursor = connection()
    cursor.execute("INSERT INTO expenses (description,amount,category) VALUES(?,?,?)", (description,amount,category))
    conn.commit()
    conn.close()

def mod_expense(id,description,amount):
    conn,cursor = connection()
    cursor.execute("""
    UPDATE expenses
    SET description = ?,amount= ?
     WHERE id = ?
    """, (description, amount, id))
    conn.commit()
    conn.close()

def del_expense():pass
def get_expenses():pass
def sum_expenses():pass
def sum_expenses_mont():pass

