'''
express_2019_03_01_cigarettes.py
Zach Bogart
03/02/2019

Code for testing out riddler express on buying cigarette packs

'''
from random import randint
from datetime import datetime

start = datetime.now()

def buy_cigarettes():
    cards_to_get = 144
    my_cards = [False] * cards_to_get
    cards_i_have = 0
    cards_drawn = 0

    while cards_i_have < cards_to_get:
        # get a random card
        new_card = randint(0, (cards_to_get - 1))
        cards_drawn += 1

        # I don't have this card yet in my collection
        if not my_cards[new_card]:
            my_cards[new_card] = True
            cards_i_have += 1

        # check if I have all of the cards
        if cards_i_have == cards_to_get:
            # print("I have all of the cards!")
            # print(f"It took me {cards_drawn} cards to get there.")
            return cards_drawn


number_of_trials = 20000
average_to_complete = 0

for trial in range(number_of_trials):

    card_number = buy_cigarettes()

    average_to_complete += card_number

average_to_complete /= number_of_trials

print(f"For {number_of_trials} trials, it took {average_to_complete} cards to get them all, on average.")


print(f"Time to execute: {datetime.now() - start}")








