import sqlite3


# create a connection with the db or create one , if it doesn't exist
def get_connection():
    return sqlite3.connect("database.db")


# creates table of expenses
def create_tables():
    # create the cursor to do all the commands
    cursor = get_connection().cursor()

    cursor.execute(
        '''CREATE TABLE IF NOT EXISTS expense(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description TEXT NOT NULL,
        category TEXT NOT NULL,
        amount REAL NOT NULL,
        date TEXT NOT NULL
        )''')

    # commit the changes and close the connection
    get_connection().commit()
    get_connection().close()


def add_expense(description, category, amount, date):
    cursor = get_connection().cursor()
    cursor.execute("INSERT INTO expense ( description, category, amount, date ) VALUES ( ?, ?, ?, ?)",
                   (description, category, amount, date)
                   )
    get_connection().commit()
    get_connection().close()


def get_expenses():
    cursor = get_connection().cursor()
    cursor.execute("SELECT * FROM expense")
    rows = cursor.fetchall()
    get_connection().close()
    return rows


def delete_expense(expense_id_to_delete):
    cursor = get_connection().cursor()
    cursor.execute("DELETE FROM expense WHERE id =?", (expense_id_to_delete,))
    get_connection().commit()
    get_connection().close()
