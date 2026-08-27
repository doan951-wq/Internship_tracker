from User_Input import get_action
from actions import add_internship, edit_internship, remove_internship, select_internship,select_edit_option,enter_change,change_value
from print_list import print_list
from storage import save_data, load_data



internship_data = load_data()
    
        #example
        #"Internship Name:": "Microsoft Explore",
        #"Date to Apply By:" : "09/01/26",
        #"Status:" : "Applied" #Applied, #Open # Closed


while True: 
    action = get_action()
    if action == "stop":
        break



        
    if action == "add":

        add_internship(internship_data)
        print_list(internship_data)
        save_data(internship_data)

    elif action == "edit":
            edit_internship(internship_data)
            selected_internship = select_internship()
            

            select_edit_option_value = select_edit_option()
            enter_change_value = enter_change(select_edit_option_value)
            
            change_value(select_edit_option_value, 
                         internship_data, 
                         selected_internship, 
                         enter_change_value)
            
            print_list(internship_data)
            save_data(internship_data)
            

    elif action == "remove":
        remove_internship(internship_data)
        print_list(internship_data)
        save_data(internship_data)

    
    

        
            
   

        


