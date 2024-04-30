from typing import List
from grid import Grid
from house import House

class GameController:

    def __init__(self, grid: Grid, teams: List[int]):
        self.grid = grid

    def move_piece(self, source: House, destination: House):

        if self.grid.is_empty(source):
            print("Você não pode mover uma peça vazia")
            return False
        
        if not self.grid.is_valid_house(source):
            print("A origem tem que ser uma casa válida")
            return False
        
        if not self.grid.is_valid_house(source):
            print("Você não pode mover para uma casa inválida")
            return False

        piece = self.grid.get_content(source)

        moves = [str(move) for move in piece.get_legal_moves_position()]

        if str(destination) not in moves:
            print("Você não pode fazer um movmento ilegal")
            return False
        
        piece.set_location(destination)
        self.grid.move_content(source, destination)
        return True

    def print(self):
        self.grid.print()