from unittest import TestCase

from game_controller import GameController
from house import House
from pieces.pawn import Pawn
from standard_chess_grid import StandardChessGrid

class PawnMovmentTest(TestCase):
    def setUp(self) -> None:
        self.chessGrid = StandardChessGrid()
        self.gameController = GameController(self.chessGrid, [1,2])

    def test_initial_foward_movment(self):
        pawn = Pawn(self.chessGrid, House("D4"), 1)

        current_valid_moves =  [str(position) for position in pawn.get_legal_moves_position()]
        valid_moves = ["D5", "D6"]

        self.assertEqual(current_valid_moves, valid_moves, "The initial pawn movment is wrong")

    def test_foward_movment(self):
        pawn = Pawn(self.chessGrid, House("D4"), 1)
        pawn.was_moved = True

        current_valid_moves =  [str(position) for position in pawn.get_legal_moves_position()]
        valid_moves = ["D5"]

        self.assertEqual(current_valid_moves, valid_moves, "The foward pawn movment is wrong")

    def test_left_attack(self):
        pawn = Pawn(self.chessGrid, House("D4"), 1)
        Pawn(self.chessGrid, House("E5"), 2)

        current_valid_moves =  [str(position) for position in pawn.get_legal_moves_position()]

        for position in current_valid_moves:
            print(position)

        self.assertIn("E5", current_valid_moves, "The pawn was not able to attack on the left side")
    
    def test_right_attack(self):
        pawn = Pawn(self.chessGrid, House("D4"), 1)
        Pawn(self.chessGrid, House("C5"), 2)

        current_valid_moves =  [str(position) for position in pawn.get_legal_moves_position()]

        self.assertIn("C5", current_valid_moves, "The pawn was not able to attack on the rightw side")



