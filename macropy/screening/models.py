import random


class Position:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Box:
    def __init__(self, left: int, top: int, width: int, height: int):
        self.left = left
        self.top = top
        self.right = left + width
        self.bottom = top + height

    @property
    def x(self) -> int:
        return random.randint(self.left, self.right)

    @property
    def y(self) -> int:
        return random.randint(self.top, self.bottom)
