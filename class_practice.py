class TrackerItem:
    def show_type(self):
        print("I am a tracker item")


class Internship(TrackerItem):
    def __init__(self, company, status):
        self.company = company
        self.status = status

    def change_status(self, new_status):
        self.status = new_status


google = Internship("Google", "applied")
amazon = Internship("Amazon", "applied")

google.change_status("interview")

print("Google:", google.status)
print("Amazon:", amazon.status)

google.show_type()
