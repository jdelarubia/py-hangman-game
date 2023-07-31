"""player.py
"""


class Player:
    def __init__(self, nickname: str, wins: int = 0, losses: int = 0) -> None:
        self._nickname = nickname.lower()
        self._wins = wins
        self._losses = losses

    @property
    def nickname(self) -> str:
        return self._nickname

    @property
    def wins(self) -> int:
        return self._wins

    @wins.setter
    def score(self, new_wins: int) -> int:
        self._wins = new_wins

    def add_win(self):
        self._wins += 1

    def add_lose(self):
        self._losses += 1
