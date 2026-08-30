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
            edit_internship()
            selected_internship = select_internship()
            ##this next     
            connection, cursor = sql_connect()
            

            select_edit_option_value = select_edit_option()
            enter_change_value = enter_change(select_edit_option_value)
            
            change_value(cursor,connection, select_edit_option_value, selected_internship, enter_change_value)
            
            
            

    elif action == "remove":
        remove_internship(internship_data)
        print_list(internship_data)
        save_data(internship_data)

    
    

        
            
   

        


