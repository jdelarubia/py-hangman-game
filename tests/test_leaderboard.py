"""test_leaderboard.py
"""

import unittest
from cli.leaderboard import Leaderboard
from cli.player import Player


class TestLeaderboard(unittest.TestCase):
    def setUp(self):
        self.test_score = Leaderboard("data/test_scores.json")

    def test_init_scores_file_not_empty(self):
        current = self.test_score
        notexpected = {}
        self.assertNotEqual(current, notexpected, f"scores not expected to be empty")
        self.assertIsInstance(current, Leaderboard, f"object types don't match")
        self.assertIsInstance(current.leaderboard, dict, f"object types don't match")
