
class Game():
    #Used for a Tic Tac Toe game

    def __init__(self):
        #Each board is 3x3
        self.game_board = {1:"-", 2:"-",3:"-",
                           4:"-", 5:"-", 6:"-",
                           7:"-", 8:"-", 9:"-"}
        self.valid_moves = {
                            "top left": 1, "top left corner" : 1, "1":1,
                            "top middle": 2, "middle top": 2, "2": 2,
                            "top right": 3, "top right corner": 3, "3": 3,
                            "left middle": 4, "middle left": 4, "4": 4,
                            "middle": 5, "mid": 5, "middle middle": 5,"5": 5,
                            "right middle": 6, "middle right": 6, "6": 6,
                            "bottom left": 7, "bottom left corner": 7, "7": 7,
                            "bottom middle": 8, "middle bottom": 8, "8": 8,
                            "bottom right": 9, "bottom right corner": 9, "9": 9,
                            '' : None,
        }

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

    def move(self, sign, pos):
        # if (self.game_board[pos] == '-' and self._validate_move(pos)):
        if self._validate_move(pos):
            if self.game_board[self.valid_moves[pos]] == '-':
                self.game_board[self.valid_moves[pos]] = sign
                print(self)
                print()
                return True
        return False

    def _validate_move(self, move):
        if(move.lower() in self.valid_moves.keys()):
            if(self.game_board[self.valid_moves[move.lower()]] == '-'):
                # self.move(sign, self.valid_moves[move.lower()])
                return True
        return False

    def play(self, player1, player2):
        print("Let's play tic-tac-toe! I'm Os, you're Xs!")
        while not self.check_for_win():
            p1move = ""
            while (p1move == "" or (not player1.game.move(player1.sign, p1move))):
                p1move = input("Player 1 turn: ")
            player1.move(p1move)
            if player1.game.check_for_win():
                print("Player 1 wins!")
                return player1
            p2move = ""
            while (p2move == "" or (not player2.game.move(player2.sign, p2move))):
                p2move = input("Player 2 turn: ")
            player2.move(p2move)
            if player1.game.check_for_win():
                print("Player 2 wins!")
                return player2

    def play_test(self, player1, player2, p1moves, p2moves):
        print("Let's play tic-tac-toe! I'm Os, you're Xs!")
        i = 0
        while not self.check_for_win():
            player1.move(p1moves[i])
            if player1.game.check_for_win():
                print("Player 1 wins!")
                return player1

            player2.move(p2moves[i])
            if player1.game.check_for_win():
                print("Player 2 wins!")
                return player2

            i+=1



class Player():
    # The player of Tic Tac Toe

    def __init__(self, sign, game):
        self.sign = sign
        self.game = game

    def move(self, pos):
        return self.game.move(self.sign, pos)



# 9 Functions to win the game!


# game = Game()
# player1 = Player('X', game)
# player2 = Player('O', game)

# game.play(player1, player2)




