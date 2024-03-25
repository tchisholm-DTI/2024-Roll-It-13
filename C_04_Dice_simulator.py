import random


# Generates an integer between 0 and 6
# to simulate a roll of a die
def roll_dice():
    result = random.randint(1, 6)
    return result


# Main routine goes here
for item in range(0, 10):
    user_score = 0
    double_score = "no"

    # Roll two dice
    roll_1 = roll_dice()
    roll_2 = roll_dice()

    # Check if we have a double score opportunity
    if roll_1 == roll_2:
        double_score = "yes"

    # Find the total points so far
    user_points = roll_1 + roll_2

    # Show the user the results
    print(f"Die 1: {roll_1} \t Die 2: {roll_2} \t Points: {user_points}")
    print(f"Double score opportunity: {double_score}")


