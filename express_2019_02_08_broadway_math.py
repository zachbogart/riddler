'''
https://fivethirtyeight.com/features/525600-minutes-of-math/

What are the chances three random integers create a product divisible by 100?

Notes:
    - not sure if I'm doing this right...
'''

from datetime import datetime

start = datetime.now()

debug = False

number_of_ways = 0
ways = []

# find all ways to get product of 100 from three integers (like a tree)
for first in range(1, 101):
    for second in range(1, 101):
        for third in range(1, 101):
            product = first * second * third
            if product % 100 == 0:
                print(f"{first} {second} {third}")
                ways.append([first, second, third])
                number_of_ways += 1

print(f"\nNumber of ways: {number_of_ways}\n")

# find probability
branch_fraction = 1 / number_of_ways
total_probability = 0

# go through ways and multiply out odds (Ex. 1/50th of integers are divisible by 50)
for way in ways:
    first_prob = 1 / way[0]
    second_prob = 1 / way[1]
    third_prob = 1 / way[2]

    branch_probability = branch_fraction * (first_prob * second_prob * third_prob)

    if debug:
        print(f"{branch_fraction} * ({first_prob} * {second_prob} * {third_prob} = {branch_probability}")

    # add branch to total
    total_probability += branch_probability

print("\nTotal Probability: ", total_probability)

end = datetime.now()
print("Time to execute: ", end - start)