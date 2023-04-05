import timeit
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


a_list = []


# step 4
def storing_output_in_dictionary(user_input_array, user_input_algo):
    a_dict = {}
    sorted_list = np.random.rand(user_input_array)
    quicksort_time = timeit.timeit(lambda: np.sort(sorted_list, kind=user_input_algo), number=1) * 1000
    a_dict.update({"algorithm-size":f'{user_input_algo}-{user_input_array}', "sorting_time": f"{quicksort_time:.5f}ms"})
    return a_dict


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
    df = pd.read_csv('sort_size.csv')
    data = dict()
    for _, row in df.iterrows():
        algorithm = row['algorithm-size']
        sorting_time = row['sorting_time']
        data[algorithm] = float(sorting_time[:-2])
    positions = [0, 1]
    fig, ax = plt.subplots()
    for i, l in enumerate(data.keys()):
        ax.bar(x=l, height=data[l], color='g')
        ax.text(l, data[l] + 0.2, f"{data[l]:.2f}ms", ha='center')
    ax.set_ylim(bottom=0)
    ax.set_xlabel('Algorithm')
    ax.set_title('Sorting Algorithms')
    plt.show()


if __name__ == '__main__':

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