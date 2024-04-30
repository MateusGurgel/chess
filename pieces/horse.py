from grid import Grid
from house import House
from pieces.piece import Piece
from utils.relative_house import get_attacked_relative_houses, get_valid_relative_house

from utils.trace_line import trace_attack_line, trace_movment_line

class Horse(Piece):

    def __init__(self, grid: Grid, location: House, team: int):
        self.location = location

        self.grid = grid
        self.grid.add_content(location, self)
        
        self.team = team

    def __str__(self):
        return "6"

    def set_location(self, location: House):
        self.location = location


    def get_legal_moves_position(self):

        positions = []

        positions.extend(get_attacked_relative_houses(self.grid, self.location, 2, 1, self.team))
        positions.extend(get_attacked_relative_houses(self.grid, self.location, 2, -1, self.team))
        positions.extend(get_attacked_relative_houses(self.grid, self.location, -2, 1, self.team))
        positions.extend(get_attacked_relative_houses(self.grid, self.location, -2, -1, self.team))
        positions.extend(get_attacked_relative_houses(self.grid, self.location, -1, 2, self.team))
        positions.extend(get_attacked_relative_houses(self.grid, self.location, 1, 2, self.team)) 
        positions.extend(get_attacked_relative_houses(self.grid, self.location, -1, -2, self.team))
        positions.extend(get_attacked_relative_houses(self.grid, self.location, 1, -2, self.team))  






        return positions