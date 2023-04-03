# Direct Recursion
def natural_num(n):
    if n <= 0:
        return
    print(n, end=" ")
    return natural_num(n - 1)


# Indirect Recursion
def natu_num(n):
    if n <= 0:
        return
    print(n, end=" ")
    return natu_num_one(n-1)


def natu_num_one(n):
    print(n, end=" ")
    return natu_num(n-1)


if __name__ == '__main__':
    natural_num(20)
    print('\n')
    natural_num(10)
    print('\n')
    natu_num(30)
    print('\n')
    natu_num(10)
