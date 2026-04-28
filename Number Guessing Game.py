#Number Guessing Game
import random

class NumberGuessingGame:
    def __init__(self):
        self.number = 0
        self.attempts = 0
        self.max_attempts = None
        self.difficulty = ""
        self.game_over = False
        
        
