class Game:

    def __init__(self, rows, cols):

        self.rows = rows
        self.cols = cols

        self.field = [
            [False for _ in range(cols)]
            for _ in range(rows)
        ]

    def count_neighbors(self, row, col):

        count = 0

        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):

                if dx == 0 and dy == 0:
                    continue

                r = row + dy
                c = col + dx

                if 0 <= r < self.rows and 0 <= c < self.cols:

                    if self.field[r][c]:
                        count += 1

        return count

    def step(self):

        new_field = [
            [False for _ in range(self.cols)]
            for _ in range(self.rows)
        ]

        for row in range(self.rows):
            for col in range(self.cols):

                neighbors = self.count_neighbors(row, col)

                if self.field[row][col]:
                    new_field[row][col] = neighbors in (2, 3)
                else:
                    new_field[row][col] = neighbors == 3

        self.field = new_field