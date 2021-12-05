class Line:
    def __init__(self, x1: int, y1: int, x2: int, y2: int):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.s_point = (x1, y1)
        self.e_point = (x2, y2)

    def __str__(self):
        return f"s_point:{self.s_point}, e_point:{self.e_point}"

    def draw_line(self, matrix):
        # if x is the same, draw vertical line in matrix, starting point is x,y1, ending point x,y2
        if self.x1 == self.x2:
            y1 = min(self.y1, self.y2)
            y2 = max(self.y1, self.y2)
            for i in range(y1, y2 + 1):
                matrix[self.x1][i] += 1
        # if y is the same, draw horizontal line in matrix, starting point is x1,y, ending point x2,y
        elif self.y1 == self.y2:
            x1 = min(self.x1, self.x2)
            x2 = max(self.x1, self.x2)
            for i in range(x1, x2 + 1):
                matrix[i][self.y1] += 1
        # draw diagonal line, move x(x1->X2), y(y1->y2) at same time
        elif abs(self.x1 - self.x2) == abs(self.y1 - self.y2):
            diff = abs(self.x1 - self.x2)
            for i in range(0, diff + 1):
                if self.x1 < self.x2 and self.y1 < self.y2:
                    matrix[self.x1 + i][self.y1 + i] += 1
                if self.x1 < self.x2 and self.y1 > self.y2:
                    matrix[self.x1 + i][self.y1 - i] += 1
                if self.x1 > self.x2 and self.y1 > self.y2:
                    matrix[self.x1 - i][self.y1 - i] += 1
                if self.x1 > self.x2 and self.y1 < self.y2:
                    matrix[self.x1 - i][self.y1 + i] += 1
        return matrix
