import sqlite3

def sql_connect ():
    connection = sqlite3.connect("internship.db")
    cursor = connection.cursor()
    return connection, cursor




def sql_create_table(cursor):
#creates a table only once that gives a unique ID to every internship in the database
    cursor.execute("""CREATE TABLE IF NOT EXISTS internships (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        name TEXT,
        apply_by TEXT,
        status TEXT
    )
    """)

def sql_add_internship(cursor, connection, name, apply_by, status):
    
    cursor.execute(
        """
        INSERT INTO internships (name, apply_by, status)
        VALUES (?, ? , ?)
        """,
        (name,apply_by,status)
    )

    connection.commit()

def sql_get_internships(cursor):
    cursor.execute("SELECT * FROM internships")
    return cursor.fetchall()



