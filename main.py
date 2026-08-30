from User_Input import get_action
from actions import add_internship, edit_internship, remove_internship, select_internship,select_edit_option,enter_change,change_value
from print_list import print_list
from storage import save_data, load_data
from database import sql_connect, sql_create_table, sql_get_internships



internship_data = load_data()
    
        #example
        #"Internship Name:": "Microsoft Explore",
        #"Date to Apply By:" : "09/01/26",
        #"Status:" : "Applied" #Applied, #Open # Closed


while True: 
    action = get_action()
    if action == "stop":
        break


    elif action == "print":
         connection, cursor = sql_connect()
         internship_list = sql_get_internships(cursor)
         print (internship_list)
         connection.close()
        
    elif action == "add":

        connection,cursor = sql_connect()
        sql_create_table(cursor)
        add_internship(cursor, connection)
        connection.close()



    elif action == "edit":
            # prints the internship, connects to the data base then runs the various functions to find out what value the user wants to edit, select which internship by their database id, and then askes for the value the user is changing it to
            edit_internship()
            connection, cursor = sql_connect()
            select_edit_option_value = select_edit_option()
            selected_internship = select_internship()   
            enter_changed_value = enter_change(select_edit_option_value)
            
            change_value(cursor,connection, select_edit_option_value, selected_internship, enter_changed_value)
            
            
            

    elif action == "remove":
        edit_internship() #prints the sql database
        connection, cursor = sql_connect()
        remove_internship(cursor, connection)

    
    

        
            
   

        


