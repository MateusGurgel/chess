from unittest import TestCase

from game_controller import GameController
from house import House
from pieces.horse import Horse
from pieces.pawn import Pawn
from standard_chess_grid import StandardChessGrid

class HorseMovmentTest(TestCase):
    def setUp(self) -> None:
        self.chessGrid = StandardChessGrid()
        self.gameController = GameController(self.chessGrid, [1,2])

    def test_legal_movments(self):
        horse = Horse(self.chessGrid, House("D4"), 1)
        self.chessGrid.print()
        positions =  [str(position) for position in horse.get_legal_moves_position()]
        validPositions = ["B3", "B5", "F3", "F5", "E6", "C6", "E2", "C2"]

        self.assertCountEqual(positions, validPositions)

    def test_legal_attacks(self):
        tower = Horse(self.chessGrid, House("D4"), 1)
        Pawn(self.chessGrid, House("B3"), 1)
        Pawn(self.chessGrid, House("B5"), 2)
        positions =  [str(position) for position in tower.get_legal_moves_position()]
    
        self.assertIn("B5", positions)
        self.assertNotIn("B3", positions)



