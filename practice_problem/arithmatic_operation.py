# "Create a function to perform basic arithmetic operations that includes addition, subtraction, multiplication and
# division on a string number (e.g. ""12 + 24"" or ""23 - 21"" or ""12 // 12"" or ""12 * 21"").
#
# Here, we have 1 followed by a space, operator followed by another space and 2. For the challenge, we are going to
# have only two numbers between 1 valid operator. The return value should be a number.
#
# eval() is not allowed. In case of division, whenever the second number equals ""0"" return
import calendar


def arithmatic_operation(a_string):

    a = a_string.split()

    for i in a:
        if i == '+':
            b = int(a[0]) + int(a[2])
            return b
        elif i == '-':
            b = int(a[0]) - int(a[2])
            return b
        elif i == '*':
            b = int(a[0]) * int(a[2])
            return b
        elif i == '//':
            b = int(a[0]) // int(a[2])
            return b


if __name__ == '__main__':
    # a_string = "12 + 24"
    # a_string = "12 // 12"
    # a_string = "12 * 21"
    a_string = "23 - 21"
    a = arithmatic_operation(a_string)
    print(a)