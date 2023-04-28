# First Way

# Sorting a string
# using join() + sorted()

# initializing string
test_string = "geekforgeeks"

# printing original string
print("The original string : " + str(test_string))

# using join() + sorted()
# Sorting a string
res = ''.join(sorted(test_string))

# print result
print("String after sorting : " + str(res))





# Second way

string = input("Enter String: ")
lst = [string[i] for i in range(0, len(string))]
lst.sort()
for i in lst:
    print(i, end="")
    