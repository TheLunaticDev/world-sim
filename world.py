import singleton


class World:
    def __init__(self, size):
        self.world = [[] for _ in range(size)]
        for i in range(size):
            self.world[i] = [[] for _ in range(size)]

    def add(self, entity, posx, posy):
        self.world[posx][posy].append(entity)


def calculate_next_world():
    singleton.age += 1
    update_complexity()
    update_score()
    reduce_life_all()
    kill_entities_with_no_life()


def get_total_entity_count():
    total_entity_count = 0
    for i in range(len(singleton.World.world)):
        for j in range(len(singleton.World.world[i])):
            entities_in_location = len(singleton.World.world[i][j])
            total_entity_count += entities_in_location
    return total_entity_count



def update_complexity():
    total_distinct_entity_count = 0
    for i in range(len(singleton.World.world)):
        for j in range(len(singleton.World.world[i])):
            entities_in_location = len(singleton.World.world[i][j])
            if entities_in_location > 0:
                total_distinct_entity_count += 1
    coverage = ((total_distinct_entity_count /
                 (singleton.options['World']['size'] ** 2)) * 100)
    if (0.0 <= coverage <= 20.0):
        singleton.complexity = 'E'
    if (21.0 <= coverage <= 40.0):
        singleton.complexity = 'D'
    if (41.0 <= coverage <= 60.0):
        singleton.complexity = 'C'
    if (61.0 <= coverage <= 80.0):
        singleton.complexity = 'B'
    if (81.0 <= coverage <= 100.0):
        singleton.complexity = 'A'


def update_score():
    entites = get_total_entity_count()
    complexity = singleton.complexity
    if complexity == 'E':
        complexity = 1
    if complexity == 'D':
        complexity = 1.25
    if complexity == 'C':
        complexity = 1.5
    if complexity == 'B':
        complexity = 1.75
    if complexity == 'A':
        complexity = 2

    value = entites * complexity
    singleton.score += value


def reduce_life_all():
    for i in range(len(singleton.World.world)):
        for j in range(len(singleton.World.world[i])):
            for entity in singleton.World.world[i][j]:
                if entity is not None:
                    entity.life -= 1


def kill_entities_with_no_life():
    for i in range(len(singleton.World.world)):
        for j in range(len(singleton.World.world[i])):
            for id, entity in enumerate(singleton.World.world[i][j]):
                if entity is not None:
                    if entity.life <= 0:
                        del singleton.World.world[i][j][id]
