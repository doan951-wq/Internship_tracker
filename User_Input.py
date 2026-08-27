#Create a variable where the user is able to select certain options and input there action
def get_action():  
    valid_answer = ["add", "remove", "edit", "stop"] 
    while True:
        action = input("Please type the following options (Add, Edit, Remove, Stop):").lower()

        if action in valid_answer:
            break
        else:
            print("Invalid action type, please type a valid option")


    return action


#Create an if statement that occurs if the following action is selected for add edit and remove



