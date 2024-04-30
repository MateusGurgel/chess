from game_controller import GameController
from pieces.bishop import Bishop
from pieces.horse import Horse
from pieces.king import King
from pieces.pawn import Pawn
from pieces.queen import Queen
from pieces.tower import Tower
from standard_chess_grid import StandardChessGrid
from house import House
import os

chessGrid = StandardChessGrid()
gameController = GameController(chessGrid, [1,2])

Tower(chessGrid, House("A1"), 1)
Pawn(chessGrid, House("A2"), 1)

Horse(chessGrid, House("B1"), 1)
Pawn(chessGrid, House("B2"), 1)

Bishop(chessGrid, House("C1"), 1)
Pawn(chessGrid, House("C2"), 1)

King(chessGrid, House("D1"), 1)
Pawn(chessGrid, House("D2"), 1)

Queen(chessGrid, House("E1"), 1)
Pawn(chessGrid, House("E2"), 1)

Bishop(chessGrid, House("F1"), 1)
Pawn(chessGrid, House("F2"), 1)

Horse(chessGrid, House("G1"), 1)
Pawn(chessGrid, House("G2"), 1)

Tower(chessGrid, House("H1"), 1)
Pawn(chessGrid, House("H2"), 1)

while True:

    chessGrid.print()

    source_input = input("Qual peça você quer mexer?: ")
    source = House(source_input)

    destination_input = input("Qual é o destino?: ")
    destination = House(destination_input)

    if not gameController.move_piece(source, destination):
        input()

    os.system("cls")

    


