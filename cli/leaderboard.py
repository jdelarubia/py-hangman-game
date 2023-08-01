"""leaderboard.py
"""
import json


class Leaderboard:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self._leaderboard = self.load()

    @property
    def leaderboard(self) -> dict:
        return dict(
            sorted(self._leaderboard.items(), key=lambda item: item[1]["wins"], reverse=True)
        )

    def load(self) -> None:
        with open(self.filename, "r") as leaderboard:
            data = json.load(leaderboard)
        leaderboard = {}
        for player, score in data.items():
            leaderboard[player] = {"wins": score["wins"], "losses": score["losses"]}
        return leaderboard

    def save(self) -> None:
        with open(self.filename, "w") as lb_handler:
            json.dump(self.leaderboard, lb_handler, indent=4)

    def __repr__(self) -> str:
        current_leaderboard = (
            """LEADER BOARD TABLE\n""" """nickname    | score\n""" """*******************\n"""
        )
        for player, score in self.leaderboard.items():
            current_leaderboard += f"{player[:12]:<12} {score['wins']:>6}\n"
        return current_leaderboard
