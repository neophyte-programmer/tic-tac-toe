import time
from player import HumanPlayer, RandomComputerPlayer


class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]    # single list representing 3x3 board
        self.currentWinner = None   # keep track of winner

    def printBoard(self):
        # defining rows
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print("| " + " | ".join(row) + " |")

    @staticmethod
    def printBoardNums():
        # shows which numbers correspond to which box on the board
        numberBoard = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in numberBoard:
            print("| " + " | ".join(row) + " |")

    def availableMoves(self):
        return [i for i, spot in enumerate(self.board) if spot == " "]
        # moves = []
        # for (i, spot) in enumerate(self.board):
        #     if spot == " ":
        #         moves.append(i)
        # return moves

    def emptySquares(self):
        return " " in self.board

    def numEmptySquares(self):
        return len(self.availableMoves())

    def makeMove(self, square, letter):
        if self.board[square] == " ":
            self.board[square] = letter
            if self.winner(square, letter):
                self.currentWinner = letter
            return True

        return False

    def winner(self, square, letter):
        # check if there is a win in row
        rowIndex = square // 3
        row = self.board[rowIndex*3: (rowIndex + 1) * 3]    # which row are we checking, 1st 2nd or 3rd
        if all([spot == letter for spot in row]):
            return True

        # check if there is a win in column
        colIndex = square % 3
        column = [self.board[colIndex+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        # check if there is a win in diagonal
        # for this to be possible, the square has to be an even number because we are counting from 0
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True

        return False


def play(game, xPlayer, oPlayer, printGame=True):
    if printGame:
        game.printBoardNums()

    letter = "X"    # starting letter
    while game.emptySquares():
        # get move from player
        if letter == "O":
            square = oPlayer.getMove(game)
        else:
            square = xPlayer.getMove(game)

        if game.makeMove(square, letter):
            if printGame:
                print(letter + f" makes a move to square {square}")
                game.printBoard()
                print("")

            if game.currentWinner:
                if printGame:
                    print(f"{letter} wins!")
                return letter

            letter = "O" if letter == "X" else "X"

        time.sleep(0.8)

    if printGame:
        print("It's a tie")


if __name__ == "__main__":
    xPlayer = HumanPlayer("X")
    oPlayer = RandomComputerPlayer("O")
    t = TicTacToe()
    play(t, xPlayer, oPlayer, printGame=True)

