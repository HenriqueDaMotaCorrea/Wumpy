# Game objects

class Room():
    def __init__(self, name='0', connections=[]):
        self.name = name
        self.connections = connections
    
    def is_connected(self, other_room):
        if other_room.name in self.connections:
            return True
        else:
            return False

class Entity():
    def __init__(self, **kwargs):
        self.location = None

        for key, value in kwargs.items():
            setattr(self, key, value)
    
    def move(self, new_location):
        self.location = new_location
    
    def move_connected(self, new_location):
        if new_location.is_connected(self.location):
            self.move(new_location)
        else:
            return False