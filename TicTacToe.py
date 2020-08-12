
class Game():
    #Used for a Tic Tac Toe game

    def __init__(self):
        #Each board is 3x3
        self.game_board = {1:"-", 2:"-",3:"-",
                           4:"-", 5:"-", 6:"-",
                           7:"-", 8:"-", 9:"-"}
        self.valid_moves = {
                            "top left": 1, "top left corner" : 1, "1":1, 1:1,
                            "top middle": 2, "middle top": 2, "2": 2, 2:2,
                            "top right": 3, "top right corner": 3, "3": 3, 3:3,
                            "left middle": 4, "middle left": 4, "4": 4, 4:4,
                            "middle": 5, "mid": 5, "middle middle": 5,"5": 5, 5:5,
                            "right middle": 6, "middle right": 6, "6": 6, 6:6,
                            "bottom left": 7, "bottom left corner": 7, "7": 7, 7:7,
                            "bottom middle": 8, "middle bottom": 8, "8": 8, 8:8,
                            "bottom right": 9, "bottom right corner": 9, "9": 9, 9:9,
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
                return True
        return False

    def _validate_move(self, move):
        """
        Checks if the move is in the valid_moves dict and maps that to
        the appropriate space in the game board dictionary
        :param move: String move
        :return: True if the move is in the dict and the space is open
        """
        #temporarily taking out move.lower()
        if ((move in self.valid_moves.keys()) and
            (self.game_board[self.valid_moves[move]] == '-')):
            return True
        return False

    def play(self, player1, player2):
        print("Let's play tic-tac-toe! I'm Os, you're Xs!")
        while not self.check_for_win():
            p1move = ""
            while (p1move == "" or (not player1.game.move(player1.sign, p1move))):
                p1move = input("Player 1 turn: ")
            player1.move(p1move)
            if self.check_for_win():
                print("Player 1 wins!")
                return player1

            p2move = ""
            while (p2move == "" or (not player2.game.move(player2.sign, p2move))):
                p2move = input("Player 2 turn: ")
            player2.move(p2move)
            if self.check_for_win():
                print("Player 2 wins!")
                return player2

    def play_test(self, player1, player2, p1moves, p2moves):
        print("Let's play tic-tac-toe! I'm Os, you're Xs!")
        i = 0
        while not self.check_for_win():
            player1.move(p1moves[i])
            if self.check_for_win():
                print("Player 1 wins!")
                return player1

            if i == 4:
                return None

            player2.move(p2moves[i])
            if self.check_for_win():
                print("Player 2 wins!")
                return player2

            i += 1

    def play_comp_test(self, comp1, player2, p2moves):
        print("Let's play tic-tac-toe! I'm Os, you're Xs!")
        i = 0
        while not self.check_for_win():
            comp1.auto_move()

            if self.check_for_win():
                print("Player 1 wins!")
                return comp1

            if i == 4:
                return None

            player2.move(p2moves[i])
            if self.check_for_win():
                print("Player 2 wins!")
                return player2

            i += 1






class Player():
    # The player of Tic Tac Toe

    def __init__(self, sign, game):
        self.sign = sign
        self.game = game

    def taken(self, sign, index):
        if self.game.game_board[index] == sign:
            return True
        return False

    def playable(self, index):
        if self.game.game_board[index] == '-':
            return True
        return False

    def move(self, pos):
        return self.game.move(self.sign, pos)


class Computer(Player):

    def auto_move(self):
        print("beginning auto move")
        moved = False
        moves = [self.first_win, self.second_block, self.fifth_center,]
        for i in range(len(moves)):
            moved = moves[i]()
            if moved:
                break

    def _get_three(self, indices):
        """
        Finds the playable space in 'indicies'. Always called after
        _oneplay_twotaken
        :param indices: 3 indicies in the game_board, representing a row,
                        column, or diagonal
        :return: The index that is playable
        """
        for i in indices:
            if self.playable(i):
                return i

    def _oneplay_twotaken(self, sign, indices):
        """
        Checks if it is possible to get 'three-in-a-row' in this group
        :param indices: 3 indicies in the game_board, representing a row,
                        column, or diagonal
        :return: True if there are two spaces taken by the sign and
                one that is open, False otherwise
        """
        playble = 0
        taken = 0
        for i in indices:
            if self.playable(i):
                playble +=1
            if self.taken(sign, i):
                taken +=1
        return (playble, taken) == (1,2)

    def first_win(self):

        for combo in [  [1,2,3], [4,5,6], [7,8,9],
                        [1,4,7], [2,5,8], [3,6,9],
                        [1,5,9], [3,5,7]]:
            if self._oneplay_twotaken(self.sign, combo):
                self.move(self._get_three(combo))
                return True

        return False

    def second_block(self):
        sign = ''
        if self.sign == 'X':
            sign = 'O'
        else:
            sign = 'X'
        for combo in [  [1,2,3], [4,5,6], [7,8,9],
                        [1,4,7], [2,5,8], [3,6,9],
                        [1,5,9], [3,5,7]]:
            if self._oneplay_twotaken(sign, combo):
                print(self._get_three(combo))
                self.move(self._get_three(combo))
                print(self.game.check_for_win())
                print(self.game)
                return True

        return False

    def fifth_center(self):

        if self.playable(5):
            self.move(5)
            return True
        return False



