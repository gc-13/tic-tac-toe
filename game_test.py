import unittest
import TicTacToe

class MyTestCase(unittest.TestCase):
    # def test_something(self):
    #     self.assertEqual(True, False)

    def twoplayer_setup(self):
        game1 = TicTacToe.Game()
        player1 = TicTacToe.Player('X', game1)
        player2 = TicTacToe.Player('O', game1)
        return (game1, player1, player2)

    def onecompplayer_setup(self):
        game1 = TicTacToe.Game()
        computer1 = TicTacToe.Computer('X', game1)
        player2 = TicTacToe.Player('O', game1)
        return (game1, computer1, player2)

    #Player 1 wins
    def test_mock_game1(self):
        game1, player1, player2 = self.twoplayer_setup()
        p1moves = ['top left', 'middle', 'bottom right']
        p2moves = ['top middle', 'bottom left', 'top right']
        winner = game1.play_test(player1, player2, p1moves, p2moves)
        self.assertEqual(player1, winner)

    #Player 2 wins
    def test_mock_game2(self):
        game1, player1, player2 = self.twoplayer_setup()
        p1moves = ['top right', 'middle', 'bottom right']
        p2moves = ['top left', 'middle left', 'bottom left']
        winner = game1.play_test(player1, player2, p1moves, p2moves)
        self.assertEqual(player2, winner)

    #Draw
    def test_mock_game3(self):
        game1, player1, player2 = self.twoplayer_setup()
        p1moves = ['top right', 'middle top', 'middle', 'bottom right', 'middle left']
        p2moves = ['top left', 'middle right', 'bottom left', 'bottom middle']
        winner = game1.play_test(player1, player2, p1moves, p2moves)
        self.assertEqual(None, winner)

    def test_place3(self):
        game1, computer1, player2 = self.onecompplayer_setup()
        game1.game_board = {1:"X", 2:"X",3:"-",
                           4:"-", 5:"-", 6:"-",
                           7:"-", 8:"-", 9:"-"}
        p2moves = ["middle", "bottom left"]
        winner = game1.play_comp_test(computer1, player2, p2moves)
        self.assertEqual(computer1, winner)
        self.assertEqual({1:"X", 2:"X",3:"X",
                           4:"-", 5:"-", 6:"-",
                           7:"-", 8:"-", 9:"-"},
                        game1.game_board
                         )

if __name__ == '__main__':
    unittest.main()
