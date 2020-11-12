class TicTacToeBoard:
    def __init__(self):
        self.field = [['-' for _ in range(3)] for _ in range(3)]
        self.end = 0
        self.turn = 1

    def new_game(self):
        self.field = [['-' for _ in range(3)] for _ in range(3)]

    def get_field(self):
        return self.field

    def check_field(self):
        if self.field[1 - 1][1 - 1] == self.field[2 - 1][1 - 1] == self.field[3 - 1][1 - 1] == 'X':
            return 'X'
        elif self.field[1 - 1][2 - 1] == self.field[2 - 1][2 - 1] == self.field[3 - 1][2 - 1] == 'X':
            return 'X'
        elif self.field[1 - 1][3 - 1] == self.field[2 - 1][3 - 1] == self.field[3 - 1][3 - 1] == 'X':
            return 'X'
        elif self.field[1 - 1][1 - 1] == self.field[1 - 1][2 - 1] == self.field[1 - 1][3 - 1] == 'X':
            return 'X'
        elif self.field[2 - 1][1 - 1] == self.field[2 - 1][2 - 1] == self.field[2 - 1][3 - 1] == 'X':
            return 'X'
        elif self.field[3 - 1][1 - 1] == self.field[3 - 1][2 - 1] == self.field[3 - 1][3 - 1] == 'X':
            return 'X'
        elif self.field[1 - 1][1 - 1] == self.field[2 - 1][2 - 1] == self.field[3 - 1][3 - 1] == 'X':
            return 'X'
        elif self.field[1 - 1][3 - 1] == self.field[2 - 1][2 - 1] == self.field[3 - 1][1 - 1] == 'X':
            return 'X'
        elif self.field[1 - 1][1 - 1] == self.field[2 - 1][1 - 1] == self.field[3 - 1][1 - 1] == '0':
            return 0
        elif self.field[1 - 1][2 - 1] == self.field[2 - 1][2 - 1] == self.field[3 - 1][2 - 1] == '0':
            return 0
        elif self.field[1 - 1][3 - 1] == self.field[2 - 1][3 - 1] == self.field[3 - 1][3 - 1] == '0':
            return 0
        elif self.field[1 - 1][1 - 1] == self.field[1 - 1][2 - 1] == self.field[1 - 1][3 - 1] == '0':
            return 0
        elif self.field[2 - 1][1 - 1] == self.field[2 - 1][2 - 1] == self.field[2 - 1][3 - 1] == '0':
            return 0
        elif self.field[3 - 1][1 - 1] == self.field[3 - 1][2 - 1] == self.field[3 - 1][3 - 1] == '0':
            return 0
        elif self.field[1 - 1][1 - 1] == self.field[2 - 1][2 - 1] == self.field[3 - 1][3 - 1] == '0':
            return 0
        elif self.field[1 - 1][3 - 1] == self.field[2 - 1][2 - 1] == self.field[3 - 1][1 - 1] == '0':
            return 0
        else:
            for i in self.field:
                for j in i:
                    if j == '-':
                        return 'None'
            else:
                return 'D'

    def make_move(self, row, col):
        if self.check_field() == 'None':
            if self.field[row - 1][col - 1] == '-':
                if self.turn % 2 == 1:
                    self.field[row - 1][col - 1] = 'X'
                    if self.check_field() == 'None':
                        self.turn += 1
                        return 'Продолжаем играть'
                    elif self.check_field() == 'D':
                        self.turn += 1
                        return 'Ничья'
                    elif self.check_field() == 'X':
                        self.turn += 1
                        return 'Победил игрок X'

                else:
                    self.field[row - 1][col - 1] = '0'
                    if self.check_field() == 'None':
                        self.turn += 1
                        return 'Продолжаем играть'
                    elif self.check_field() == 'D':
                        self.turn += 1
                        return 'Ничья'
                    elif self.check_field() == 0:
                        self.turn += 1
                        return 'Победил игрок 0'
            else:
                return 'Клетка ' + str(row) + ', ' + str(col) + ' уже занята'
        else:
            return 'Игра уже завершена'


board = TicTacToeBoard()
print(*board.get_field(), sep="\n")
print(board.make_move(1, 1))
print(*board.get_field(), sep="\n")
print(board.make_move(1, 1))
print(board.make_move(1, 2))
print(*board.get_field(), sep="\n")
print(board.make_move(2, 1))
print(board.make_move(2, 2))
print(board.make_move(3, 1))
print(board.make_move(2, 2))
print(*board.get_field(), sep="\n")