class Player1:
    def __init__(self, x, y, dy, canMoveUp, canMoveDown, score):
        self.x = x
        self.y = y
        self.dy = dy
        self.canMoveUp = canMoveUp
        self.canMoveDown = canMoveDown
        self.score = score

    def moveUp(self):
        self.y -= self.dy

    def moveDown(self):
        self.y += self.dy


class Player2:
    def __init__(self, x, y, dy, canMoveUp, canMoveDown, score):
        self.x = x
        self.y = y
        self.dy = dy
        self.canMoveUp = canMoveUp
        self.canMoveDown = canMoveDown
        self.score = score

    def moveUp(self):
        self.y -= self.dy

    def moveDown(self):
        self.y += self.dy
