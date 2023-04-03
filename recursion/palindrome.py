def pal(n, t):
    if n == 0:
        return t
    t = (t * 10) + (n % 10)
    return pal((n // 10), t)


if __name__ == '__main__':

    num = int(input("Enter any Number"))
    temp = 0
    p = pal(num, temp)
    if num == p:
        print(num, "is a palindrome number")
    else:
        print(num, 'is not a palindrome number')
