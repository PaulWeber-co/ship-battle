
import random
from enum import Enum


class Result(Enum):
    Draw = 1
    Win = 2
    Lose = 3

class RPSModel:

    def computer_choice(self):
        return random.randrange(1, 4)

    def __init__(self):
        self.lcount = 0
        self.wcount = 0


    def evaluate(self, n, x):
        match n:
            case 1:
                match x:
                    case 1:
                        return 1
                    case 2:
                        self.wcount += 1
                        return 2
                    case 3:
                        self.lcount += 1
                        return 3


            case 2:
                match x:
                    case 1:
                        self.lcount += 1
                        return 3
                    case 2:
                        return 1
                    case 3:
                        self.wcount += 1
                        return 2

            case 3:
                match x:
                    case 1:
                        self.wcount += 1
                        return 2
                    case 2:
                        self.lcount += 1
                        return 3
                    case 3:
                        return 1
        print("Wins:"+ wcount)
        print("Looses:"+ lcount)
        return "Wrong input"