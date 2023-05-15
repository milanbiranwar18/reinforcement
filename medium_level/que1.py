# Write a program that takes two lists of integers and returns a new list where each element is the sum of the
# corresponding elements from the two input lists.

def sum_of_list_ele(a_list, b_list):
    c_list = []
    for i in range(len(a_list)):
        a = a_list[i] + b_list[i]
        c_list.append(a)
    return c_list


if __name__ == '__main__':
    l1 = int(input("Enter len of first list"))
    l2 = int(input("Enter len of second list"))
    a_list = []
    for i in range(l1):
        a = int(input("Enter element for first list which u want to store in list"))
        a_list.append(a)

    b_list = []
    for i in range(l1):
        a = int(input("Enter element for second list which u want to store in list"))
        b_list.append(a)

    print("First list", a_list)
    print("Second list", b_list)
    print("Sum of two lists element", sum_of_list_ele(a_list, b_list))