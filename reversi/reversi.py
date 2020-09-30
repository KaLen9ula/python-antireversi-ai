FIELD_WIDTH = 8


class Reversi():
    def __init__(self):
        self.is_finished = False
        self.free_cells = 60
        self.field = [" " for i in range(64)]
        self.field[27] = "w"
        self.field[28] = "b"
        self.field[35] = "b"
        self.field[36] = "w"
        self.piece = " "
        self.current_player = "b"

    def turn(self):
        self.free_cells -= 1

    def check_up(self, cell):
        prev = False
        curr = self.field[cell]
        not_curr = "w" if curr == "b" else "b"
        for i in range(cell - FIELD_WIDTH, 0, -FIELD_WIDTH):
            up = self.field[i]
            if up == curr:
                return None
            if up == not_curr:
                prev = True
                continue
            if up == " " and prev is True:
                return i
            return None

    def check_down(self, cell):
        prev = False
        curr = self.field[cell]
        not_curr = "w" if curr == "b" else "b"
        for i in range(cell + FIELD_WIDTH, FIELD_WIDTH ** 2, FIELD_WIDTH):
            up = self.field[i]
            if up == curr:
                return None
            if up == not_curr:
                prev = True
                continue
            if up == " " and prev is True:
                return i
            return None

    def check_vertical(self, cell):
        moves = []
        up = self.check_up(cell)
        down = self.check_down(cell)
        if up is not None:
            moves.append(up)
        if down is not None:
            moves.append(down)
        return moves

    def next(self):
        if self.current_player == "b":
            pass
        else:
            self.current_player = "w"
        return self.current_player
