# These variables are used in drawing various bits of clothing onto humanoid characters.
#  the first tuple is the pixel coords of the section of the image to draw,
# the second is the offset required to properly place it on top of the unit

robes = []
base = (-544, -96)
for i in range(6): # first row of robes
    offset = (16, 0)
    x = base[0] - i * 16
    y = base[1]
    robes.append(((x, y), offset))

base = (0, -128)
for i in range(29): # second row of robes
    offset = (16, 0)
    x = base[0] - i * 16
    y = base[1]
    robes.append(((x, y), offset))

weapons = []
base = (-256, -224)
for i in range(24):
    offset = (-16, 0)
    x = base[0] - i * 16
    y = base[1]
    weapons.append(((x,y), offset))


