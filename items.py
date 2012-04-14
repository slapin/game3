class Item(object):
    def __init__(self, name="No Name", **kwargs):
        self.name = name
        self.stats = {}
        for key, value in kwargs.items():
            self.stats[key] = value
        
a = Item("simple robe", str = -1, int )
        