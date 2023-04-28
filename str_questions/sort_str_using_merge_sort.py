# ALGORITHM:
#
# 1.Define a function called “merge_sort” that takes a string “s” as input.
# 2.If the length of the string “s” is less than or equal to 1, return the string “s”.
# 3.Otherwise, find the middle index of the string “s” and split the string into two halves, left and right.
# 4.Recursively apply the merge_sort function on the left and right halves.
# 5.Merge the left and right halves using the merge function.
# 6.Define another function called “merge” that takes two sorted arrays “left” and “right” as input.
# 7.Initialize an empty list called “result” and two indices, “i” and “j”, both set to 0.
# 8.Compare the first elements of the left and right arrays, and append the smaller one to the result array.
# 9.Increment the index of the array that contributed the smaller element.
# 10.Continue steps 8-9 until one of the arrays is empty.
# 11.Append any remaining elements from the non-empty array to the result array.
# 12.Return the result array.
# 13.Convert the sorted list to a string and print the result.

def merge_sort(s):
    if len(s) <= 1:
        return s
    mid = len(s) // 2
    left = merge_sort(s[:mid])
    right = merge_sort(s[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


s = 'geekforgeeks'
sorted_s = ''.join(merge_sort(list(s)))
print("String after sorting:", sorted_s)
