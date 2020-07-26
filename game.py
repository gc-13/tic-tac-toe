
class Game():
    #Used for a Tic Tac Toe game

    def __init__(self):
        #Each board is 3x3
        self.game_board = {1:"-", 2:"-",3:"-",
                           4:"-", 5:"-", 6:"-",
                           7:"-", 8:"-", 9:"-"}

    def __str__(self):
        return self.game_board[1] + " | " + self.game_board[2] + " | " + self.game_board[3] + '\n' + \
               self.game_board[4] + " | " + self.game_board[5] + " | " + self.game_board[6] + '\n' + \
               self.game_board[7] + " | " + self.game_board[8] + " | " + self.game_board[9]

    def check_for_win(self):

        # Check Horizontal Rows
        for i in [1, 4, 7]:
            if(self.game_board[i] != '-' and
            self.game_board[i] == self.game_board[i+1] and self.game_board[i] == self.game_board[i+2]):
                return True

        # Check Vertical Row
        for i in [1,2,3]:
            if(self.game_board[i] != '-' and
            self.game_board[i] == self.game_board[i+3] and self.game_board[i] == self.game_board[i+6]):
                return True

        # Check Diagonals
        if((self.game_board[1] != '-' and
        self.game_board[1] == self.game_board[5] and self.game_board[1] == self.game_board[9]) or(
        self.game_board[3] != '-' and
        self.game_board[3] == self.game_board[5] and self.game_board[3] == self.game_board[7])):
                return True

        #No matches
        return False

    def place(self, sign, pos):
        if (self.game_board[pos] == '-'):
            self.game_board[pos] = sign
            print(self)
            return True
        return False


class Player():
    # The player of Tic Tac Toe

    def __init__(self, sign, game):
        self.sign = sign
        self.game = game

    def move(self, pos):
        return self.game.place(self.sign, pos)



# 9 Functions to win the game!


game = Game()
print(game)
player1 = Player('X', game)
player2 = Player('O', game)


game_over = False
print("Let's play tic-tac-toe! I'm Os, you're Xs!")

while not game.check_for_win():
    player1.move(int(input("Player 1 turn:")))
    player2.move(int(input("Player 2 turn:")))

