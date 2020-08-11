import unittest
import game

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

    def setup(self):
        gameA = game.Game()
        print(game)
        player1 = game.Player('X', game)
        player2 = game.Player('O', game)
        return (gameA, player1, player2)

    def mock_game1(self):
        p1moves = ['top left', 'middle', 'bottom right']
        p2moves = ['top middle', 'bottom left', 'top right']


if __name__ == '__main__':
    unittest.main()
