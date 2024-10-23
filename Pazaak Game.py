class PazaakGame:
    def __init__(self):
        self.main_deck = list(range(1, 11)) * 4
        self.player_hand = []
        self.computer_hand = []
        self.player_stand = False
        self.computer_stand = False

    def draw_card(self):
        if not self.main_deck:
            self.main_deck = list(range(1, 11)) * 4
        index = self.get_random_index(len(self.main_deck))
        card = self.main_deck.pop(index)
        return card

    def get_random_index(self, length):
        # Generates a pseudo-random number using a seed.
        # A basic implementation of LCG (Linear Congruential Generator)
        self.seed = (self.seed * 1103515245 + 12345) % 2**31
        return self.seed % length

    def play(self):
        self.seed = 1  # Initial seed for pseudo-random number generation
        while not self.player_stand or not self.computer_stand:
            if not self.player_stand:
                print(f"Your hand: {self.player_hand}, Total: {sum(self.player_hand)}")
                choice = input("Do you want another card? (y/n): ")
                if choice.lower() == 'y':
                    self.player_hand.append(self.draw_card())
                else:
                    self.player_stand = True

                if sum(self.player_hand) > 20:
                    print("You went over 20! You lost.")
                    return

            if not self.computer_stand:
                if sum(self.computer_hand) < 17:
                    self.computer_hand.append(self.draw_card())
                else:
                    self.computer_stand = True

                if sum(self.computer_hand) > 20:
                    print("The computer went over 20! You won.")
                    return

        player_total = sum(self.player_hand)
        computer_total = sum(self.computer_hand)

        print(f"Your total: {player_total}")
        print(f"Computer's total: {computer_total}")

        if player_total > computer_total:
            print("You won!")
        elif player_total < computer_total:
            print("You lost.")
        else:
            print("It's a tie.")

def main():
    while True:
        game = PazaakGame()
        game.play()
        replay = input("Do you want to play another game? (y/n): ")
        if replay.lower() != 'y':
            print("Thanks for playing. See you next time!")
            break

if __name__ == "__main__":
    main()
