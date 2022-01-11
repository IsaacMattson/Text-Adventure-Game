class GameObject:

    def __init__(self, name, location, movable, visible, carried, description):
        self.name  = name
        self.location = location
        self.movable = movable
        self.visible = visible
        self.carried = carried
        self.description  = description

class Location:
    
    def __init_(self, name, description, value, image):
        self.name = name
        self.description = description
        self.value = value
        self.image = image