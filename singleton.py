World = None
cell_size = None
options = {}
world_timer = None
score = 0
font = None
age = 0
complexity = 'E'
world_timer_speed = 2
world_timer_speeds = ['Very Slow', 'Slow', 'Normal', 'Fast', 'Very Fast']
entities = ['Plankton', 'Protists', 'Hominins']
entity_selected = 0


def change_selected_entity(type):
    global entity_selected
    if type is True:
        entity_selected += 1
        if entity_selected > 1:
            entity_selected = 0
    elif type is False:
        entity_selected -= 1
        if entity_selected < 0:
            entity_selected = 1


def change_world_timer_speed(type):
    global world_timer_speed
    if type is True:
        world_timer_speed += 1
        if world_timer_speed > 4:
            world_timer_speed = 0
    elif type is False:
        world_timer_speed -= 1
        if world_timer_speed < 0:
            world_timer_speed = 4


def get_timer_modifier():
    global world_timer_speed
    match(world_timer_speed):
        case 0:
            return 1.5
        case 1:
            return 1.25
        case 2:
            return 1
        case 3:
            return 0.5
        case 4:
            return 0.25
    return 0
