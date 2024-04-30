from unittest import TestCase

from game_controller import GameController
from house import House
from pieces.king import King
from pieces.pawn import Pawn

from standard_chess_grid import StandardChessGrid


class KingMovmentTest(TestCase):
    def setUp(self) -> None:
        self.chessGrid = StandardChessGrid()
        self.gameController = GameController(self.chessGrid, [1, 2])

    def test_legal_movments(self):
        king = King(self.chessGrid, House("D4"), 1)
        positions = [str(position) for position in king.get_legal_moves_position()]
        validPositions = ["C3", "D3", "E3", "C4", "E4", "C5", "D5", "E5"]

        self.assertCountEqual(positions, validPositions)

    def test_legal_attacks(self):
        tower = King(self.chessGrid, House("D4"), 1)
        Pawn(self.chessGrid, House("D3"), 1)
        Pawn(self.chessGrid, House("D5"), 2)
        Pawn(self.chessGrid, House("E5"), 1)
        Pawn(self.chessGrid, House("C5"), 2)
        positions = [str(position) for position in tower.get_legal_moves_position()]

        self.assertIn("D5", positions)
        self.assertNotIn("D3", positions)
        self.assertIn("D5", positions)
        self.assertNotIn("D3", positions)
