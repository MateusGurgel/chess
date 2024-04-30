import copy
from typing import List
from grid import Grid
from house import House


def get_attacked_relative_houses(grid: Grid, source: House, row: int, col: int, team) -> List[House]:
    relative_house = get_valid_relative_house(grid, source, row, col)

    if not relative_house:
        return []
    
    if not grid.is_empty(relative_house) and grid.get_content(relative_house).team == team:
        return []
    
    return [relative_house]
        
    



def get_valid_relative_house(grid: Grid, source: House, row: int, col: int) -> House:
    relative_house = copy.copy(source)
    relative_house.add_row(row)
    relative_house.add_column(col)

    if not grid.is_valid_house(source):
        return None

    return relative_house
    