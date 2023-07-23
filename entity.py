import singleton
import random


class Entity:
    def __init__(self, name='entity', life=10, posx=0, posy=0,
                 color='#282a36', tags=[]):
        self.life = life
        self.name = name
        self.pos = [posx, posy]
        self.color = color
        self.tags = tags

    def act(self, id):
        pass

    def reproduce(self, id):
        pass


class Ether(Entity):
    grand_ether = 100

    def __init__(self, name='Ether', life=1000, posx=0, posy=0,
                 color='#282a36', tags=[]):
        super().__init__(name, life, posx, posy, color, tags)


class Plankton(Entity):
    def __init__(self, name='Plankton', life=10, posx=0, posy=0,
                 color='#50fa7b', tags=['level-0']):
        super().__init__(name, life, posx, posy, color, tags)

    def act(self, i, j, id, to_be_removed=[], to_be_added=[]):
        entity_cram = 0
        for id, entity in enumerate(singleton.World.world[i][j]):
            if entity is not None:
                if isinstance(entity, Plankton):
                    entity_cram += 1

        if entity_cram > 1:
            for id, entity in enumerate(singleton.World.world[i][j]):
                entity_cram -= 1
                if entity_cram:
                    if entity is not None:
                        if isinstance(entity, Plankton):
                            to_be_removed.append((i, j, id))
                    else:
                        break
        surrounding_count = 0
        try:
            for entity in singleton.World.world[i-1][j-1]:
                if isinstance(entity, Plankton):
                    surrounding_count += 1
            for entity in singleton.World.world[i][j-1]:
                if isinstance(entity, Plankton):
                    surrounding_count += 1
            for entity in singleton.World.world[i+1][j-1]:
                if isinstance(entity, Plankton):
                    surrounding_count += 1
            for entity in singleton.World.world[i-1][j]:
                if isinstance(entity, Plankton):
                    surrounding_count += 1
            for entity in singleton.World.world[i+1][j]:
                if isinstance(entity, Plankton):
                    surrounding_count += 1
            for entity in singleton.World.world[i-1][j+1]:
                if isinstance(entity, Plankton):
                    surrounding_count += 1
            for entity in singleton.World.world[i][j+1]:
                if isinstance(entity, Plankton):
                    surrounding_count += 1
            for entity in singleton.World.world[i+1][j+1]:
                if isinstance(entity, Plankton):
                    surrounding_count += 1
        except IndexError:
            pass

        if surrounding_count >= 2:
            try:
                for entity in singleton.World.world[i-1][j-1]:
                    if isinstance(entity, Plankton):
                        break
                to_be_added.append((
                    Plankton(i-1, j-1), i-1, j-1))
                for entity in singleton.World.world[i][j-1]:
                    if isinstance(entity, Plankton):
                        break
                    to_be_added.append((
                        Plankton(i, j-1), i, j-1))
                for entity in singleton.World.world[i+1][j-1]:
                    if isinstance(entity, Plankton):
                        break
                    to_be_added.append((
                        Plankton(i+1, j-1), i+1, j-1))
                for entity in singleton.World.world[i-1][j]:
                    if isinstance(entity, Plankton):
                        break
                    to_be_added.append((
                        Plankton(i-1, j), i-1, j))
                for entity in singleton.World.world[i+1][j]:
                    if isinstance(entity, Plankton):
                        break
                    to_be_added.append((
                        Plankton(i+1, j), i+1, j))
                for entity in singleton.World.world[i-1][j+1]:
                    if isinstance(entity, Plankton):
                        break
                    to_be_added.append((
                        Plankton(i-1, j+1), i-1, j+1))
                for entity in singleton.World.world[i][j+1]:
                    if isinstance(entity, Plankton):
                        break
                    to_be_added.append((
                        Plankton(i, j+1), i, j+1))
                for entity in singleton.World.world[i+1][j+1]:
                    if isinstance(entity, Plankton):
                        break
                    to_be_added.append((
                        Plankton(i+1, j+1), i+1, j+1))
            except IndexError:
                pass

    def reproduce(self, id):
        pass


class Protists(Entity):
    def __init__(self, sex, name='Protists', life=20, posx=0, posy=0,
                 color='#ff79c6', tags=['level-1']):
        super().__init__(name, life, posx, posy, color, tags)
        self.sex = sex

    def act(self, i, j, id, to_be_removed=[], to_be_added=[]):
        # new_object = Protists(
        #     singleton.World.world[i][j][id].sex,
        #     posx=i+1, posy=j+1)
        # to_be_removed.append((i, j, id))
        # to_be_added.append((new_object, i+1, j+1))
        pass

    def reproduce(self, id):
        pass


class Hominins(Entity):
    def __init__(self, sex, name='Hominins', life=40, posx=0, posy=0,
                 color='#ff5555', tags=['level-2']):
        super().__init__(name, life, posx, posy, color, tags)
        self.sex = sex

    def act(self):
        pass

    def reproduce(self):
        pass


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
