import clothes

class Item(object):
    def __init__(self, name="No Name", imagedata = clothes.robes[0], price = 0, **kwargs):
        self.name = name
        self.price = price
        self.imagedata = imagedata
        self.stats = {}
        for key, value in kwargs.items():
            self.stats[key] = value

robelist = [
            Item("tattered robe", clothes.robes[0], price = 2, str = -1, int = 1),            
            Item("simple robe", clothes.robes[1], price = 8, str = -1, int = 3),
            Item("ratty robe", clothes.robes[2], price = 12, str = -1, int = 4),
            Item("stinky robe", clothes.robes[3], price = 15, str = -1, int = 5),
            Item("plain robe", clothes.robes[4], price = 15, str = -2, int = 6),
            Item("plain robe", clothes.robes[5], price = 15, str = -2, int = 6),
            Item("plain robe", clothes.robes[6], price = 15, str = -2, int = 6),
            Item("plain robe", clothes.robes[7], price = 15, str = -2, int = 6),
            Item("plain robe", clothes.robes[8], price = 15, str = -2, int = 6),
            Item("plain robe", clothes.robes[9], price = 15, str = -2, int = 6),
            Item("plain robe", clothes.robes[10], price = 15, str = -2, int = 6),
            Item("plain robe", clothes.robes[11], price = 15, str = -2, int = 6),
            Item("plain robe", clothes.robes[12], price = 15, str = -2, int = 6),
            Item("plain robe", clothes.robes[13], price = 15, str = -2, int = 6),
            Item("plain robe", clothes.robes[14], price = 15, str = -2, int = 6),
            Item("plain robe", clothes.robes[15], price = 15, str = -2, int = 6),
            Item("plain robe", clothes.robes[16], price = 15, str = -2, int = 6),
            Item("ratty robe", clothes.robes[17], price = 12, str = -1, int = 4),
            Item("plain robe", clothes.robes[18], price = 15, str = -2, int = 6),
            Item("plain robe", clothes.robes[19], price = 15, str = -2, int = 6),
            Item("plain robe", clothes.robes[20], price = 15, str = -2, int = 6),
            Item("plain robe", clothes.robes[21], price = 15, str = -2, int = 6),
            Item("ratty robe", clothes.robes[22], price = 12, str = -1, int = 4),
            Item("plain robe", clothes.robes[23], price = 15, str = -2, int = 6),
            Item("plain robe", clothes.robes[24], price = 15, str = -2, int = 6),
            Item("plain robe", clothes.robes[25], price = 15, str = -2, int = 6),
            Item("plain robe", clothes.robes[26], price = 15, str = -2, int = 6),
            Item("plain robe", clothes.robes[27], price = 15, str = -2, int = 6),
            Item("plain robe", clothes.robes[28], price = 15, str = -2, int = 6),
            Item("plain robe", clothes.robes[29], price = 15, str = -2, int = 6),
            Item("plain robe", clothes.robes[30], price = 15, str = -2, int = 6),
            Item("plain robe", clothes.robes[31], price = 15, str = -2, int = 6),
            Item("plain robe", clothes.robes[32], price = 15, str = -2, int = 6),
            Item("plain robe", clothes.robes[33], price = 15, str = -2, int = 6),
            Item("plain robe", clothes.robes[34], price = 15, str = -2, int = 6),
              ]

weaponlist = [
              Item("weapon", clothes.weapons[0], price = 5, damage = 2),
              Item("weapon", clothes.weapons[1], price = 5, damage = 3),
              Item("weapon", clothes.weapons[2], price = 5, damage = 4),
              Item("weapon", clothes.weapons[3], price = 5, damage = 5),
              Item("weapon", clothes.weapons[4], price = 5, damage = 6),
              Item("weapon", clothes.weapons[5], price = 5, damage = 7),
              ]

itemlist = robelist