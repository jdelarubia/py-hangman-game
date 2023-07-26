import unittest
from cli.user import User


class TestUser(unittest.TestCase):
    def setUp(self) -> None:
        self.test_user = User(nickname="Johnny", score=0)

    def test_nickname_dont_match(self) -> None:
        current = self.test_user.nickname
        expected = "anything"
        with self.assertRaises(AssertionError):
            assert current == expected

    def test_nickname_match(self) -> None:
        current = self.test_user.nickname
        expected = "johnny"
        self.assertEqual(
            current, expected, f"nicknames don't match, {current} != {expected}"
        )

    def test_initial_score_is_zero(self) -> None:
        current = self.test_user.score
        expected = 0
        self.assertEqual(current, expected, f"initial score must be {expected}")

    def test_add_points_to_score(self) -> None:
        self.test_user.add_score(1)
        current = self.test_user.score
        expected = 1
        self.assertEqual(current, expected, f"score must be {expected}")
