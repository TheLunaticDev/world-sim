import singleton


def get_cell_coord_from_mouse(pos):
    if pos[0] < 20 or pos[1] < 20:
        return None
    if pos[0] > 520 or pos[1] > 520:
        return None
    cell_x = (pos[0] - 20) // singleton.cell_size
    cell_y = (pos[1] - 20) // singleton.cell_size
    return (cell_x, cell_y)
