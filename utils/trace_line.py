from grid import Grid
from house import House
from typing import List, Tuple
import copy

def move_in_direction(source: House,  direction: Tuple[int, int]):
    source.add_row(direction[0])
    source.add_column(direction[1])

def trace_movment_line(table: Grid, source: House, direction: Tuple[int, int], length) -> List[House]:
    points = []
    currentLocaiton = copy.copy(source)

    for house in range(length):
        move_in_direction(currentLocaiton, direction)

        if not table.is_valid_house(currentLocaiton):
            break

        if not table.is_empty(currentLocaiton):
            break

        points.append(copy.copy(currentLocaiton))

    return points

def trace_attack_line(table: Grid, source: House, direction: Tuple[int, int], length, team: int) -> List[House]:
    points = []
    currentLocaiton = copy.copy(source)

    for house in range(length):
        move_in_direction(currentLocaiton, direction)

        if not table.is_valid_house(currentLocaiton):
            break

        if not table.is_empty(currentLocaiton):

            piece = table.get_content(currentLocaiton)

            if piece.team != team:
                points.append(copy.copy(currentLocaiton))
            
            break

        points.append(copy.copy(currentLocaiton))

    return points






    