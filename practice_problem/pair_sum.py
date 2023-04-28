# First Approach
def pair_sum(a_list, k):
    a = []
    for i in range(len(a_list)):
        for j in range(i+1, len(a_list)):
            if a_list[i]+a_list[j] == k:
                a.append((a_list[i], a_list[j]))
    return a


# Second Approach / Another way
def pair_sum_another_way(a_list, k):
    if len(a_list) < 2:
        return
    seen = set()
    output = set()

    for num in a_list:
        target = k - num
        if target not in seen:
            seen.add(num)
        else:
            output.add((min(num, target), max(num, target)))
    return output, len(output)


if __name__ == '__main__':
    print(pair_sum([1, 3, 2, 2], 4))
    print(pair_sum_another_way([1, 3, 2, 2], 4))
