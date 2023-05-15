# given a list of integers, write a function that returns the longest increasing subsequesnce in the list
def longest_increasing_subsequesnce(a_list):
    b_list = []
    for i in range(len(a_list)-1):
        if len(b_list) == 0:
            b_list.append(a_list[0])
        if a_list[i] < a_list[i+1] and a_list[i+1] not in b_list:
            b_list.append(a_list[i+1])
    return b_list


if __name__ == '__main__':
    print(longest_increasing_subsequesnce([1, 2, 5, 6, 8, 7, 4, 3, 5, 10, 20, 15]))


