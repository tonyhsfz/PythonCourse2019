from random import shuffle
from statistics import mean
import time
import random
import matplotlib.pyplot as plt

# define insertion sort function
def insert_sort(list):
    # starting from the second element
    for i in range(1, len(list)):
        # compare it with every element before
        for j in range(i):
            # if smaller then pop it out and insert it before that element
            if list[i] < list[j]:
                element = list[i]
                list.pop(i)
                list.insert(j, element)
    return list

# define quick sort function
def quick_sort(list):
    # if the length equals 0 or 1, then return the list
    if len(list) <= 1:
        return list
    else:
        # if the length greater than 1, then divide the list in the following way
        list_left = []
        list_middle = []
        list_right = []
        for i in list:
            # use the first element as a divider
            # any element that is greater than the divider than append it to the right list
            # any element that is smaller than the divider than append it to the left list
            # any element that is equal to the divider than append it to the middle list
            if i < list[0]:
                list_left.append(i)
            elif i == list[0]:
                list_middle.append(i)
            else:
                list_right.append(i)
        # use recursion to sort each list
        return quick_sort(list_left) + list_middle + quick_sort(list_right)

# define bubble sort function
def bubble_sort(list):
    swapped = True
    for i in range(1, len(list)):
        # if never swapped than stop the sorting process
        while swapped == True:
            swapped = False
            # for each neighboring pairs, if the order is incorrect then swap them
            for j in range(len(list) - i):
                if list[j] > list[j+1]:
                    list[j], list[j+1] = list[j+1], list[j]
                    swapped = True
        return list

# define a function to record the running time for insertion sort
def timed_insert_sort(list_len, list_max, repeat):
    list_list = []
    # repeat the sorting process for a given time such that the difference is noticeable
    for i in range(repeat):
        list = []
        # create a random list from random integer 1 to list_max with length list_len
        for j in range(list_len):
            list.append(random.randint(1, list_max))
        list_list.append(list)
    # record the starting time of the sorting
    start_time = time.time()
    # sort all the lists
    for item in list_list:
        item = insert_sort(item)
    # record the ending time
    end_time = time.time()
    # return the difference in time to get the runtime
    return end_time-start_time

# define a similar function to record the running time for quick sort
def timed_quick_sort(list_len, list_max, repeat):
    list_list = []
    for i in range(repeat):
        list = []
        for j in range(list_len):
            list.append(random.randint(1, list_max))
        list_list.append(list)
    start_time = time.time()
    for i in range(len(list_list)):
        list_list[i] = quick_sort(list_list[i])
    end_time = time.time()
    return end_time-start_time

# define a similar function to record the running time for bubble sort
def timed_bubble_sort(list_len, list_max, repeat):
    list_list = []
    for i in range(repeat):
        list = []
        for j in range(list_len):
            list.append(random.randint(1, list_max))
        list_list.append(list)
    start_time = time.time()
    for item in list_list:
        item = bubble_sort(item)
    end_time = time.time()
    return end_time-start_time

# create lists of runtime for each sorting algorithm
list_insert = []
list_quick = []
list_bubble = []
# each sorting algorithm calculates a random list with length i 1000 times
for i in range(1, 201):
    list_insert.append(timed_insert_sort(i, 50, 1000))
    list_quick.append(timed_quick_sort(i, 50, 1000))
    list_bubble.append(timed_bubble_sort(i, 50, 1000))

# plot out the runtime
# x-axis: length of the lists
x = range(1, 201)
# y-axis: runtime for each algorithm
y1 = list_insert
y2 = list_quick
y3 = list_bubble
plt.subplots_adjust(left = .13, right = .95, top = .9, bottom = .3)
plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)
plt.legend(['Insertion Sort', 'Quick Sort', 'Bubble Sort'], loc = "upper left", prop = {"size":10})
plt.ylabel("Runtime for sorting 1000 times")
plt.xlabel("length of the list")
plt.title("The Effect of Different Sorting Algorithms on Runtime")
txt = """
This plot shows the runtime for three different sorting algorithms:
Insertion Sort, Quick Sort, and Bubble Sort.
It tests the runtime of sorting a list consisting random numbers from 1 to 50
with length x (from 1 to 200) for each algorithm.
"""
plt.figtext(.5, .05, txt, fontsize = 9, ha = "center")
plt.savefig('HW4_Tony_plot.pdf')
