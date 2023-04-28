# In the Code tab is a function which is meant to return how many uppercase letters there are in a list of various words
# . Fix the list comprehension so that the code functions normally!
#
# Examples
# count_uppercase(["SOLO", "hello", "Tea", "wHat"]) ➞ 6
#
# count_uppercase(["little", "lower", "down"]) ➞ 0
#
# count_uppercase(["EDAbit", "Educate", "Coding"]) ➞ 5

def count_uppercase(a_list):
    count = 0
    for a_str in a_list:
        for i in a_str:
            if i.isupper():
                count += 1
    return count


if __name__ == '__main__':
    print(count_uppercase(["SOLO", "hello", "Tea", "wHat"]))
    print(count_uppercase(["little", "lower", "down"]))
    print(count_uppercase(["EDAbit", "Educate", "Coding"]))