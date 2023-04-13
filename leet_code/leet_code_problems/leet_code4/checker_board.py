# Create a checker board generator, which takes as inputs n and 2 elements to generate an n x n checkerboard with those
# two elements as alternating squares.
# Examples
# checker_board(2, 7, 6) ➞ [
#   [7, 6],
#   [6, 7]
# ]
#
# checker_board(3, "A", "B") ➞ [
#   ["A", "B", "A"],
#   ["B", "A", "B"],
#   ["A", "B", "A"]
# ]
#
# checker_board(4, "c", "d") ➞ [
#   ["c", "d", "c", "d"],
#   ["d", "c", "d", "c"],
#   ["c", "d", "c", "d"],
#   ["d", "c", "d", "c"]
# ]
#
# checker_board(4, "c", "c") ➞ "invalid"
# Notes
# Both elements can be either strings or integers.
# The first element should be on the upper left corner of the checker board. e.g. "c", not "d" should be element [0][0]
# for example 3.
# Return "invalid" if both inputs are identical (see example 4).

def checker_board(n, ele1, ele2):
    a_list = []
    c_list = [ele1, ele2]
    count = 0
    # for i in range(n):
    #     b_list = []
    #     for j in range(n):
    #         if i%2==0:
    #             if j%2==0:
    #                 b_list.append(c_list[0])
    #                 # b_list.append(ele2)
    #             else:
    #                 b_list.append(c_list[1])
    #                 # b_list.append(ele1)
    #         else:
    #             if j%2==1:
    #                 b_list.append(c_list[0])
    #                 # b_list.append(ele2)
    #             else:
    #                 b_list.append(c_list[1])
    #                 # b_list.append(ele1)
    #
    #         a_list.append(b_list)
    # print(a_list)
    # # a_list.append()

    # if ele1 == ele2:
    #     return "invalid"
    # else:
    # # for y in range(n):
    # #     for x in range(n):
    # #         a_list.append(0)

    if ele1 == ele2:
        return "invalid"
    else:
        # matrix = [[0 for x in range(n)] for y in range(n)]
        a_list = []
        for y in range(n):
            b_list = []
            for x in range(n):
                b_list.append(0)
            a_list.append(b_list)
        for i in range(n):
            for j in range(n):
                if (i + j) % 2 == 0:
                    a_list[i][j] = ele1
                else:
                    a_list[i][j] = ele2
        return a_list


if __name__ == '__main__':
    print(checker_board(2, 7, 6))
    print(checker_board(3, "A", "B"))
    print(checker_board(4, "c", "d"))
    print(checker_board(4, "c", "c"))