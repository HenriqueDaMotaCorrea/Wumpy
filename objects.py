# Game objects

class Room():
    def __init__(self, id=0, connections=[], messages=[]):
        self.id = id
        self.connections = connections
        self.messages = messages