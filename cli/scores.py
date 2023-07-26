"""scores.py
"""
import json


class Scores:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self._scores = self.load()

    @property
    def scores(self) -> dict:
        return dict(
            sorted(self._scores.items(), key=lambda item: item[1], reverse=True)
        )

    def load(self) -> None:
        with open(self.filename, "r") as scores:
            scores = json.load(scores)
        return scores

    def save(self) -> None:
        with open(self.filename, "w") as scores:
            json.dump(self.scores, scores, indent=4)

    def __repr__(self) -> str:
        current_scores = (
            """LEADER BOARD TABLE\n"""
            """nickname | current score\n"""
            """************************\n"""
        )
        for nickname, current_score in self.scores.items():
            current_scores += f"{nickname:<10} {current_score:>6}\n"
        return current_scores
