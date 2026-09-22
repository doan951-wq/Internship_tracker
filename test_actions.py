from actions import get_status_history_to_add, save_internship_database
from database import (
    sql_create_user_id_table,
    sql_create_table,
    sql_create_status_history_table,
    sql_add_user,
    sql_status_tracker_history,
)
import sqlite3
"""Backtests the backfill function if a user inputs a value that is ahead in the internship cycle"""
def test_interview_backfills_previous_statuses():
    result = get_status_history_to_add("interview")

    assert result == [

        "applied",
        "oa",
        "phone screen",
        "interview"

        ]

   
"""Creates a temporary database, creates a user, adds a fake internship.
   Then it checks if status history is saved and updated correctly"""
def test_oa_adds_applied_and_oa_to_history():
    connection = sqlite3.connect(":memory:")
    cursor = connection.cursor()

    sql_create_user_id_table(cursor, connection)
    sql_create_table(cursor, connection)
    sql_create_status_history_table(cursor, connection)

    user_id = sql_add_user(cursor, connection, "tony")

    save_internship_database(
        cursor,
        connection,
        user_id,
        "Google",
        "10/01/2026",
        "oa"
    )

    applied = sql_status_tracker_history(cursor, user_id, "applied")
    oa = sql_status_tracker_history(cursor, user_id, "oa")

    assert applied == 1
    assert oa == 1

    connection.close()

"""Creates aa temp database, creates a user, adds a internship that is in a later stage such as interview stage
   We are trying to check to make sure that status history works regardless of the stage the internship is inputted"""
def test_interview_adds_all_previous_statuses():
    connection = sqlite3.connect(":memory:")
    cursor = connection.cursor()

    sql_create_user_id_table(cursor, connection)
    sql_create_table(cursor, connection)
    sql_create_status_history_table(cursor, connection)

    user_id = sql_add_user(cursor, connection, "tony")

    save_internship_database(
        cursor,
        connection,
        user_id,
        "Meta",
        "10/05/2026",
        "interview"
    )

    applied = sql_status_tracker_history(cursor, user_id,  "applied")
    oa = sql_status_tracker_history(cursor, user_id, "oa")
    phone_screen = sql_status_tracker_history(cursor, user_id, "phone screen")
    interview = sql_status_tracker_history(cursor, user_id, "interview")

    assert applied == 1
    assert oa == 1
    assert phone_screen == 1
    assert interview == 1

    connection.close()

"""Tests a case in which which the user inputs a rejected internship
   We want to make sure that sicne a rjection can come from any stage of the internship process that it does not
   get back filled in the status history"""
def test_rejected_does_not_backfill():
    connection = sqlite3.connect(":memory:")
    cursor = connection.cursor()

    sql_create_user_id_table(cursor, connection)
    sql_create_table(cursor, connection)
    sql_create_status_history_table(cursor, connection)

    user_id = sql_add_user(cursor, connection, "tony")

    save_internship_database(
        cursor,
        connection,
        user_id,
        "Amazon",
        "10/10/2026",
        "rejected"
    )

    applied = sql_status_tracker_history(cursor, user_id, "applied")
    oa = sql_status_tracker_history(cursor, user_id, "oa")
    rejected = sql_status_tracker_history(cursor, user_id, "rejected")

    assert applied == 0
    assert oa == 0
    assert rejected == 1

    connection.close()

"""Test's the user_id filter to make sure other users do not see internships that are not theirs"""
def test_status_history_isolated_by_user():
    connection = sqlite3.connect(":memory:")
    cursor = connection.cursor()

    sql_create_user_id_table(cursor, connection)
    sql_create_table(cursor, connection)
    sql_create_status_history_table(cursor, connection)
    

    tony_id = sql_add_user(cursor, connection, "tony")
    bob_id = sql_add_user(cursor, connection, "bob")

    save_internship_database(
        cursor,
        connection,
        tony_id,
        "Google",
        "10/01/2026",
        "oa"
    )

    save_internship_database(
        cursor,
        connection,
        bob_id,
        "Meta",
        "10/02/2026",
        "interview"
    )

    tony_oa = sql_status_tracker_history(cursor, tony_id, "oa")
    bob_oa = sql_status_tracker_history(cursor, bob_id, "oa")

    assert tony_oa == 1
    assert bob_oa == 1

    connection.close()

"""Tests if the status history backfill feature stays localized to the user that inputed the internship
   and does not change other users status history"""
def test_status_history_isolated_by_user():
    connection = sqlite3.connect(":memory:")
    cursor = connection.cursor()

    sql_create_user_id_table(cursor, connection)
    sql_create_table(cursor, connection)
    sql_create_status_history_table(cursor, connection)

    tony_id = sql_add_user(cursor, connection, "tony")
    bob_id = sql_add_user(cursor, connection, "bob")

    save_internship_database(
        cursor,
        connection,
        tony_id,
        "Google",
        "10/01/2026",
        "oa"
    )

    save_internship_database(
        cursor,
        connection,
        bob_id,
        "Meta",
        "10/02/2026",
        "interview"
    )

    tony_oa = sql_status_tracker_history(cursor, tony_id, "oa")
    bob_oa = sql_status_tracker_history(cursor, bob_id, "oa")
    tony_interview = sql_status_tracker_history(cursor, tony_id, "interview")

    assert tony_oa == 1
    assert bob_oa == 1
    assert tony_interview == 0

    connection.close()