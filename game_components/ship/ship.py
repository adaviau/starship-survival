class Hatch():
    def __init__(self, first, second):
        self.connected_pair = [ first, second ]

class Room:
    def __init__(self, name):
        self.name = name

class Ship:
    def __init__(self):
        self.name = "Agatha"
        self.rooms = [  
            Room("Bridge"), 
            Room("Engine Room"), 
            Room("Medical Bay"), 
            Room("Galley"), 
            Room("Quarters") 
        ]
        self.connections = [ 
            Hatch( self.rooms[0], self.rooms[3] ),
            Hatch( self.rooms[3], self.rooms[3] ),
            Hatch( self.rooms[0], self.rooms[3] ),
            Hatch( self.rooms[0], self.rooms[3] )
        ]

    def get_room(self, index):
        return self.rooms[index]

    def description(self):
        output = "This ship is a " + str(len(self.rooms)) + \
                 " room vessel called " + self.name
        return output
