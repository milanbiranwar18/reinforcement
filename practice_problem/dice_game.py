"""
# "John is playing a dice game. The rules are as follows.
# Roll two dice.
# Add the numbers on the dice together.
# Add the total to your overall score.
# Repeat this for three rounds.
# But if you roll DOUBLES, your score is instantly wiped to 0 and your game ends immediately!
# Create a function that takes in a list of tuples as input, and return John's score after his game has ended.
# Examples
# dice_game([(1, 2), (3, 4), (5, 6)]) ➞ 21
# dice_game([(1, 1), (5, 6), (6, 4)]) ➞ 0
# dice_game([(4, 5), (4, 5), (4, 5)]) ➞ 27
"""


def dice_game(a_list):
    a = 0
    for i in range(len(a_list)):
        for j in range(len(a_list[i])-1):
            if a_list[i][j] == a_list[i][j+1]:
                return 0
            a += a_list[i][j] + a_list[i][j+1]
    return a


if __name__ == '__main__':
    print(dice_game([(1, 2), (3, 4), (5, 6)]))
    print(dice_game([(1, 1), (5, 6), (6, 4)]))
    print(dice_game([(4, 5), (4, 5), (4, 5)]))