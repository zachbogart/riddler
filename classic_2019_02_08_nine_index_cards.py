'''
Riddler Classic
Posted Feb 8 2019
Zach Bogart

--------

Instructions

You and I are playing a game. It’s a simple one: Spread out on a table in front of us, face up, are nine index cards with the numbers 1 through 9 on them. We take turns picking up cards and putting them in our hands. There is no discarding.

The game ends in one of two ways. If we run out of cards to pick up, the game is a draw. But if one player has a set of three cards in his or her hand that add up to exactly 15 before we run out of cards, that player wins. (For example, if you had 2, 4, 6 and 7, you would win with the 2, 6 and 7. However, if you had 1, 2, 3, 7 and 8, you haven’t won because no set of three cards adds up to 15.)

Let’s say you go first. With perfect play, who wins and why?

--------

Work

First, find all ways to get 15 (sets)

- Just with good old-fashioned pencil and paper, these are the eight sets possible:

1 5 9
1 6 8
2 4 9
2 5 8
2 6 7
3 4 8
3 5 7
4 5 6

- These form a magic square, where every column, row, and diagonal sum to 15
- Can be written out pretty easily (5 must go in center, etc.)

|   |   |   |
| 2 | 9 | 4 |
|   |   |   |
-------------
|   |   |   |
| 7 | 5 | 3 |
|   |   |   |
-------------
|   |   |   |
| 6 | 1 | 8 |
|   |   |   |

- Now we just play tic tac toe since both players are shooting for three numbers that sum to 15 (no discards and no repeats)
- If both play perfectly, they always draw, do I believe the answer is no one wins. What a nice card game.

'''