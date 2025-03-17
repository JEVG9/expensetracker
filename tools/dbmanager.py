import sqlite3

DB_PATH = "data/expense_tracker.db"

def connection():
    """Connects the app with the db file and creates/return the cursor"""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn, conn.cursor()

def clean_table():
    pass

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

def add_expense(description, amount, category, date=None):
    """Adds an expense to the db. If no date is provided, uses current timestamp."""
    conn, cursor = connection()
    if date:
        cursor.execute("INSERT INTO expenses (description, amount, category, date) VALUES (?, ?, ?, ?)", 
                       (description, amount, category, date))
    else:
        cursor.execute("INSERT INTO expenses (description, amount, category) VALUES (?, ?, ?)", 
                       (description, amount, category))
    conn.commit()
    conn.close()

def mod_expense(id,amount):
    """Modify an expense using the id"""
    conn,cursor = connection()
    cursor.execute("""
    UPDATE expenses
    SET amount= ?
    WHERE id = ?
    """, (amount, id))
    conn.commit()
    conn.close()

def del_expense(id):
    """Deletes an expense using the id"""
    conn, cursor = connection()
    cursor.execute("DELETE FROM expenses WHERE id = ?", (id,))  # <- COMA añadida aquí
    conn.commit()
    conn.close()

def get_expenses():
    #pending expenses filtered by category
    """Returns all expenses in DB"""
    conn, cursor = connection()
    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

def sum_expenses(category:str | None):
    """Returns the sum of all expenses in DB"""
    conn,cursor = connection()
    if category:
        cursor.execute("""
            SELECT SUM(amount) FROM expenses
            WHERE category= ? """,(category,))
    else:
        cursor.execute("SELECT SUM(amount) FROM expenses")
    total = cursor.fetchone()[0]
    conn.close()
    return total if total is not None else 0
    
def sum_expenses_month(year, month):
    """Returns the sum of all expenses of a month"""
    date_filter = f"{year}-{month:02d}"
    conn, cursor = connection()
    cursor.execute("""
        SELECT SUM(amount)
        FROM expenses
        WHERE strftime('%Y-%m', date) = ?
    """, (date_filter,))
    total = cursor.fetchone()[0]
    conn.close()
    return total if total is not None else 0


###########################################
