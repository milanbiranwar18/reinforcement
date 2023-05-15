# Given a list of integers, write a function that returns the difference between the sum of the even numbers and the
# sum of the odd numbers in the list.

def diff_of_sum_odd_even(a_list):
    odd = []
    even = []
    [even.append(num) if num % 2 == 0 else odd.append(num) for num in a_list]
    return (sum(even) - sum(odd))


if __name__ == '__main__':
    print(diff_of_sum_odd_even([1, 2, 3, 4, 5, 6, 5, 7, 8, 9]))
