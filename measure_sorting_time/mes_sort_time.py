import timeit
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


a_list = []
array_sizes = [1000, 5000, 10000, 50000, 100000, 500000, 1000000]


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
            sorting_time_ms = timeit.timeit(lambda: np.sort(sorted_list, kind=algorithm), number=1) * 1000
            a_list.append(f'Sorting time for {size} using {algorithm} is {sorting_time_ms} millisecond')
    return a_list


# step 3
def array_and_algorithm_as_a_input(user_input_array, user_input_algo):
    a_list = []
    sorted_list = np.random.rand(user_input_array)
    quicksort_time = timeit.timeit(lambda: np.sort(sorted_list, kind=user_input_algo), number=1) * 1000
    a_list.append(f"size-{user_input_array} and sorting time-{quicksort_time} millisecond")
    return a_list


# step 4
def storing_output_in_dictionary(user_input_array, user_input_algo):
    a_dict = {}
    sorted_list = np.random.rand(user_input_array)
    quicksort_time = timeit.timeit(lambda: np.sort(sorted_list, kind=user_input_algo), number=1) * 1000
    a_dict.update({"algorithm-size":f'{user_input_algo}-{user_input_array}', "sorting_time": f"{quicksort_time:.5f}ms"})
    return a_dict


def numpy_floating_num():
    print(numpy_floating_number(array_sizes))


def array_with_different_algo():
    print(array_with_different_algorithms(array_sizes))


def array_and_algo_as_a_input():
    user_input_array = int(input("Enter the array size : "))
    user_input_algo = input("Enter algorithm name quicksort or mergesort or heapsort : ")
    print(array_and_algorithm_as_a_input(user_input_array, user_input_algo))


def storing_output_in_dict():
    user_input_array = int(input("Enter the array size : "))
    user_input_algo = input("Enter algorithm name quicksort or mergesort or heapsort : ")
    print(storing_output_in_dictionary(user_input_array, user_input_algo))


def choice_one():
    user_input_array = int(input("Enter the array size : "))
    user_input_algo = input("Enter algorithm name quicksort or mergesort or heapsort : ")
    obj = storing_output_in_dictionary(user_input_array, user_input_algo)
    a_list.append(obj)


def choice_two():
    print(a_list)


def choice_three():
    df = pd.DataFrame(a_list)
    print(df)


def choice_four():
    df = pd.DataFrame(a_list)
    # df.to_csv('sort_size.csv', index=False)
    df.to_csv('sort_size.csv')


def choice_five():
    # Read the data from CSV file
    df = pd.read_csv('sort_size.csv')

    # Initialize a dictionary for algorithms
    data = dict()

    # Store each line in the dictionary
    for _, row in df.iterrows():
        algorithm = row['algorithm-size']
        sorting_time = row['sorting_time']

        data[algorithm] = float(sorting_time[:-2])

    # Define the positions for the subplots
    positions = [0, 1]

    # Plot the subgraphs
    fig, ax = plt.subplots()
    for i, l in enumerate(data.keys()):
        ax.bar(x=l, height=data[l], color='g')
        ax.text(l, data[l] + 0.2, f"{data[l]:.2f}ms", ha='center')

    # Set the y-axis range to start at 0
    ax.set_ylim(bottom=0)

    # Set the x-axis label
    ax.set_xlabel('Algorithm')

    # Set the title
    ax.set_title('Sorting Algorithms')

    # Show the plot
    plt.show()


def store_in_list():

    while True:
        print("1 for calculating sorting time in milliseconds using algorithm for size\n2 for output\n"
              "3 To convert list of dict to pandas dataframe\n4 To convert list of dict to csv file\n"
              "5 for performance data\n0 for exist")

        choice = int(input("Enter any option : "))

        options = {1: choice_one,
                   2: choice_two,
                   3: choice_three,
                   4: choice_four,
                   5: choice_five}
        if choice == 0:
            break
        else:
            options.get(choice)()


if __name__ == '__main__':

    while True:
        print("Options\n1 for numpy_floating_number\n2 for array_with_different_algorithms\n3 for "
              "array_and_algorithm_as_a_input\n4 for storing_output_in_dictionary\n"
              "5 for list_of_dictionary_for_each_algorithm\n0 for exist")

        choice = int(input("select any option between 0-5 : "))

        options = {1: numpy_floating_num,
                   2: array_with_different_algo,
                   3: array_and_algo_as_a_input,
                   4: storing_output_in_dict,
                   5: store_in_list}
        if choice == 0:
            break
        else:
            options.get(choice)()
