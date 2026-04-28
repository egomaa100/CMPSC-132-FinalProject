#Number Guessing Game
import random

class NumberGuessingGame:
    def __init__(self):
        self.number = 0
        self.attempts = 0
        self.max_attempts = None
        self.difficulty = ""
        self.game_over = False
    
    def choose_difficulty(self):
        valid_choice = False
        while not valid_choice:
            print("\nChoose Difficulty:")
            print("1. Easy (1-50, Unlimited attempts)")
            print("2. Medium (1-100, 10 attempts)")
            print("3. Hard (1-200, 5 attempts)")

            choice = input("Enter choice (1-3): ".strip()

            if choice == "1":
                self.number = random.randint(1,50)
                self.max_attempts = None
                self.difficulty = "Easy"
                valid_choice = True
            elif choice == "2":
                self.number = random.randint(1,100)
                self.max_attempts = 10
                self.difficulty = "Medium"
                valid_choice = True
            elif choice == "3":
                self.number = random.randint(1,200)
                self.max_attempts = 5
                self.difficulty = "Hard"
                valid_choice = True
            else:
                print("Invalid choice. Please select 1, 2, or 3.")
        
