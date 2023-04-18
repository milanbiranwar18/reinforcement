# #Create a function that returns the majority vote in a list. A majority vote is an element that occurs > N/2 times in
# a list (where N is the length of the list).
#
# Examples
# majority_vote(["A", "A", "B"]) ➞ "A"
#
# majority_vote(["A", "A", "A", "B", "C", "A"]) ➞ "A"
#
# majority_vote(["A", "B", "B", "A", "C", "C"]) ➞ None
# Notes
# The frequency of the majority element must be strictly greater than 1/2.
# If there is no majority element, return None.
# If the list is empty, return None.
import math


def majority_vote(a_list):
    n = len(a_list)/2
    n = math.ceil(n)
    for i in range(len(a_list)):
        if a_list.count(a_list[i]) >= n:
            return a_list[i]
        else:
            return None


if __name__ == '__main__':
    print(majority_vote(["A", "A", "B"]))
    print(majority_vote(["A", "C", "B"]))
    print(majority_vote(["A", "A", "A", "B", "C", "A"]))
    print(majority_vote(["A", "B", "B", "A", "C", "C"]))
