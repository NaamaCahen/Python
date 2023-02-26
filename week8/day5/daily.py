import random


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value


class Deck:
    def __init__(self, cards):
        self.cards = cards
        self.suits = ['Heart', 'Diamond', 'Club', 'Spade']
        self.values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    def shuffle(self):
        # check if it's a complete deck
        for suit in self.suits:
            for value in self.values:
                if not any(card.suit == suit and card.value == value for card in self.cards):
                    return f"not a complete deck"
        # shuffle the cards
        random.shuffle(self.cards)

    def deal(self):
        dealt_card = random.choice(self.cards)
        self.cards.remove(dealt_card)
        return dealt_card


card1 = Card('Heart', 'A')
card2 = Card('Diamond', 'Q')
card3 = Card('Club', '2')
cards = [card3, card1, card2]
deck = Deck(cards)
print(deck.shuffle())
print(deck.deal().suit)
