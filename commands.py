import carddraw
from carddraw import *

command_list = ["help", "hit", "stay", "show hand", "show dealers hand", "instructions", "my total", "dealers total"]
command_list.sort()


def hit():
    draw_player_card("new card")
    player_total()


def show_hand():
    print(carddraw.player_cards)


def show_dealer_hand():
    print(carddraw.dealers_cards[~1])


def instructions():
    print('''
Object of the game:
Each participant attempts to beat the dealer by getting a count as close to 21 as possible, without going over 21.

Card Values:
It is up to each individual player if an ace is worth 1 or 11. Face cards are 10 and any other card is its pip value.

Betting:
Before the deal begins, each player places a bet

The Deal:
Every player gets two cards face up. The house gets two cards, however, players can only see one of them.
If a player receives an Ace and a 10 value card, they get Blackjack and win 3:2 odds.

The Play:
The player goes first and must decide whether to "stand" (not ask for another card) or 
"hit" (ask for another card in an attempt to get closer to a count of 21, or even hit 21 exactly).
Thus, a player may stand on the two cards originally dealt to them, or they may ask the dealer for additional cards,
one at a time, until deciding to stand on the total (if it is 21 or under), or goes "bust" (if it is over 21). 
In the latter case, the player loses and the dealer collects the bet wagered.

The Dealers Play:
If the total is 17 or more, it must stand. If the total is 16 or under, they must take a card. 
The dealer must continue to take cards until the total is 17 or more, at which point the dealer must stand. 
If the dealer has an ace, and counting it as 11 would bring the total to 17 or more (but not over 21), 
the dealer must count the ace as 11 and stand. The dealer's decisions, then, are automatic on all plays, 
whereas the player always has the option of taking one or more cards.


''')


def player_total():
    p_total = 0
    for card in carddraw.player_cards:
        number = card.split()
        p_total += int(face_converter.get(number[0]))

        # Ace
        if p_total > 21 and face_converter.get(number[0]) == "11":
            p_total -= 10

    return p_total


def print_dealer_total(d_total=None):
    excluded_index = 1
    indexed_list = carddraw.dealers_cards[:excluded_index] + carddraw.dealers_cards[excluded_index+1:]
    for card in indexed_list:
        split = card.split()
        d_total += int(face_converter.get(split[0]))
        if d_total > 21 and face_converter.get(split[0]) == "11":
            d_total -= 10
    return d_total


def real_dealer_total(d_total=None):
    for card in carddraw.dealers_cards:
        split = card.split()
        d_total += int(face_converter.get(split[0]))
        if d_total > 21 and face_converter.get(split[0]) == "11":
            d_total -= 10
    return d_total
