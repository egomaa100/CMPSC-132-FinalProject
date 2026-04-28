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

            choice = input("Enter choice (1-3): ".strip())

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

    def get_valid_guess(self):
        valid_input = False
        result = None
        while not valid_input:
            guess = input("Enter your guess: ").strip()

            if guess.lower() == "quit":
                result = None
                valid_input = True
            else:
                try:
                    guess_int = int(guess)
                    if guess_int > 0:
                        result = guess_int
                        valid_input = True
                    else:
                        print("Please enter a positive number")
                except ValueError:
                    print("Invalid input. Please enter a valid number")

        return result

    def play(self):
        self.attempts = 0
        self.game_over = False
        print(f"\nGame Started! Difficulty: {self.difficulty}")
        print("Type 'quit' anytime to exit the game\n")
        
        while not self.game_over:
            guess = self.get_valid_guess()
            
            if guess is None:
                print("You exited the game")
                self.game_over = True
            else:
                self.attempts += 1

            if self.max_attempts is not None and self.attempts == self.max_attempts:
                print(f"\nOut of attempts! The number was {self.number}")
                self.game_over = True
            else:
                if guess > self.number:
                    print("Too high! Try a lower number")
                elif guess < self.number:
                    print("Too low! Try a higher number")
                else:
                    print(f"\nCongratulations! You guessed the number in {self.attempts} attempts!")
                    self.game_over = True

                if not self.game_over and self.max_attempts is not None:
                    remaining = self.max_attempts - self.attempts
                    print(f"{remaining} attempts left")

    def replay(self):
        valid_choice = False
        play_again = False
        
        while not valid_choice:
            choice = input("\nPlay again? (y/n): ").strip().lower()
            
            if choice == "y":
                play_again = True
                valid_choice = True
            elif choice == "n":
                play_again = False
                valid_choice = True
                print("Thanks for playing!")
            else:
                print("Invalid input. Please enter 'y' or 'n'")
                
        return play_again
                    
def main():
    print("Number Guessing Game")
    game = NumberGuessingGame()
    playing = True
    while playing:
        game.choose_difficulty()
        game.play()
        playing = game.replay()

if __name__ == "__main__":
    main()
