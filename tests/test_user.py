import unittest
from cli.user import User


class TestUser(unittest.TestCase):
    def setUp(self) -> None:
        self.test_user = User(nickname="Johnny", score=0)

    def test_nickname_dont_match(self) -> None:
        current = self.test_user.nickname
        expected = "anything"
        self.assertRaises(ValueError)

    def test_nickname_match(self) -> None:
        current = self.test_user.nickname
        expected = "johnny"
        self.assertEqual(current, expected, "nicknames don't match")
