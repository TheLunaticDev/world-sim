import pygame
import singleton
import pygame.freetype
import world
import math
import utility
import entity

timerStopped = False


def main_loop():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                handle_mouse_input()

            handle_world_timer(event)

            if event.type == pygame.USEREVENT:
                world.calculate_next_world()

        pygame.display.get_surface().fill(
            singleton.options['Display']['background_color']
        )
        render_grid()
        render_score()
        render_age()
        render_complexity()
        render_world_status()
        render_world_timer_control_panel()
        render_entity_control_panel()
        render_entity_control_panel_previous()
        render_all_entities()
        pygame.display.flip()


def render_grid():
    render_box()
    render_horizontal_lines()
    render_vertical_lines()


def render_box():
    pygame.draw.rect(
        pygame.display.get_surface(),
        singleton.options['Display']['line_color'],
        pygame.Rect(20, 20, 500, 500), 1
    )


def render_vertical_lines():
    for i in range(singleton.options['World']['size'] - 1):
        pygame.draw.line(pygame.display.get_surface(),
                         singleton.options['Display']['line_color'],
                         (20 + (500/singleton.options['World']['size'])
                          * (i+1), 20),
                         (20 + (500/singleton.options['World']['size'])
                          * (i + 1), 19 + 500))


def render_horizontal_lines():
    for i in range(singleton.options['World']['size'] - 1):
        pygame.draw.line(pygame.display.get_surface(),
                         singleton.options['Display']['line_color'],
                         (20, 20 + (500/singleton.options['World']['size'])
                          * (i+1)),
                         (20 + 499,
                          20 + (500/singleton.options['World']['size'])
                          * (i + 1)))


def handle_world_timer(event):
    global timerStopped
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE and not timerStopped:
            singleton.world_timer = pygame.time.set_timer(
                pygame.USEREVENT, 0
            )
            timerStopped = True

        elif event.key == pygame.K_SPACE and timerStopped:
            singleton.world_timer = pygame.time.set_timer(
                pygame.USEREVENT, 1000
            )
            timerStopped = False


def render_score():
    pygame.draw.rect(
        pygame.display.get_surface(),
        singleton.options['Display']['line_color'],
        pygame.Rect(540, 20, 240, 100), 1
    )
    singleton.font.render_to(pygame.display.get_surface(),
                             (700, 30),
                             'Score',
                             singleton.options['Display']['line_color'])
    singleton.font.render_to(pygame.display.get_surface(),
                             (550, 85),
                             str(singleton.score),
                             singleton.options['Display']['line_color'])


def render_age():
    pygame.draw.rect(
        pygame.display.get_surface(),
        singleton.options['Display']['line_color'],
        pygame.Rect(540, 140, 240, 100), 1
    )
    singleton.font.render_to(pygame.display.get_surface(),
                             (725, 150),
                             'Age',
                             singleton.options['Display']['line_color'])
    singleton.font.render_to(pygame.display.get_surface(),
                             (550, 205),
                             str(singleton.age),
                             singleton.options['Display']['line_color'])


def render_complexity():
    pygame.draw.rect(
        pygame.display.get_surface(),
        singleton.options['Display']['line_color'],
        pygame.Rect(540, 260, 240, 50), 1
    )
    singleton.font.render_to(pygame.display.get_surface(),
                             (550, 270),
                             'Complexity',
                             singleton.options['Display']['line_color'])
    singleton.font.render_to(pygame.display.get_surface(),
                             (755, 270),
                             singleton.complexity,
                             singleton.options['Display']['line_color'])


def render_world_timer_control_panel():
    pygame.draw.rect(
        pygame.display.get_surface(),
        singleton.options['Display']['line_color'],
        pygame.Rect(540, 330, 240, 50), 1
    )
    singleton.font.render_to(pygame.display.get_surface(),
                             (550, 340),
                             singleton.world_timer_speeds[
                                 singleton.world_timer_speed],
                             singleton.options['Display']['line_color'])


def render_world_status():
    if timerStopped is True:
        singleton.font.render_to(pygame.display.get_surface(),
                                 (175, 175),
                                 'World Stopped!',
                                 '#ff5555'
                                 )


def render_entity_control_panel():
    pygame.draw.rect(
        pygame.display.get_surface(),
        singleton.options['Display']['line_color'],
        pygame.Rect(540, 400, 240, 50), 1
    )
    singleton.font.render_to(pygame.display.get_surface(),
                             (550, 410),
                             singleton.entities[singleton.entity_selected],
                             singleton.options['Display']['line_color'])


def render_entity_control_panel_previous():
    pygame.draw.rect(
        pygame.display.get_surface(),
        singleton.options['Display']['line_color'],
        pygame.Rect(540, 470, 240, 50), 1
    )
    singleton.font.render_to(pygame.display.get_surface(),
                             (625, 480),
                             'Back',
                             singleton.options['Display']['line_color'])


def handle_mouse_input():
    mouse = pygame.mouse.get_pressed()
    if mouse[0]:
        pos = pygame.mouse.get_pos()
        if (540 <= pos[0] <= 780) and (330 <= pos[1] <= 380):
            singleton.change_world_timer_speed(True)
            pygame.time.set_timer(
                pygame.USEREVENT,
                int(singleton.options['World']['speed'] *
                    singleton.get_timer_modifier()))
        if (540 <= pos[0] <= 780) and (400 <= pos[1] <= 450):
            singleton.change_selected_entity(True)
        if (20 <= pos[0] <= 520) and (20 <= pos[1] <= 520):
            create_entity(pos)

    if mouse[2]:
        pos = pygame.mouse.get_pos()
        if (540 <= pos[0] <= 780) and (330 <= pos[1] <= 380):
            singleton.change_world_timer_speed(False)
            pygame.time.set_timer(
                pygame.USEREVENT,
                int(singleton.options['World']['speed'] *
                    singleton.get_timer_modifier()))
        if (540 <= pos[0] <= 780) and (400 <= pos[1] <= 450):
            singleton.change_selected_entity(False)


def render_all_entities():
    for i in range(len(singleton.World.world)):
        for j in range(len(singleton.World.world[i])):
            render_top_entity(i, j)


def render_top_entity(posx, posy):
    location = singleton.World.world[posx][posy]
    if len(location) == 0:
        return
    render_object = location[-1]
    margin = math.floor(singleton.cell_size * 0.2)
    pygame.draw.rect(
        pygame.display.get_surface(),
        render_object.color,
        ((20 + singleton.cell_size * posx) + margin,
         (20 + singleton.cell_size * posy) + margin,
         singleton.cell_size - (margin * 2),
         singleton.cell_size - (margin * 2)))


def create_entity(pos):
    cell = utility.get_cell_coord_from_mouse(pos)
    new_entity = entity.get_entity(cell)
    singleton.World.add(new_entity, int(cell[0]), int(cell[1]))
