# A class is a blueprint. TrackerItem is the parent class in this example.
class TrackerItem:
    # This is an instance method. `self` is the object that called the method.
    def show_type(self):
        print("I am a tracker item")


# Putting TrackerItem in parentheses makes Internship inherit its methods.
class Internship(TrackerItem):
    # Python calls __init__ when a new Internship object is created.
    # `company` and `status` receive the arguments passed to Internship(...).
    def __init__(self, company, status):
        # These lines store separate data on each individual object.
        self.company = company
        self.status = status

    # This method changes the status of the object that called it.
    def change_status(self, new_status):
        self.status = new_status


# Calling the class creates two separate objects from the same blueprint.
google = Internship("Google", "applied")
amazon = Internship("Amazon", "applied")

# Here `self` will refer to `google`, so Amazon remains unchanged.
google.change_status("interview")

# Attribute access uses a dot: google.status reads data stored on google.
print("Google:", google.status)
print("Amazon:", amazon.status)

# Internship inherited show_type() from its parent, TrackerItem.
google.show_type()
