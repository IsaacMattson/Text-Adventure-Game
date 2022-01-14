class GameObject:

    def __init__(self, name, location, movable, visible, carried, description):
        self.name  = name
        self.location = location
        self.movable = movable
        self.visible = visible
        self.carried = carried
        self.description  = description

class Location:
    
    def __init__(self,value, description = 'Null', image = 'res/Title.gif'):
        self.value = value
        self.description = description     
        self.image = image