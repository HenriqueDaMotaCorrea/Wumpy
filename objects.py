# Game objects

class Room():
    def __init__(self, id=0, connections=[], messages=[]):
        self.id = id
        self.connections = connections
        self.messages = messages
    
    def is_connected(self, other_room):
        if other_room.id in self.connections:
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