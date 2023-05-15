def sum_of_digit(num):
    if len(str(num)) == 1:
        return num
    else:
        res = 0
        num = str(num)
        for i in num:
            i = int(i)
            res += i
        return sum_of_digit(res)


if __name__ == '__main__':
    print(sum_of_digit(7812))
    print(sum_of_digit(6556))
    print(sum_of_digit(90))
    print(sum_of_digit(101))

