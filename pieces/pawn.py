from typing import Tuple
from grid import Grid
from house import House
from pieces.piece import Piece

from utils.trace_line import trace_attack_line, trace_movment_line

class Pawn(Piece):

    def __init__(self, grid: Grid, location: House, team: int):
        self.location = location
        self.was_moved = False

        self.orientation = (1, 0)
        self.left_attack_direction = (1 , -1)
        self.right_attack_direction = (1, 1)

        self.grid = grid
        self.grid.add_content(location, self)
        
        self.team = team


    def __str__(self):
        return "1"

    def set_location(self, location: House):
        self.was_moved = True
        self.location = location

    def check_attack(self, attack_array):

        if len(attack_array) != 1:
            return False
        
        attack_location = attack_array[0]
        
        if not self.grid.is_valid_house(attack_location):
            return False
        
        if self.grid.is_empty(attack_location):
            return False
        
        return self.grid.get_content(attack_location).team != self.team



    def get_legal_moves_position(self):
        movment_range = 2 if not self.was_moved else 1
        positions = []

        positions.extend(trace_movment_line(self.grid, self.location, self.orientation, movment_range))
        left_attack = trace_attack_line(self.grid, self.location, self.left_attack_direction, 1, self.team)
        right_attack = trace_attack_line(self.grid, self.location, self.right_attack_direction, 1, self.team)

        if self.check_attack(left_attack):
            positions.append(left_attack[0])

        if self.check_attack(right_attack):
            positions.append(right_attack[0])

        return positions