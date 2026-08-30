import sqlite3

def sql_connect ():
    connection = sqlite3.connect("internship.db")
    cursor = connection.cursor()
    return connection, cursor




def sql_create_table(cursor):
#creates a table only once that gives a unique ID to every internship in the database
    cursor.execute("""CREATE TABLE IF NOT EXISTS internships (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        name TEXT NOT NULL,
        apply_by TEXT NOT NULL,
        status TEXT NOT NULL
    )
    """)

def sql_create_status_history_table(cursor):
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS status_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        internship_id INTEGER NOT NULL,
        status TEXT NOT NULL,
        date_changed TEXT NOT NULL,
        FOREIGN KEY (internship_id) REFERENCES internships(id)
        )
        """
    )


def sql_add_status_history(cursor, connection, internship_id, status, date_changed):
    cursor.execute(
        """
        INSERT INTO status_history (internship_id, status, date_changed)
        VALUES (?, ?, ?)
        """,
        (internship_id, status, date_changed)
    )

    connection.commit()
    
def sql_add_internship(cursor, connection, name, apply_by, status):
    
    cursor.execute(
        """
        INSERT INTO internships (name, apply_by, status)
        VALUES (?, ? , ?)
        """,
        (name,apply_by,status)
    )

    connection.commit()

def update_internship_status(cursor,connection, edit_value, user_selected_number):
    
    cursor.execute(
        """
        UPDATE internships
        SET status = ?
        WHERE id = ?
        """,
        (edit_value, user_selected_number)
        
    )
    connection.commit()

    

def update_internship_name(cursor,connection, edit_value, user_selected_number):
    cursor.execute(
        """
        UPDATE internships
        SET name = ?
        WHERE id = ?
        """,
        (edit_value,user_selected_number)
    )
    connection.commit()

def update_internship_date(cursor, connection, edit_value, user_selected_number):
    cursor.execute(
        """
        UPDATE internships
        SET apply_by = ?
        WHERE id = ?
        """,
        (edit_value, user_selected_number)
    )
    connection.commit()

def sql_delete_option(cursor, connection, user_selected_number):
    cursor.execute(
        """
        DELETE FROM internships
        WHERE id = ?
        """,
        (user_selected_number,)
    
    )
    connection.commit()


def sql_get_internships(cursor):
    cursor.execute("SELECT * FROM internships")
    return cursor.fetchall()





