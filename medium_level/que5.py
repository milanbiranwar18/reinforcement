# Write a program that takes a list of integers and returns a new list where each element is the product of all the
# other elements in the original list.

def product_of_ele(a_list):
    b_list = []
    for i in range(len(a_list)):
        for j in a_list[i]:
            pass


if __name__ == '__main__':
    print(product_of_ele([2, 1, 3, 4, 5, 6]))