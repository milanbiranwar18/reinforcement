import timeit
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv


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
def array_and_algorithm_as_a_input(user_input_array, user_input_algo):
    a_list = []
    sorted_list = np.random.rand(user_input_array)
    quicksort_time = timeit.timeit(lambda: np.sort(sorted_list, kind=user_input_algo), number=1)
    a_list.append(f"size-{user_input_array} and sorting time-{quicksort_time} millisecond")
    return a_list


# step 4
def storing_output_in_dictionary(user_input_array, user_input_algo):
    a_dict = {}
    sorted_list = np.random.rand(user_input_array)
    quicksort_time = timeit.timeit(lambda: np.sort(sorted_list, kind=user_input_algo), number=1)
    a_dict.update({"algorithm-size":f'{user_input_algo}-{user_input_array}', "sorting_time": f"{quicksort_time:.5f}ms"})
    return a_dict


class UI:
    @staticmethod
    def numpy_floating_num():
        print(numpy_floating_number(array_sizes))

    @staticmethod
    def array_with_different_algo():
        print(array_with_different_algorithms(array_sizes))

    @staticmethod
    def array_and_algo_as_a_input():
        user_input_array = int(input("Enter the array size : "))
        user_input_algo = input("Enter algorithm name quicksort or mergesort or heapsort : ")
        print(array_and_algorithm_as_a_input(user_input_array, user_input_algo))

    @staticmethod
    def storing_output_in_dict():
        user_input_array = int(input("Enter the array size : "))
        user_input_algo = input("Enter algorithm name quicksort or mergesort or heapsort : ")
        print(storing_output_in_dictionary(user_input_array, user_input_algo))

    @staticmethod
    def store_in_list():
        a_list = []
        while True:
            print("1 for calculating sorting time in milliseconds using algorithm for size\n2 for output\n"
                  "3 To convert list of dict to pandas dataframe\n4 To convert list of dict to csv file\n"
                  "5 for performance data\n0 for exist")

            choice = int(input("Enter any option : "))
            if choice == 1:
                user_input_array = int(input("Enter the array size : "))
                user_input_algo = input("Enter algorithm name quicksort or mergesort or heapsort : ")
                obj = storing_output_in_dictionary(user_input_array, user_input_algo)
                a_list.append(obj)
            elif choice == 2:
                print(a_list)
            elif choice == 3:
                df = pd.DataFrame(a_list)
                df = df.set_index('algorithm-size')
                # df2 = df.to_string(index=False)
                # print(df2)
                print(df.shape)

            elif choice == 4:
                df = pd.DataFrame(a_list)
                df.to_csv('sort_size.csv', index=False)
            elif choice == 5:
                x = []
                y = []

                with open('sort_size.csv', 'r') as csvfile:
                    plots = csv.reader(csvfile, delimiter=',')
                    for row in plots:
                        x.append(row[0])
                        y.append(row[1])

                plt.bar(x, y, color='g', width=0.4, label="Sorting Time")
                plt.xlabel('algorithm-size')
                plt.ylabel('sorting_time')
                plt.title('sorting time of various algorithm')
                plt.legend()
                plt.show()

            elif choice == 0:
                break


if __name__ == '__main__':
    array_sizes = [1000, 5000, 10000, 50000, 100000, 500000, 1000000]

    while True:
        print("Options\n1 for numpy_floating_number\n2 for array_with_different_algorithms\n3 for "
              "array_and_algorithm_as_a_input\n4 for storing_output_in_dictionary\n"
              "5 for list_of_dictionary_for_each_algorithm\n0 for exist")

        choice = int(input("select any option between 0-5 : "))

        options = {1: UI.numpy_floating_num,
                   2: UI.array_with_different_algo,
                   3: UI.array_and_algo_as_a_input,
                   4: UI.storing_output_in_dict,
                   5: UI.store_in_list,
                   }
        if choice == 0:
            break
        else:
            options.get(choice)()
