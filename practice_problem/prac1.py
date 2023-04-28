# # a_str = 'abcd'
# # # first way
# # b_str = a_str[::-1]
# # print(b_str)
# #
# # # second way
# # a = ''
# # for i in a_str:
# #     a = i + a
# # print(a)
txt = "dogdogdogdogdog"

animals = ["dog", "cat", "bat", "cock", "cow", "pig",
"fox", "ant", "bird", "lion", "wolf", "deer", "bear",
"frog", "hen", "mole", "duck", "goat"]
count = 0
b = ''
c = ''
# for i in range(len(animals)):
for animal in animals:
    if txt.startswith(animal):
        print(animal)


# a = ['a', 'a', 'e', 'f']
# ab = 'abc'
# for i in a:
#     print(i)
#     # if i in ab:
#     #     a.remove(i)
# # print(a)
