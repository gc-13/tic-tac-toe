
class Game():
    #Used for a Tic Tac Toe game

    def __init__(self):
        #Each board is 3x3
        self.game_board = {"1":"-", "2":"-","3":"-",
                           "4":"-", "5":"-", "6":"-",
                           "7":"-", "8":"-", "9":"-"}

    def __str__(self):
        return self.game_board["1"] + " | " + self.game_board["2"] + " | " + self.game_board["3"] + '\n' + \
               self.game_board["4"] + " | " + self.game_board["5"] + " | " + self.game_board["6"] + '\n' + \
               self.game_board["7"] + " | " + self.game_board["8"] + " | " + self.game_board["9"]


class Player():
    # The player of Tic Tac Toe

    def __init__(self, sign):
        self.sign = sign


# 9 Functions to win the game!


game = Game()
print(game)


game_over = False
print("Let's play tic-tac-toe! I'm Os, you're Xs!")
