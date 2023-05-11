import random


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit


card_values = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
card_suits = ["Hearts", "Diamonds", "Clubs", "Spades"]

# Player Stats
player_cards = []

# Dealer Stats
dealers_cards = []


drawn_cards = []

emojis = {
    "Diamonds": "♦️",
    "Hearts": "❤️",
    "Clubs": "♣️",
    "Spades": "♠️",
    "Ace": "A",
    "Two": "2",
    "Three": "3",
    "Four": "4",
    "Five": "5",
    "Six": "6",
    "Seven": "7",
    "Eight": "8",
    "Nine": "9",
    "Ten": "10",
    "Jack": "J",
    "Queen": "Q",
    "King": "K"
    }

face_converter = {
    "Two": "2",
    "Three": "3",
    "Four": "4",
    "Five": "5",
    "Six": "6",
    "Seven": "7",
    "Eight": "8",
    "Nine": "9",
    "Ten": "10",
    "Jack": "10",
    "Queen": "10",
    "King": "10",
    "Ace": "11"
}


def draw_player_card():
    # Generates random value and suit
    given_card_value = random.randint(0, len(card_values) - 1)
    given_card_suit = random.randint(0, len(card_suits) - 1)

    # Makes a card with that value and suit
    card = Card(card_values[given_card_value], card_suits[given_card_suit])

    # Checks if card already exists, if so, draws a new one
    if f"{card.value} of {card.suit}" in drawn_cards:
        draw_player_card()
        return

    # Adds drawn card to drawn list
    drawn_cards.append(f"{card.value} of {card.suit}")

    # Adds drawn card to players hand
    player_cards.append(f"{card.value} of {card.suit}")
    print(f"You drew {emojis.get(card_values[given_card_value])}{emojis.get(card_suits[given_card_suit])}")


def draw_dealer_card():
    # Generates random value and suit
    given_card_value = random.randint(0, len(card_values) - 1)
    given_card_suit = random.randint(0, len(card_suits) - 1)

    # Makes a card with that value and suit
    card = Card(card_values[given_card_value], card_suits[given_card_suit])

    # Checks if card has already been drawn
    if f"{card.value} of {card.suit}" in drawn_cards:
        draw_dealer_card()
        return

    # Adds drawn car to dealers hand
    drawn_cards.append(f"{card.value} of {card.suit}")
    dealers_cards.append(f"{card.value} of {card.suit}")
