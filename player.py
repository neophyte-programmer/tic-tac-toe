import math
import random

class Player:
    def __init__(self, letter):
        self.letter = letter

    def getMove(self, game):
        pass


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def getMove(self, game):
        square = random.choice(game.availableMoves())
        return square


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def getMove(self, game):
        validSquare = False
        val = None
        while not validSquare:
            square = input(self.letter + "'s turn. Input move 0-8: ")
            # validation
            try:
                val = int(square)
                if val not in game.availableMoves():
                    raise ValueError
                validSquare = True
            except ValueError:
                print("Invalid square! Try again.")

        return val

