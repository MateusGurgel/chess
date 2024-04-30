from typing import Any
from grid import Grid
from house import House


class StandardChessGrid(Grid):

    def __init__(self):
        self.table = [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
        ]

    def move_content(self, source: House, destination: House):

        if self.table[source.row][source.column] == 0:
            raise ("The source cannot be empty")

        if self.table[destination.row][destination.column] != 0:
            raise ("The destination house is not empty")

        self.table[destination.row][destination.column] = self.table[source.row][
            source.column
        ]

        self.remove_content(source)

    def get_content(self, house: House):

        content = self.table[house.row][house.column]

        if content == 0:
            raise ("The house content is empty")

        return content
    
    def is_empty(self, house: House):
        return self.table[house.row][house.column] == 0
    
    def is_valid_house(self, house: House):

        is_row_valid = (house.row >= 0 and house.row < len(self.table))

        if not is_row_valid:
            return False

        is_col_valid = house.column >= 0 and house.column < len(self.table[house.row])

        return is_col_valid
    
    def print(self):
        print("   A  B  C  D  E  F  G  H  ")
        print("  -------------------------")
        for row in self.table:
            print("[", end="  ")
            for item in row:
                print(item, end="  ")
            print("]", end="  ")
            print("")
        print("  -------------------------")

    def remove_content(self, house: House):
        self.table[house.row][house.column] = 0

    def add_content(self, location: House, content: Any):

        if not self.is_empty(location):
            raise ("You cannot add something on a used house")
        
        self.table[location.row][location.column] = content
