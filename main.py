from User_Input import get_action
from actions import add_internship, edit_internship, remove_internship, select_internship,select_edit_option,enter_change,change_value, login_user
from database import sql_connect, sql_create_table, sql_get_internships, sql_create_status_history_table, sql_create_user_id_table, sql_count_status, sql_status_tracker_history


connection, cursor = sql_connect()
sql_create_table(cursor, connection)
sql_create_status_history_table(cursor, connection)
sql_create_user_id_table(cursor, connection)
user_id = login_user(cursor, connection)



   


while True: 
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
            # prints the internship, connects to the data base then runs the various functions to find out what value the user wants to edit, select which internship by their database id, and then askes for the value the user is changing it to
        edit_internship()
        connection, cursor = sql_connect()
        select_edit_option_value = select_edit_option()
        selected_internship = select_internship()   
        enter_changed_value = enter_change(select_edit_option_value)
            
        change_value(cursor,connection, select_edit_option_value, selected_internship, enter_changed_value)

    elif action == "stats":
        connection, cursor = sql_connect()
        status_counts = sql_count_status(cursor, user_id)
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
        

        print(f"Applied to OA Conversion Rate: {oa/applied*100}%")

        
            



            
            
            

    elif action == "remove":
        edit_internship() #prints the sql database
        connection, cursor = sql_connect()
        remove_internship(cursor, connection)

    elif action == "history":
         connection, cursor = sql_connect()
         print(sql_count_status(cursor, user_id))
         
         

    
    

        
            
   

        


