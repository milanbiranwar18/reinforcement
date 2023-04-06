def minimize_maximum_of_list(a_list):
    a = 0
    b = 0
    for i in range(len(a_list)):
        a += a_list[i]
        c = i + 1
        d = a + i
        b = max(b, d//c)
    return int(b)


if __name__ == '__main__':
    print(minimize_maximum_of_list([3,7,1,6]))
    print(minimize_maximum_of_list([10,1]))
