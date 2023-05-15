# Given a list of integers, write a function that returns the kth smallest number in the list.
def smallest_num(a_list, k):
    for i in range(len(a_list)-1, 0, -1):
        for j in range(i):
            if a_list[j] > a_list[j+1]:
                a_list[j], a_list[j+1] = a_list[j+1], a_list[j]
    for i in range(len(a_list)):
        if i == k:
            return a_list[i]


if __name__ == '__main__':
    print(smallest_num([5, 6, 4, 8, 1, 3, 2], 2))