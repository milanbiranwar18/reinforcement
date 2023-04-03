import timeit
import pandas as pd
import numpy as np


# step - 1
def numpy_floating_number(array_sizes):
    a_list = []
    for i in array_sizes:
        r_num = np.random.rand(i)
        a_list.append(r_num)
    return a_list


# step 2
def array_with_different_algorithms(array_sizes):
    a_list = []
    sort_methods = ['quicksort', 'mergesort', 'heapsort']
    for size in array_sizes:
        sorted_list = np.random.rand(size)
        for algorithm in sort_methods:
            sorting_time_ms = timeit.timeit(lambda: np.sort(sorted_list, kind=algorithm), number=1)
            a_list.append(f'Sorting time for {size} using {algorithm} is {sorting_time_ms} millisecond')
    return a_list


# step 3
def array_and_algorithm_as_a_input(array, algo):
    a_list = []
    for array_size in array:
        size = int(array_size)
        sorted_list = np.random.rand(size)
        quicksort_time = timeit.timeit(lambda: np.sort(sorted_list, kind=algo), number=1)
        a_list.append(f"size-{size} and sorting time-{quicksort_time} millisecond")
    return a_list


# step 4
def storing_output_in_dictionary(array, algo):
    a_dict = {}
    sorted_list = np.random.rand(array)
    quicksort_time = timeit.timeit(lambda: np.sort(sorted_list, kind=algo), number=1)
    a_dict.update({f"{algo}-{array}": f"{quicksort_time:.5f}"})
    return a_dict


if __name__ == '__main__':
    array_sizes = [1, 2, 5, 10]
    while True:
        print("Enter 1 for step 1 or to call numpy_floating_number()")
        print("Enter 2 for step 2 or to call array_with_different_algorithms()")
        print("Enter 3 for step 3 or to call array_and_algorithm_as_a_input()")
        print("Enter 4 for step 4 or to call storing_output_in_dictionary()")
        print("Enter 5 for step 5 or to call list_of_dictionary_for_each_algorithm()")
        print("Enter 0 for exist")

        choice = int(input("Enter number"))
        if choice == 1:
            obj = numpy_floating_number(array_sizes)
            print(obj)
        elif choice == 2:
            print(array_with_different_algorithms(array_sizes))
        elif choice == 3:
            user_input_array = input("Enter the array element as a values of size with space")
            user_input_algo = input("Enter algorithm name quicksort or mergesort or heapsort")
            print(array_and_algorithm_as_a_input(user_input_array, user_input_algo))
        elif choice == 4:
            user_input_array = int(input("Enter the array element as a values of size with space"))
            user_input_algo = input("Enter algorithm name quicksort or mergesort or heapsort")
            print(storing_output_in_dictionary(user_input_array, user_input_algo))
        elif choice == 5:
            a_list = []
            while True:
                print("Enter 6 for calculating sorting time in milliseconds using algorithm for size")
                print("Enter 7 for print output")
                print("Enter 0 for exist")
                choice = int(input("Enter choice"))
                if choice == 6:
                    user_input_array = input("Enter the array element as a values of size with space")
                    user_input_algo = input("Enter algorithm name quicksort or mergesort or heapsort")
                    obj = storing_output_in_dictionary(user_input_array, user_input_algo)
                    a_list.append(obj)
                elif choice == 7:
                    print(a_list)
                elif choice == 0:
                    break
        elif choice == 0:
            break












