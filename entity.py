import singleton
import random


class Entity:
    def __init__(self, name='entity', life=10, posx=0, posy=0,
                 color='#282a36', tags=[]):
        self.life = life
        self.name = name
        self.pos = (posx, posy)
        self.color = color
        self.tags = tags


class Ether(Entity):
    grand_ether = 100

    def __init__(self, name='Ether', life=1000, posx=0, posy=0, color='#282a36',
                 tags=[]):
        super().__init__(name, life, posx, posy, color, tags)


class Plankton(Entity):
    def __init__(self, name='Plankton', life=10, posx=0, posy=0,
                 color='#50fa7b', tags=['level-0']):
        super().__init__(name, life, posx, posy, color, tags)


class Protists(Entity):
    def __init__(self, sex, name='Protists', life=20, posx=0, posy=0,
                 color='#ff79c6', tags=['level-1']):
        super().__init__(name, life, posx, posy, color, tags)
        self.sex = sex


class Hominins(Entity):
    def __init__(self, sex, name='Hominins', life=40, posx=0, posy=0,
                 color='#ff5555', tags=['level-2']):
        super().__init__(name, life, posx, posy, color, tags)
        self.sex = sex


def get_entity(cell):
    selected = singleton.entity_selected
    entity = None
    if selected == 0:
        entity = Plankton(posx=cell[0], posy=cell[1])
    if selected == 1:
        gender = random.randint(0, 1)
        if gender:
            gender = 'Female'
        else:
            gender = 'Male'
        entity = Protists(gender, posx=cell[0], posy=cell[1])
    return entity
