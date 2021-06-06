import sqlite3

connection = sqlite3.connect("data.db")
connection.row_factory = sqlite3.Row


def create_table():
    with connection:
        connection.execute(
            "CREATE TABLE IF NOT EXISTS entries (content TEXT, date TEXT);")


def add_entry(entry_content, entry_date):
    with connection:
        connection.execute(  # To protect against SQL injection attack:
            "INSERT INTO entries VALUES(?, ?);", (entry_content, entry_date))


# Not making the syntax shorter to make it readable
def get_entries():
    cursor = connection.execute("SELECT * FROM entries;")
    return cursor
