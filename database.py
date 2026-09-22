import sqlite3

def sql_connect ():
    """Opens a connection to the internship database."""
    connection = sqlite3.connect("internship.db")
    cursor = connection.cursor()
    return connection, cursor



def sql_create_table(cursor, connection):
    """Creates a table that gives a unique ID to every internship in the database."""
    cursor.execute("""CREATE TABLE IF NOT EXISTS internships (
        
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        user_id INTEGER NOT NULL,
        name TEXT NOT NULL,
        apply_by TEXT NOT NULL,
        status TEXT NOT NULL,

        FOREIGN KEY (user_id) REFERENCES users(id)
    )
    """)
    connection.commit()

def sql_get_user(cursor, username):
    cursor.execute(
        """
        SELECT id
        FROM users
        WHERE LOWER(username) = ?
        """,
        (username.lower(),)

    )
    return cursor.fetchone()

def sql_add_user(cursor, connection, username):
    cursor.execute(
        """
        INSERT INTO users (username)
        VALUES (?)
        """,
        (username,)
    )
    connection.commit()

    return cursor.lastrowid

def sql_create_status_history_table(cursor, connection):
    """Creates a table the stores the history of changes to internship status and records the date it was changed."""
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
    connection.commit()

def sql_create_user_id_table(cursor, connection):
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE
        )
        """
    )
    connection.commit()


def sql_add_status_history(cursor, connection, internship_id, status, date_changed):
    cursor.execute(
        """
        INSERT INTO status_history (internship_id, status, date_changed)
        VALUES (?, ?, ?)
        """,
        (internship_id, status, date_changed)
    )

    connection.commit()
    
def sql_add_internship(cursor, connection,user_id, name, apply_by, status):
    """Adds the internship into the internships database"""
    
    cursor.execute(
        """
        INSERT INTO internships (user_id, name, apply_by, status)
        VALUES (?, ?, ? , ?)
        """,
        (user_id, name, apply_by, status)
    )

    connection.commit()

    #Immediately returns the ID of the internship that was just added
    return cursor.lastrowid 


def update_internship_status(cursor,connection, edit_value, user_selected_number):
    """Changes a specifc internship data based on the value the user decided to edit"""
    
    cursor.execute(
        """
        UPDATE internships
        SET status = ?
        WHERE id = ?
        """,
        (edit_value, user_selected_number)
        
    )
    connection.commit()

    

def update_internship_name(cursor, connection, edit_value, user_selected_number):
    """Updates the internship name based on what internship the user selected"""
    cursor.execute(
        """
        UPDATE internships
        SET name = ?
        WHERE id = ?
        """,
        (edit_value, user_selected_number)
    )
    connection.commit()

def update_internship_date(cursor, connection, edit_value, user_selected_number):
    """Updates the internship date based on what the user selecte"""
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
    """Deltes the internship the user selects from the database"""
    cursor.execute(
        """
        DELETE FROM internships
        WHERE id = ?
        """,
        (user_selected_number,)
    
    )
    connection.commit()


def sql_get_internships(cursor, username):
    """Gets all the internships from the internships database and returns a tuple of all the values"""
    cursor.execute(
        """
        SELECT * FROM internships
        where user_id = ?
        """,
        (username,)
    )
    return cursor.fetchall()

def sql_count_current_status(cursor, user_id):
    """Counts the number of internships and grousp them based on their current status (i.e OA, Rejected, etc)"""
    cursor.execute(
        """
        SELECT status, COUNT(*)
        FROM internships
        WHERE user_id = ?
        GROUP BY status
        """,
        (user_id,)
    )

    return cursor.fetchall()

def sql_status_tracker_history(cursor, user_id, status):
    cursor.execute(
        """
        SELECT COUNT(DISTINCT status_history.internship_id)
        FROM status_history
        JOIN internships
        ON status_history.internship_id = internships.id
        WHERE internships.user_id = ?
        AND status_history.status = ?
        """,
        (user_id, status)
    )

    return cursor.fetchone()[0]





