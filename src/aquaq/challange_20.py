from typing import Literal, cast

CardRank = Literal["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]


class Card:
    __slots__ = "rank"
    rank: CardRank

    def __init__(self, rank: str) -> None:
        self.rank = cast(CardRank, rank)

    @property
    def value(self) -> list[int]:
        match self.rank:
            case "A":
                return [1, 11]
            case "J" | "Q" | "K":
                return [10]
            case r:
                return [int(r)]

    def __repr__(self) -> str:
        return self.rank


class Hand:
    __slots__ = "cards", "values"
    cards: list[Card]
    values: list[int]

    def __init__(self) -> None:
        self.reset()

    def is_winning(self) -> bool:
        return any(v == 21 for v in self.values)

    def is_losing(self) -> bool:
        return all(v > 21 for v in self.values)

    def reset(self):
        self.cards = []
        self.values = [0]

    def add(self, card: Card):
        self.cards.append(card)
        self.values = [v + value for v in self.values for value in card.value]

    def __repr__(self) -> str:
        return "[" + ", ".join(str(c) for c in self.cards) + "]"


def solve_20(file: str) -> int:
    hand = Hand()
    solution = 0
    for card in file.split(" "):
        hand.add(Card(card))
        if hand.is_winning():
            solution += 1
            hand.reset()
        if hand.is_losing():
            hand.reset()
    return solution
