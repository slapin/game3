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
            Item("Blue robe", clothes.robes[0], price = 2, str = -1, int = 1),            
            Item("Black robe", clothes.robes[1], price = 8, str = -1, int = 3),
            Item("White robe", clothes.robes[2], price = 12, str = -1, int = 4),
            Item("Red robe", clothes.robes[3], price = 15, str = -2, int = 6),
            Item("Purple robe", clothes.robes[4], price = 15, str = -1, int = 5),
            Item("Green robe", clothes.robes[5], price = 15, str = -2, int = 6),
            Item("Yellow robe", clothes.robes[6], price = 15, str = -2, int = 6),
            Item("Brown robe", clothes.robes[7], price = 15, str = -2, int = 6),
            Item("Light blue robe", clothes.robes[8], price = 15, str = -2, int = 6),
            Item("Iridescent robe", clothes.robes[9], price = 15, str = -2, int = 6),
            Item("Heavy robe", clothes.robes[10], price = 15, str = -2, int = 6),
            Item("Acolyte's robe", clothes.robes[11], price = 22, str = 0, int = 7),
            Item("Hooded robe", clothes.robes[12], price = 25, str = -2, int = 10),
            Item("Fine blue robe", clothes.robes[13], price = 15, str = -2, int = 6),
            Item("Fine dark robe", clothes.robes[14], price = 15, str = -2, int = 6),
            Item("Green dress", clothes.robes[15], price = 15, str = -2, int = 6),
            Item("Elegant robe", clothes.robes[16], price = 15, str = -2, int = 6),
            Item("Simple robe", clothes.robes[17], price = 15, str = -2, int = 6),
            Item("Crimson robe", clothes.robes[18], price = 15, str = -2, int = 6),
            Item("Holy robe", clothes.robes[19], price = 12, str = -1, int = 4),
            Item("Fancy robe", clothes.robes[20], price = 15, str = -2, int = 6),
            Item("Comfortable robe", clothes.robes[21], price = 15, str = -2, int = 6),
            Item("Violet robe", clothes.robes[22], price = 15, str = -2, int = 6),
            Item("Red and gold robe", clothes.robes[23], price = 15, str = -2, int = 6),
            Item("Blood robe", clothes.robes[24], price = 12, str = -1, int = 4),
            Item("Sapphire robe", clothes.robes[25], price = 15, str = -2, int = 6),
            Item("Dragon robe", clothes.robes[26], price = 15, str = -2, int = 6),
            Item("Commander's robe", clothes.robes[27], price = 15, str = -2, int = 6),
            Item("Minister's robe", clothes.robes[28], price = 15, str = -2, int = 6),
            Item("Brown half-robe", clothes.robes[29], price = 15, str = -2, int = 6),
            Item("Grey half-robe", clothes.robes[30], price = 15, str = -2, int = 6),
            Item("White dress", clothes.robes[31], price = 15, str = -2, int = 6),
            Item("Fine purple robes", clothes.robes[32], price = 15, str = -2, int = 6),
            Item("Peasant's dress", clothes.robes[33], price = 15, str = -2, int = 6),
            Item("Bloody torn garment", clothes.robes[34], price = 15, str = -2, int = 6)
              ]

weaponlist = [
              Item("weapon1", clothes.weapons[0], price = 5, damage = 2),
              Item("weapon2", clothes.weapons[1], price = 5, damage = 3),
              Item("weapon3", clothes.weapons[2], price = 5, damage = 4),
              Item("weapon4", clothes.weapons[3], price = 5, damage = 5),
              Item("weapon5", clothes.weapons[4], price = 5, damage = 6),
              Item("weapon6", clothes.weapons[5], price = 5, damage = 7),
              Item("weapon6", clothes.weapons[6], price = 5, damage = 7),
              Item("weapon6", clothes.weapons[7], price = 5, damage = 7),
              Item("weapon6", clothes.weapons[8], price = 5, damage = 7),
              Item("weapon6", clothes.weapons[9], price = 5, damage = 7),
              Item("weapon6", clothes.weapons[10], price = 5, damage = 7),
              Item("weapon6", clothes.weapons[11], price = 5, damage = 7),
              Item("weapon6", clothes.weapons[12], price = 5, damage = 7),
              Item("weapon6", clothes.weapons[13], price = 5, damage = 7),
              Item("weapon6", clothes.weapons[14], price = 5, damage = 7),
              Item("weapon6", clothes.weapons[15], price = 5, damage = 7),
              Item("weapon6", clothes.weapons[16], price = 5, damage = 7),
              Item("weapon6", clothes.weapons[17], price = 5, damage = 7),
              Item("weapon6", clothes.weapons[18], price = 5, damage = 7),
              Item("weapon6", clothes.weapons[19], price = 5, damage = 7),
              Item("weapon6", clothes.weapons[20], price = 5, damage = 7),
              Item("weapon6", clothes.weapons[21], price = 5, damage = 7),
              Item("weapon6", clothes.weapons[22], price = 5, damage = 7),
              Item("weapon6", clothes.weapons[23], price = 5, damage = 7)
              ]

itemlist = robelist