"""test_scores.py
"""

import unittest
from cli.scores import Scores
from cli.user import User


class TestScores(unittest.TestCase):
    def setUp(self):
        self.test_score = Scores("data/test_scores.json")

    def test_init_scores_file_not_empty(self):
        current = self.test_score
        notexpected = {}
        self.assertNotEqual(current, notexpected, f"scores not expected to be empty")
        self.assertIsInstance(current, Scores, f"object types don't match")
        self.assertIsInstance(current.scores, dict, f"object types don't match")
