from unittest import TestCase

from game_controller import GameController
from house import House
from pieces.pawn import Pawn
from pieces.tower import Tower
from standard_chess_grid import StandardChessGrid

class TowerMovmentTest(TestCase):
    def setUp(self) -> None:
        self.chessGrid = StandardChessGrid()
        self.gameController = GameController(self.chessGrid, [1,2])

    def test_legal_movments(self):
        tower = Tower(self.chessGrid, House("D4"), 1)
        self.chessGrid.print()
        positions =  [str(position) for position in tower.get_legal_moves_position()]
        validPositions = ["D5", "D6", "D7", "D8", "D3", "D2", "D1", "E4", "F4", "G4", "H4", "C4", "B4", "A4"]

        self.assertCountEqual(positions, validPositions)

    def test_legal_attacks(self):
        tower = Tower(self.chessGrid, House("D4"), 1)
        Pawn(self.chessGrid, House("D3"), 1)
        Pawn(self.chessGrid, House("D5"), 2)
        positions =  [str(position) for position in tower.get_legal_moves_position()]
    
        self.assertIn("D5", positions)
        self.assertNotIn("D3", positions)



