from actions import add_internship
from storage import load_data



def test_add_internship(monkeypatch):
    test_data = []

    inputs = iter([
        "Microsoft Explore Program",
        "06/05/27",
        "open"
    ])

    def test_input(_): # Replaces the input() function with a fake temporary input function.
        # In this case it does next(inputs) which iterates through the list. 
        # Since add_internship only has 3 input functions, it stops before it returns a error
        #You need iter before you can use next. 

        return next(inputs)

    # Basically monkeypatch is replacing every input() function with a test input function
    monkeypatch.setattr("builtins.input", test_input)

    add_internship(test_data)

    assert test_data == [
        {
            "Internship Name:": "Microsoft Explore Program",
            "Date to Apply By:": "06/05/27",
            "Status:": "open"
        }
    ]

