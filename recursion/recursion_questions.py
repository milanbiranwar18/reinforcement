# TODO:  Find the Highest Integer in the List Using Recursion.
def highest_ele(a_list, num, maxi):
    if num == 0:
        return maxi
    if num>0:
        if a_list[num]>maxi:
            maxi=a_list[num]
    return highest_ele(a_list, num-1, maxi)


# TODO:  Find the smallest Integer in the List Using Recursion.
def smallest_num(a_list, len, small):
    if len == 0:
        return small
    elif len > 0:
        if small > a_list[len]:
            small = a_list(len)
    return smallest_num(a_list, len-1, small)


# TODO:  Find the even numbers
def even_num(a, b):
    if a>b:
        return
    print(a)
    return even_num(a+2, b)


# TODO:  Find the prime number
def prime_num(num, i):
    if i == 1:
        return 1
    if (num%i) == 0:
        return 0
    return prime_num(num, i-1)


# TODO:  Find sum of even number
def even_num_sum(a, b, s):
    if a>b:
        return s
    s=s+a
    # print(a)
    return even_num_sum(a+2, b, s)


# TODO:  Sort list using bubble sort and recursion
def sort_bubble_recursion(a):
    for i in range(len(a)-1):
        if a[i]>a[i+1]:
            temp = a[i]
            a[i] = a[i+1]
            a[i+1] = temp
            # a[i], a[i+1] = a[i+1], a[i]
            sort_bubble_recursion(a)
    return a


# TODO:  Sort list using bubble sort and recursion
def swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp


def bubble_sort(a, n):
    for i in range(n-1):
        if a[i] > a[i+1]:
            swap(a, i, i+1)
    if (n-1) > 1:
        bubble_sort(a, n-1)


# TODO 5.  Pick Squares
#  Write a function for picking up the numbers which are squares of positive integers from a given array and do a sort
#  which is not a brute force sort or a bubble sort. Basically the complexity of the algorithm should be lease than
#  O(n2)
#  Example 1:
#  Input: [169,145,225,211,121,183,100,111,196,214,275]
#  Output: [100,121,169,196,225]
#  Increasing digits Sum

def odd_num(a, b):
    if (a%2) == 1:
        return a


# Length of Last Word
# Given a string s consisting of words and spaces, return the length of the last word in the string.
#
# A word is a maximal substring consisting of non-space characters only.
#
# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
#
# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.

def length_last_word(s):

    x = s.split()
    a = 0
    for i in x[-1]:
        a+=1
    return a


def length_of_last_word(s):
    if len(s) == 1 and s[0] != ' ':
        return 1
    n = len(s) - 1
    i = len(s) - 1
    while i >= 0:
        if s[i] == ' ':
            if n - i != 0 and s[i+1] != ' ':
                return n - i
            else:
                n = i - 1
        i -= 1
    if s[0] != ' ':
        return n + 1
    return 0


if __name__ == '__main__':
    # a_list = [-1, 3, 5, 6, 99, 12, 2]
    # maxi = a_list[0]
    # num = len(a_list)-1
    # print(highest_ele(a_list, num, maxi))
    # print()
    #
    # a = [-1, 3, 5, 6, 99, 12, 2]
    # b = len(a)-1
    # small = a[0]
    # print(smallest_num(a, b, small))
    # print()

    # x, y = 1, 20
    # if x % 2 == 0:
    #     x = x
    # else:
    #     x += 1
    # even_num(x, y)
    print()

    # num = 20
    # n = prime_num(num, num//2)
    # if n==1:
    #     print(num, "is a prime number")
    # else:
    #     print(num, "is not a prime number")

    # x, y, s = 1, 20, 0
    # if (x%2)==0:
    #     x=x
    # else:
    #     x+=1
    # print("Sum of even numbers is ", even_num_sum(x, y, s))

    # a = [4, 3, 5, 6, 99, 12, 2]
    # print(sort_bubble_recursion(a))

    # a = [3, 5, 8, 4, 1, 9, -2]
    # b = len(a)
    # bubble_sort(a, b)

    # print(a)

    # s = "Hello World"
    s = "   fly me   to   the moon  "
    # print(length_last_word(s))

    print(length_of_last_word(s))



