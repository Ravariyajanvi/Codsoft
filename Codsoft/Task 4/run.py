import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class RockPaperScissors:
    def __init__(self):
        self.choices = ['rock', 'paper', 'scissors']
        self.user_score = 0
        self.computer_score = 0
        
    def get_computer_choice(self):
        return random.choice(self.choices)
    
    def get_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "tie"
        
        winning_combinations = {
            'rock': 'scissors',
            'paper': 'rock',
            'scissors': 'paper'
        }
        
        if winning_combinations[user_choice] == computer_choice:
            return "user"
        return "computer"
    
    def display_scores(self):
        print("\n=== Current Scores ===")
        print(f"You: {self.user_score}")
        print(f"Computer: {self.computer_score}")
        print("=" * 20)
    
    def play_game(self):
        while True:
            clear_screen()
            print("\n=== Rock Paper Scissors Game ===")
            self.display_scores()
            
            print("\nChoose your move:")
            print("1. Rock 🪨")
            print("2. Paper 📄")
            print("3. Scissors ✂️")
            print("4. Exit Game")
            
            choice = input("\nEnter your choice (1-4): ")
            
            if choice == '4':
                print("\nThanks for playing!")
                break
                
            if choice not in ['1', '2', '3']:
                print("\nInvalid choice! Please try again.")
                input("Press Enter to continue...")
                continue
            
            user_choice = self.choices[int(choice) - 1]
            computer_choice = self.get_computer_choice()
            
            print(f"\nYour choice: {user_choice}")
            print(f"Computer's choice: {computer_choice}")
            
            winner = self.get_winner(user_choice, computer_choice)
            
            if winner == "tie":
                print("\nIt's a tie!")
            elif winner == "user":
                print("\nYou win! 🎉")
                self.user_score += 1
            else:
                print("\nComputer wins! 💻")
                self.computer_score += 1
            
            input("\nPress Enter to continue...")

def main():
    game = RockPaperScissors()
    game.play_game()

if __name__ == "__main__":
    main()