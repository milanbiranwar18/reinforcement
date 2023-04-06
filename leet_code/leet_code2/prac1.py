# nums = [3, 30, 34, 5, 9]
# a = ''
# # for ele in nums:
# #     a += str(ele)
# b = [str(ele) for ele in nums]
# print(b)


def word_pattern(a, b):
    global f
    c = list(a)
    d = b.split()
    e = []
    f = 0
    for i in range(len(c)-1):
        for j in c[i+1]:
            if c[i] == j:
                e.append(i)
                e.append(c.index(j))

        # if i in c[c.index(i)::]:
        #     ab = c.index(i)

        # if c.count(i) > 1:
        #     # ab = c.index()
        #     e.append(f)
        # f+=1
            # e.add(c.index(i))
            # f = tuple(e)
    # print(f)
    print(e)


    # c = d
    # print(sorted(c))
    # print(sorted(d))
    # e = len(set(a)) == len(set(d))


def max_product_of_word_lengths(a_list):
    for ind in range(len(a_list)-1):

        if len(a_list[ind]) == len(a_list[ind + 1]):
            return len(a_list[ind]) * len(a_list[ind + 1])
        return 0


if __name__ == '__main__':
    # print(word_pattern("abba", "dog cat cat dog"))

    print(max_product_of_word_lengths(["abcw","baz","foo","bar","xtfn","abcdef"]))