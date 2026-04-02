import random

class Card:
    def __init__(self, rank, suit):
        self.__rank = rank
        self.__suit = suit
        self.__face_up = False

    def flip(self):
        self.__face_up = not self.__face_up

    def get_value(self):
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
        return ranks.index(self.__rank)

    def __str__(self):
        return f"{self.__rank}{self.__suit}" if self.__face_up else "?? "

class Hand:
    def __init__(self):
        self.__cards = []

    def add_card(self, card):
        if len(self.__cards) < 2:
            self.__cards.append(card)

    def get_total_point(self):
        # Luat don gian: Tong diem cua 2 la bai
        return sum(c.get_value() for c in self.__cards)

    def clear(self):
        self.__cards = []

    def __str__(self):
        return " ".join(str(c) for c in self.__cards)

class Player:
    def __init__(self, name, chips):
        self.__name = name
        self.__chips = chips
        self.__bet = 0
        self.__hand = Hand()
        self.__is_in = True

    def bet_chips(self, amount):
        if amount <= self.__chips:
            self.__chips -= amount
            self.__bet += amount
            return True
        return False

    def fold(self):
        self.__is_in = False

    def reset_round(self):
        self.__bet = 0
        self.__is_in = True
        self.__hand.clear()

    def get_name(self): return self.__name
    def get_hand(self): return self.__hand
    def get_chips(self): return self.__chips
    def is_playing(self): return self.__is_in

class ComputerPlayer(Player):
    def __init__(self, name, chips, difficulty=1):
        super().__init__(name, chips)
        self.__level = difficulty

    def auto_move(self):
        # AI ngau nhien cho giong nguoi choi that
        action = random.choice(["call", "fold", "raise"])
        return action

class Deck:
    def __init__(self):
        self.__cards = []
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
        suits = ['♠', '♣', '♦', '♥']
        for s in suits:
            for r in ranks:
                self.__cards.append(Card(r, s))

    def shuffle_deck(self):
        random.shuffle(self.__cards)

    def draw(self):
        return self.__cards.pop() if self.__cards else None

class PokerGame:
    def __init__(self):
        self.__players = []
        self.__deck = Deck()
        self.__pot = 0

    def add_player(self, player):
        self.__players.append(player)

    def start_game(self):
        print("--- BAT DAU VAN POKER ---")
        self.__deck.shuffle_deck()
        
        for p in self.__players:
            p.reset_round()
            p.get_hand().add_card(self.__deck.draw())
            p.get_hand().add_card(self.__deck.draw())
            for card in p.get_hand()._Hand__cards:
                card.flip()

        for p in self.__players:
            print(f"Player {p.get_name()}: {p.get_hand()} | Chips: {p.get_chips()}")

        winner = max(self.__players, key=lambda x: x.get_hand().get_total_point())
        print(f"\nWINNER: {winner.get_name()} voi tay bai: {winner.get_hand()}")

if __name__ == "__main__":
    game = PokerGame()
    game.add_player(Player("Hieu", 5000))
    game.add_player(ComputerPlayer("Bot_1", 3000))
    game.add_player(ComputerPlayer("Bot_2", 4000))
    
    game.start_game()