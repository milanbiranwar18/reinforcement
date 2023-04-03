def odd(a, b):
    if a > b:
        return
    print(a)
    return odd(a + 2, b)


if __name__ == '__main__':

    x = int(input("Enter first number"))
    y = int(input("Enter last number"))
    if x % 2 != 0:
        x = x
    else:
        x = x + 1

    odd(x, y)
