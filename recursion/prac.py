def reverce(num, result):
    if num==0:
        return result
    if num > 0:
        temp = num % 10
        result = (result * 10) + temp
    return reverce(num//10, result)


def max_num(a_list, n, num):
    if n == 0:
        return num
    if n>0:
        if num < a_list[n]:
            num = a_list[n]
    return max_num(a_list, n-1, num)


def even_num(num, num1):
    if num == num1:
        return
    if num < num1:
        print(num)
    return even_num(num+2, num1)


if __name__ == '__main__':
    # num = 12564
    # result = 0
    # a = reverce(num, result)
    # print(a)
    # for palindrome
    # if a==num:
    #     print(True)
    # else:
    #     print(False)

    # a_list = [1, 0, 83, 5, 10, 63, 12, 7]
    # n = len(a_list)-1
    # num = a_list[0]
    # print(max_num(a_list, n, num))

    num = int(input("Enter num"))
    num1 = int(input("Enter num"))
    if num%2==1:
        num += 1
    else:
        num = num

    print(even_num(num, num1))
