# Author: Paul Quaife
# Date: 3/4/2021
# Description: Class that represents the board for a two-player game that is played on a 4x4 grid


class FourLetterBoard:

    #constructor for the class
    def __init__(self):
        #intialzing private date members
        self._board = [[" " for i in range(4)] for j in range(4)]
        #this is to keep track of which player uses the cell
        self._ptrack = [[" " for i in range(4)] for j in range(4)]
        self._current_state = "UNFINISHED"
        self.fill = 0

    def get_current_state(self):
        """def returns current state of game"""
        return self._current_state

    def check(self, row, col, letter, player):
        """def checks if letter is same as other players"""

        if row < 2 and col < 2:
            region = 1
        elif row < 2 <= col:
            region = 2
        elif row >= 2 > col:
            region = 3
        elif row >= 2 and col >= 2:
            region = 4
        if region == 1:
            data = [self._board[0][0], self._board[0][1], self._board[1][0], self._board[1][1]]
            if letter in data:
                return False
        elif region == 2:
            data = [self._board[0][2], self._board[0][3], self._board[1][2], self._board[1][3]]
            if letter in data:
                return False
        elif region == 3:
            data = [self._board[2][0], self._board[2][1], self._board[3][0], self._board[3][1]]
            if letter in data:
                return False
        elif region == 1:
            data = [self._board[3][2], self._board[3][3], self._board[2][2], self._board[2][3]]
            if letter in data:
                return False

        for i in range(4):
            if self._ptrack[row][i] != player and self._board[row][i] == letter:
                return False
        for i in range(4):
            if self._ptrack[row][i] != player and self._board[row][i] == letter:
                return False

        return True

    def check_winner(self, row, col):
        """def checks winner"""
        if row < 2 and col < 2 :
            region = 1
        elif row < 2 <= col:
            region = 2
        elif row >= 2 > col:
            region = 3
        elif row >= 2 and col >= 2:
            region = 4

        if region == 1:
            data = [self._board[0][0], self._board[0][1], self._board[1][0], self._board[1][1]]
            if sorted(data) == ['A', 'B', 'C', 'D']:
                return True
        elif region == 2:
            data = [self._board[0][2], self._board[0][3], self._board[1][2], self._board[1][3]]
            if sorted(data) == ['A', 'B', 'C', 'D']:
                return True
        elif region == 3:
            data = [self._board[2][0], self._board[2][1], self._board[3][0], self._board[3][1]]
            if sorted(data) == ['A', 'B', 'C', 'D']:
                return True
        elif region == 1:
            data = [self._board[3][2], self._board[3][3], self._board[2][2], self._board[2][3]]
            if sorted(data) == ['A','B','C','D']:
                return True

        for i in range(4):
            data = [self._board[row][0], self._board[row][1], self._board[row][2], self._board[row][3]]
            if sorted(data) == ['A', 'B', 'C', 'D']:
                return True
        #check the data for the column if the player wins
        for i in range(4):
            data = [self._board[0][col], self._board[1][col], self._board[2][col], self._board[3][col]]
            if sorted(data) == ['A', 'B', 'C', 'D']:
                return True

        return False

    #method to print the board
    def print_board(self):
        """def prints board"""
        for i in range(4):
            print(self._board[i])
        print()

    #method for make_move
    def make_move(self,row,col,letter,player):
        """def makes move on board."""
        if self.fill != 16 and self._board[row][col] == " " and self._current_state == "UNFINISHED" and self.check(row, col, letter, player):
            self._board[row][col] = letter
            self._ptrack[row][col] = player
            self.fill += 1
            if self.check_winner(row, col):
                if player == 'x':
                    self._current_state = "X_WON"
                elif player == "o":
                    self._current_state = "O_WON"

            self.print_board()

            return True
        else:
            return False


board = FourLetterBoard()
board.make_move(0, 0, 'B', 'o')  # The o player places a B in one of the corners
board.make_move(3, 3, 'D', 'o')  # The o player places a D in the opposite corner
print(board.get_current_state())
