

class Room:
    def __init__(self, name):
        self.name = name


class Ship:
    def __init__(self):
        self.name = "Agatha"
        self.rooms = [  Room("Bridge"), 
                        Room("Engine Room"), 
                        Room("Medical Bay"), 
                        Room("Galley"), 
                        Room("Quarters") 
                    ]

    def description(self):
        output = "This ship is a " + str(len(self.rooms)) + \
                 " room vessel called " + self.name
        return output
