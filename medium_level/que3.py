# Write a program that takes a list of strings and returns a new list where each string has been shortened to its first
# two characters.

def first_two_char(a_list):
    b_list = []
    for i in a_list:
        a_str = ''
        for j in range(len(i)):
            if j < 2:
                a_str += i[j]
        b_list.append(a_str)
    return b_list


if __name__ == '__main__':
    print(first_two_char(['book', 'read', 'hello', 'brother']))
