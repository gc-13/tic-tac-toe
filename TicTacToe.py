
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
        """
        prints the board and any current played spaces
        """
        return self.game_board[1] + " | " + self.game_board[2] + " | " + self.game_board[3] + '\n' + \
               self.game_board[4] + " | " + self.game_board[5] + " | " + self.game_board[6] + '\n' + \
               self.game_board[7] + " | " + self.game_board[8] + " | " + self.game_board[9]

    def check_for_win(self):
        """
        Checks if there is 'three-in-a-row' of one sign on the board
        Firt checks horizontal rows, then vertical columns, and finally the two diagonals
        :return: True if 'three-in-a-row' of a sign is found, False otherwise
        """

        # Check Horizontal Rows
        for i in [1, 4, 7]:
            if(self.game_board[i] != '-' and
            self.game_board[i] == self.game_board[i+1] and self.game_board[i] == self.game_board[i+2]):
                return True

        # Check Vertical Columns
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
        """

        :param sign: Sign (X or O) to be placed
        :param pos: String Position of where to place the sign
        :return: True if pos was valid, the space was open, and the
         sign was succesfully placed, False otherwise
        """
        # if (self.game_board[pos] == '-' and self._validate_move(pos)):
        if self._validate_move(pos):
            if self.game_board[self.valid_moves[pos]] == '-':
                self.game_board[self.valid_moves[pos]] = sign
                print(self)
                print()
                return True
        return False

    def _validate_move(self, move):
        """
        Checks if the move is in the valid_moves dict and maps that to
        the appropriate space in the game board dictionary
        :param move: String move
        :return: True if the move is in the dict and the space is open
        """
        if ((move.lower() in self.valid_moves.keys()) and
            (self.game_board[self.valid_moves[move.lower()]] == '-')):
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

            if i == 4:
                return None

            player2.move(p2moves[i])
            if player1.game.check_for_win():
                print("Player 2 wins!")
                return player2

            i += 1




class Player():
    # The player of Tic Tac Toe

    def __init__(self, sign, game):
        self.sign = sign
        self.game = game

    def move(self, pos):
        return self.game.move(self.sign, pos)



