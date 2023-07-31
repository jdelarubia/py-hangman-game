import unittest
from cli.player import Player


class TestUser(unittest.TestCase):
    def setUp(self) -> None:
        self.test_user = Player(nickname="Johnny", wins=0, losses=0)

    def test_nickname_dont_match(self) -> None:
        current = self.test_user.nickname
        expected = "anything"
        with self.assertRaises(AssertionError):
            assert current == expected

    def test_nickname_match(self) -> None:
        current = self.test_user.nickname
        expected = "johnny"
        self.assertEqual(current, expected, f"nicknames don't match, {current} != {expected}")

    def test_initial_score_is_zero(self) -> None:
        current = self.test_user.wins
        expected = 0
        self.assertEqual(current, expected, f"initial score must be {expected}")

    def test_add_points_to_score(self) -> None:
        self.test_user.add_win()
        current = self.test_user.wins
        expected = 1
        self.assertEqual(current, expected, f"score must be {expected}")
