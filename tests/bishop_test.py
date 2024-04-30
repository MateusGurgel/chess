from unittest import TestCase

from game_controller import GameController
from house import House
from pieces.bishop import Bishop
from pieces.pawn import Pawn
from standard_chess_grid import StandardChessGrid

class TowerMovmentTest(TestCase):
    def setUp(self) -> None:
        self.chessGrid = StandardChessGrid()
        self.gameController = GameController(self.chessGrid, [1,2])

    def test_legal_movments(self):
        bishop = Bishop(self.chessGrid, House("D4"), 1)
        self.chessGrid.print()
        positions =  [str(position) for position in bishop.get_legal_moves_position()]
        validPositions = ["C3", "B2", "A1", "E3", "F2", "G1", "E5", "F6", "G7", "H8", "C5", "B6", "A7"]

        self.assertCountEqual(positions, validPositions)

    def test_legal_attacks(self):
        tower = Bishop(self.chessGrid, House("D4"), 1)
        Pawn(self.chessGrid, House("E5"), 1)
        Pawn(self.chessGrid, House("C5"), 2)
        positions =  [str(position) for position in tower.get_legal_moves_position()]
    
        self.assertIn("C5", positions)
        self.assertNotIn("E5", positions)



