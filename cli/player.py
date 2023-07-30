"""player.py
"""


class Player:
    def __init__(self, nickname: str, score: int) -> None:
        self._nickname = nickname.lower()
        self._score = score

    @property
    def nickname(self) -> str:
        return self._nickname

    @property
    def score(self) -> int:
        return self._score

    @score.setter
    def score(self, new_score: int) -> int:
        self._score = new_score

    def add_score(self, points: int):
        self._score += points
