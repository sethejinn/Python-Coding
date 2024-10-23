import random

def roll_dice():
    return random.randint(1, 6)

def main():
    print("Welcome to the Dice Rolling Simulator!")
    
    while True:
        input("Press Enter to roll the dice.")
        
        try:
            result = roll_dice()
            print(f"You rolled: {result}")
            
            if random.random() < 0.1:
                raise ValueError("Oh! The die fell off the table and into the river...")
            
            while True:
                again = input("Roll again? (y/n): ").strip().lower()
                if again == 'y':
                    break
                elif again == 'n':
                    print("Goodbye!")
                    return
                else:
                    print("Invalid input. Please, enter 'y' or 'n'.")
        
        except ValueError as e:
            print(str(e))
            print("Unfortunately, you've lost your die in the river. Bye, bye!")
            return

if __name__ == "__main__":
    main()
