import unittest
import TicTacToe

class MyTestCase(unittest.TestCase):
    # def test_something(self):
    #     self.assertEqual(True, False)

    def setup(self):
        game1 = TicTacToe.Game()
        player1 = TicTacToe.Player('X', game1)
        player2 = TicTacToe.Player('O', game1)
        return (game1, player1, player2)

    def test_mock_game1(self):
        p1moves = ['top left', 'middle', 'bottom right']
        p2moves = ['top middle', 'bottom left', 'top right']
        game1, player1, player2 = self.setup()
        winner = game1.play_test(player1, player2, p1moves, p2moves)
        self.assertEqual(player1, winner)

if __name__ == '__main__':
    unittest.main()
