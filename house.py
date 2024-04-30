class House:

    def __init__(self, house: str):

        columns = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}

        if len(house) != 2:
            raise ("Casa invalida")

        column = house[0].capitalize()
        row = house[1]

        if not row.isnumeric():
            raise ("The first char must be a number")

        if not column.isalpha():
            raise ("The second char must be aphabetic")

        column = columns[column]
        row = int(row)

        self.row = row - 1
        self.column = column

    def __str__(self):
        columns = ["A", "B", "C", "D", "E", "F", "G", "H"]
        return columns[self.column] + str(self.row + 1)

    def set_row(self, row: int):
        self.row = row

    def set_column(self, column: int):
        self.column = column

    def add_row(self, number: int):
        self.row += number

    def add_column(self, number: int):
        self.column += number