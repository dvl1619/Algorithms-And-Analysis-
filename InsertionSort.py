import time
import random
import csv
import matplotlib.pyplot as plt

#Insertion Sort Algorithm Code
def insertion_sort(lst):
    for i in range(1, len(lst)):
        current_element = lst[i]
        j = i
        while j > 0 and current_element < lst[j - 1]:
            lst[j] = lst[j - 1]
            j = j - 1
        lst[j] = current_element

#Analysis Function
def insertionSortAnalysis():

    #Dictionary declaration for storing time and size as key-value pairs
    values = {}

    #Generating random numbers list of size 0,100,200,300.....10000
    for i in range(0, 10001, 100):
        lst = random.sample(range(10000), i)
        #Recording time just before starting insertion sort
        start = time.clock()
        #Applying insertion sort on list
        insertion_sort(lst)
        #Recording time difference just after applying insertion sort on list
        elapsed = (time.clock() - start)
        #Storing key-value pairs of time-size for each list
        values[i] = elapsed

    #Writing key-value pairs as row-col values in an excel csv file
    with open('mycsvfileI.csv', 'wb') as f:
        w = csv.DictWriter(f, values.keys())
        w.writeheader()
        w.writerow(values)
    
    #Plotting results on scattered x-y graph using key-value pairs as x,y pairs
    fig = plt.figure()
    for data_dict in values.values():
        z = data_dict
        x = values.keys()[values.values().index(z)]
        y = data_dict
        plt.scatter(x, y)

    fig.suptitle('Insertion Sort Time Analysis', fontsize=20)
    plt.xlabel('Size Of Array', fontsize=16)
    plt.ylabel('Time(s)', fontsize=16)
    fig.savefig('Time Analysis.png')
    plt.show()
    
insertionSortAnalysis()
