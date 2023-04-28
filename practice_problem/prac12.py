# Mubashir needs your help to find out number of animals hidden in a given string txt.
#
# You are provided with an array of animals given below:
#
# animals = ["dog", "cat", "bat", "cock", "cow", "pig",
# "fox", "ant", "bird", "lion", "wolf", "deer", "bear",
# "frog", "hen", "mole", "duck", "goat"]
# Rule: Return the maximum number of animal names. See the below example:
#
# txt = "goatcode"
#
# count_animals(txt) ➞ 2
# # First animal = "dog"
# # Remaining string = "atcoe",
# # Second animal = "cat".
# # count = 2 (correct)
#
# # If you got a "goat" first time
# # remaining string = "code",
# # no animal will be found during next time.
# # count = 1 (wrong)
# Examples
# count_animals("goatcode") ➞ 2
# # "dog", "cat"
#
# count_animals("cockdogwdufrbir") ➞ 4
# # "cow", "duck", "frog", "bird"
#
# count_animals("dogdogdogdogdog") ➞ 5

def count_animals(a_str):
    a_list = list(a_str)
    # print(a_list)
    animals = ["dog", "cat", "bat", "cock", "cow", "pig",
    "fox", "ant", "bird", "lion", "wolf", "deer", "bear",
    "frog", "hen", "mole", "duck", "goat"]
    count = 0
    b = ''
    for ani_name in animals:
        a = ''
        for j in ani_name:
            if j in a_list:
                a += j
                a_list.remove(j)
                # ind = a_list.index(j)
                # a_list.pop(ind)
            print()
        if a in animals:
            count += 1
            b += a + " "

    return f"Animals = {b} \n and \n count/ no. of elements = {count}"


if __name__ == '__main__':
    print(count_animals("goatcode"))
    print()
    print(count_animals("cockdogwdufrbir"))
    print()
    print(count_animals("dogdogdogdogdog"))
