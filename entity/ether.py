import Entity


class Ether(Entity.Entity):
    grand_ether = 100

    def __init__(self, name='ether-entity', life=100,
                 posx=0, posy=0, tags=['Invisible',
                                       'non-beneficial']):
        super().__init__(name, life, posx, posy, tags)
