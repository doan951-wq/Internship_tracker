

def add_internship(internship_data):
#Use append function to add to the list
    valid_choices_status = ["applied", "open", "closed"]
    

   
    internship_name = input("What is the name of the internship?: ").strip()
    internship_date = input("What the the date of the internship? (XX/XX/XXXX): ").strip()

    while True:
        
        internship_status = input("What is the status of the internship? (Applied, Open, or Closed): ").strip().lower()
        if internship_status in valid_choices_status:
            break
        print ("Not a valid choice, Please choose a valid option")
    
  
    
    user_input_data = {
         
                        "Internship Name:": internship_name,
                        "Date to Apply By:": internship_date, 
                        "Status:": internship_status

    }

    internship_data.append(user_input_data)

        

def edit_internship(internship_data):
    counter_number = 0

    for line in internship_data:
        counter_number += 1
        print(counter_number, " ", line)

def select_internship():
    while True:   
        user_selected_number = int(input("Please select the internship you would like to edit with its corresponding number: ").strip())-1


        if not user_selected_number.is_integer():
            print ("Invalid input, please enter a number")

        else:
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

def change_value(edit_action, internship_data, user_selected_number, edit_change):      
    if edit_action == "name":
        internship_data[user_selected_number]["Internship Name:"] = edit_change

    elif edit_action == "date":
        internship_data[user_selected_number]["Date to Apply By:"] = edit_change

    elif edit_action == "status":
        internship_data[user_selected_number]["Status:"] = edit_change
        
        

def remove_internship(internship_data):

    counter_number = 0
    
    for line in internship_data:
        counter_number+=1
        print (counter_number, " .", line)

    user_selected_number = int(input("Please select the number corresponding to the internship you want to delete: ").strip())-1

    del internship_data[user_selected_number]

    

    
        

