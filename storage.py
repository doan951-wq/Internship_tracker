import json
#Create a save function and a load function

def save_data(internship_data):
    
    with open ("internship_data.json", "w", encoding="utf-8") as file:
        json.dump(internship_data, file, indent=4)
    
    

def load_data():
    try:
        with open("internship_data.json", "r", encoding="utf-8") as file:
            data_json= json.load(file)

            return data_json
    except FileNotFoundError:
        print("Json file does not exist, creating new file")
        return []

    
