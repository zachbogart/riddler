import random
import numpy as np

'''
Riddler Classic

Three Deck Monte
Posted 02/01/2019

https://fivethirtyeight.com/features/can-you-escape-a-maze-without-walls/

Result:
- You should not take the bet. Every deck has equal odds in the long run
and you end up with ~70% chance of losing (assuming the man takes the best
counter deck every time).
'''

'''
J 11
Q 12
K 13
A 14
'''

# define the decks
red_deck = np.array([14, 14, 14, 14,
             9, 9, 9, 9,
             7, 7, 7, 7])

blue_deck = np.array([13, 13, 13, 13,
             11, 11, 11, 11,
             6, 6, 6, 6])

black_deck = np.array([12, 12, 12, 12,
              10, 10, 10, 10,
              8, 8, 8, 8])

num_cards = 5

def play_war(user_deck, cpu_deck):

    # winning condition
    user_score = 0
    cpu_score = 0

    def someone_won(user_score, cpu_score):
        return (user_score == num_cards or cpu_score == num_cards)

    # shuffle cards
    random.shuffle(user_deck)
    random.shuffle(cpu_deck)

    # print(user_deck)
    # print(cpu_deck)

    # loop thru decks
    for card in range(12):
        # if user is higher add to user score
        if user_deck[card] > cpu_deck[card]:
            user_score += 1
        # otherwise cpu won, add to cpu score
        else:
            cpu_score += 1

        # break out if someone has won
        if someone_won(user_score, cpu_score):
            break

    # print("Final score is: {}, {}".format(user_score, cpu_score))

    if user_score == num_cards:
        return 1

    else:
        return 2

# array of decks
decks = np.array([red_deck, blue_deck, black_deck])

# user win counts
user_wins_using_red = 0
user_wins_using_blue = 0
user_wins_using_black = 0

# total games by type
total_using_red = 0
total_using_blue = 0
total_using_black = 0

def update_results(result, user_choice):

    user_wins_using_red = 0
    user_wins_using_blue = 0
    user_wins_using_black = 0

    total_using_red = 0
    total_using_blue = 0
    total_using_black = 0

    if result == 1:
        if user_choice == 0:
            user_wins_using_red += 1
            total_using_red += 1
        if user_choice == 1:
            user_wins_using_blue += 1
            total_using_blue += 1
        if user_choice == 2:
            user_wins_using_black += 1
            total_using_black += 1
    else:
        if user_choice == 0:
            total_using_red += 1
        if user_choice == 1:
            total_using_blue += 1
        if user_choice == 2:
            total_using_black += 1

    return [user_wins_using_red, user_wins_using_blue, user_wins_using_black,
            total_using_red, total_using_blue, total_using_black]

games = 100000

for game in range(games):

    deck_assignments = np.random.choice([0, 1, 2], size = 2, replace = False)

    user_choice = deck_assignments[0]
    # cpu_choice = deck_assignments[1]

    if user_choice == 0:
        cpu_choice = 2
    if user_choice == 1:
        cpu_choice = 0
    if user_choice == 2:
        cpu_choice = 1

    user_deck = decks[user_choice].copy()
    cpu_deck = decks[cpu_choice].copy()

    result = play_war(user_deck, cpu_deck)

    new_additions = update_results(result, user_choice)

    user_wins_using_red += new_additions[0]
    user_wins_using_blue += new_additions[1]
    user_wins_using_black += new_additions[2]
    total_using_red += new_additions[3]
    total_using_blue += new_additions[4]
    total_using_black += new_additions[5]

print("Games played: ", games)

print("Fraction won using Red:   ", user_wins_using_red / total_using_red)
print("Fraction won using Blue:  ", user_wins_using_blue / total_using_blue)
print("Fraction won using Black: ", user_wins_using_black / total_using_black)










