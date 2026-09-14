from typing import Literal, cast

type Direction = Literal["L", "R", "U", "D"]


class Dice:
    def __init__(self, front: int, left: int, top: int) -> None:
        self.front = front
        self.left = left
        self.top = top
        self.back = 7 - front
        self.right = 7 - left
        self.bottom = 7 - top

    def rotate(self, direction: Direction):
        front = self.front
        match direction:
            case "L":
                self.front = self.right
                self.right = self.back
                self.back = self.left
                self.left = front
            case "R":
                self.front = self.left
                self.left = self.back
                self.back = self.right
                self.right = front
            case "U":
                self.front = self.bottom
                self.bottom = self.back
                self.back = self.top
                self.top = front
            case "D":
                self.front = self.top
                self.top = self.back
                self.back = self.bottom
                self.bottom = front


def solve_05(file: str) -> int:
    dice_1 = Dice(1, 2, 3)
    dice_2 = Dice(1, 3, 2)
    matching = []
    for i, direction in enumerate(file):
        direction = cast(Direction, direction)
        dice_1.rotate(direction)
        dice_2.rotate(direction)
        if dice_1.front == dice_2.front:
            matching.append(i)

    return sum(matching)
