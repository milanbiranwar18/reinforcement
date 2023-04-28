# METHOD 6:Using a dictionary
#
# APPROACH:
#
# This program sorts a given input string in ascending order based on the characters present in it. It uses a dictionary
# to count the frequency of each character and then sorts them based on the ASCII value of the character.
#
# ALGORITHM:
#
# 1.Initialize an empty dictionary to store the count of each character in the input string.
# 2.Loop through each character in the input string and update the count of that character in the dictionary.
# 3.Create an empty string to store the sorted string.
# 4.Loop through each character in the sorted list of keys of the dictionary and add that character multiplied by its
# count in the input string to the sorted string.
# 5.Print the original string and the sorted string.


# Approach 4: Using a dictionary to count the characters
input_string = "geekforgeeks"

char_count = {}
for char in input_string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

sorted_string = ""
for char in sorted(char_count.keys()):
    sorted_string += char * char_count[char]

print("Original string: {}".format(input_string))
print("String after sorting: {}".format(sorted_string))


# Time Complexity:
# The time complexity of this algorithm is O(nlogn) due to the use of the sorted() function.
#
# Space Complexity:
# The space complexity of this algorithm is O(n) due to the use of the dictionary to store the count of each character.


