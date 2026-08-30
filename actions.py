
from database import sql_add_internship, update_internship_name, update_internship_date, update_internship_status, sql_get_internships, sql_connect,sql_delete_option
def add_internship(cursor, connection):
#Use append function to add to the list
    valid_choices_status = ["applied", "open", "closed"]
    

   
    internship_name = input("What is the name of the internship?: ").strip()
    internship_date = input("What the the date of the internship? (XX/XX/XXXX): ").strip()

    while True:
        
        internship_status = input("What is the status of the internship? (Applied, Open, or Closed): ").strip().lower()
        if internship_status in valid_choices_status:
            break
        print ("Not a valid choice, Please choose a valid option")

    sql_add_internship(
        cursor,
        connection,
        internship_name,
        internship_date,
        internship_status,
    )
    
  
    
    user_input_data = {
         
                        "Internship Name:": internship_name,
                        "Date to Apply By:": internship_date, 
                        "Status:": internship_status

    }

    

        

def edit_internship():
    
    connection, cursor = sql_connect()
    internships = sql_get_internships(cursor)
    print(internships)
    connection.close()

    

def select_internship():
    # tells the user to select the internship and subtracts 1 to read it from the correct starting index
    while True:   
        user_selected_number = int(input("Please select the internship you would like to edit with its corresponding number: ").strip())


        #if not user_selected_number.is_integer():
            #print ("Invalid input, please enter a number")

        #else:
        break
            
    return user_selected_number

    
def select_edit_option():
    valid__edit_type = ["name", "date", "status"]        
            
    while True:        

        edit_action = input("What would you like to edit? (Name, Date, Status): ").lower().strip()

        if edit_action in valid__edit_type:
            break
        else:
            print("Please type in a valid option")

    return edit_action

def enter_change(edit_action):
    valid_choices_status = ["applied", "open", "closed"]

    while True:

        edit_change = input("Please enter the change: ").strip()
        if edit_action == "date" or edit_action == "name":
            break
        

        if edit_action == "status" and edit_change in valid_choices_status:
            break
        else:
            print("Please chose a valid option (Open, Closed, Applied)")

    return edit_change

def change_value(cursor,connection,edit_action, user_selected_number, edit_change):

          
    if edit_action == "name":
       
        update_internship_name(
            cursor,
            connection,
            edit_change,
            user_selected_number
        )
        

    elif edit_action == "date":
        
        update_internship_date(
            cursor,
            connection,
            edit_change,
            user_selected_number
        )
        

    elif edit_action == "status":
        
        update_internship_status(
            cursor,
            connection,
            edit_change,
            user_selected_number
        )
        
        
        

def remove_internship(cursor,connection):

    

    user_selected_number = int(input("Please select the number corresponding to the internship you want to delete: ").strip())

    sql_delete_option(cursor, connection, user_selected_number)

    

    

    

    
        

