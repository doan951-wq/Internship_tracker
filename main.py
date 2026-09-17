from User_Input import get_action
from actions import (add_internship, display_internship, remove_internship, select_internship,select_edit_option,
                     enter_change,change_value, login_user, get_internship_info)
from database import (sql_connect, sql_create_table, sql_get_internships, sql_create_status_history_table, 
                      sql_create_user_id_table, sql_count_current_status, sql_status_tracker_history)

connection, cursor = sql_connect()
sql_create_table(cursor, connection)
sql_create_status_history_table(cursor, connection)
sql_create_user_id_table(cursor, connection)
user_id = login_user(cursor, connection)



   


while True: 
    """Gets the action the user inputs and does the specific action by conencting to the database and
    calling functions"""

    action = get_action()
    if action == "stop":
        break


    elif action == "print":
         connection, cursor = sql_connect()
         internship_list = sql_get_internships(cursor, user_id)
         print (internship_list)
         connection.close()
        
    elif action == "add":

        connection,cursor = sql_connect()
        sql_create_table(cursor, connection)
        add_internship(cursor, connection, user_id)
        connection.close()



    elif action == "edit":
        """Prints the internship, connects to the data base then runs the various functions to find out what value the user wants to edit, selects
           which internship by their database id, and then askes for the value the user is changing it to"""
        
        display_internship()
        connection, cursor = sql_connect()
        select_edit_option_value = select_edit_option()
        selected_internship = select_internship()   
        enter_changed_value = enter_change(select_edit_option_value)
            
        change_value(cursor,connection, select_edit_option_value, selected_internship, enter_changed_value)

    elif action == "stats":
        connection, cursor = sql_connect()
        status_counts = sql_count_current_status(cursor, user_id)
        print("")
        print("Statistics")
        print("__________")
        print("")
        for stats in status_counts:
              
            print(f"{stats[0].title()}: {stats[1]}")
        print("__________")
        # Conversion Rate logic
        # Applied to OA
        # 18 - 10 (oa/applied)
        # Turn SQL tuple return into dictionary
        
            
        applied = sql_status_tracker_history(cursor, "applied")
        oa = sql_status_tracker_history(cursor, "oa")
        phone_screen = sql_status_tracker_history(cursor, "phone screen")
        interview = sql_status_tracker_history(cursor, "interview")
        offer = sql_status_tracker_history(cursor, "offer")
        accepted = sql_status_tracker_history(cursor, "accepted")
        rejected = sql_status_tracker_history(cursor, "rejected")


        
        if applied > 0:
            print(f"Applied to OA Conversion Rate: {oa/applied*100}%")
            #print (f"OA: {oa}, Applied: {applied}")
        elif oa > 0:
            print(f"OA to Phone Screen Conversion Rate: {phone_screen/oa*100}%")
        elif phone_screen > 0:
            print(f"Phone Screen to Interview Conversion Rate: {interview/phone_screen*100}%")
        elif interview > 0:
            print(f"Interview to Offer Conversion Rate: {offer/interview*100}%")
        elif accepted > 0:
            print(f"Accepted Conversion Rate: {accepted/applied*100}%")
        elif rejected > 0:
            print(f"Rejected Conversion Rate: {rejected/applied*100}%")
        

            #applied, OA, phone screen, interview, offer, accepted/rejected
            
            

    elif action == "remove":
        display_internship() #prints the sql database
        connection, cursor = sql_connect()
        remove_internship(cursor, connection)

    elif action == "history":
         connection, cursor = sql_connect()
         print(sql_count_current_status(cursor, user_id))
         
         

    
    

        
            
   

        


