def count_same_num(a_list):
    b_list = []
    a_dict = {}
    for i in a_list:
        if i not in b_list:
            b_list.append(i)
            a_dict.update({i: a_list.count(i)})
    return a_dict


def count_list_ele(a_list):
    a_dict = {}
    for i in a_list:
        if i not in a_dict.keys():
            a_dict.update({i: 1})
        # elif i in a_dict.keys():
        else:
            a_dict.update({i: (a_dict.get(i) + 1)})
    return a_dict


if __name__ == '__main__':

    print(count_same_num([1, 1, 1, 2, 3, 1, 5, 5, 4, 6, 6, 5, 4, 2, 2, 3, 4, 5]))

    print(count_list_ele([1, 1, 1, 2, 3, 1, 5, 5, 4, 6, 6, 5, 4, 2, 2, 3, 4, 5]))
