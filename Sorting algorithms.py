###########################################################################
#                           Sorting Algorithms                            #
#                                                                         #
#   Programmed by Maxwell Solko (02/26/2018)                              #
#   Class:  CS300                                                         #
#   Instructor:  Nathaniel Miller                                         #
#                                                                         #
#   Description:  This assignment is about data structures.  We are       #
#                 creating a Linked List, doubly Linked List, stack,      #
#                 queue, and deque.                                       #
#                                                                         #
###########################################################################
import time
from random import shuffle

###########################################################################
#                                   Switch                                #
#   This is a switching method which I use in bubble sort and selection   #
#   sort.  It's a simple method that switches two idexes of a list.       #
###########################################################################

def switch(list, lower, upper):
    temp = list[lower]
    list[lower] = list[upper]
    list[upper] = temp

###########################################################################
#                           Insertion Sort                                #
#   This is insertion sort, which inserts items into a new list one by    #
#   one so they are sorted and returns the new list.  The running time is #
#   O(n^2) due to the nested for loops.                                   #
###########################################################################

def insertionsort(list):
    nlist = []
    for i in range (len(list)):
        count = 0
        for j in range(len(nlist)):
            if list[i]>nlist[j]:
                count += 1
        nlist.insert(count, list[i])
    return nlist

###########################################################################
#                              Bubble Sort                                #
#   This is bubble sort, which compares adjacent values of a list and     #
#   switches them if they are out of order.  This occurs n^2 time, which  #
#   makes the running time O(n^2).                                        #
###########################################################################

def bsort(list):
    for i in range(len(list)):
        for j in range(i):
            # if you want to see steps
            # print(list)
            if list[len(list)-i+j-1] > list[len(list)-i+j]:
                switch(list, len(list)-i+j-1, len(list)-i+j)
    return list

###########################################################################
#                            Selection Sort                               #
#   This is selection sort, which finds the i'th biggest element of the   #
#   list and puts it in the i'th spot.  My selection sort looks for the   #
#   biggest element in a specific range, leaving out the already sorted   #
#   indexes so I only have to look at the biggest value and not the i'th  #
#   biggest value.  This still has O(n^2) running time, albeit n(n+1)/2.  #
###########################################################################

def selectionsort(list):
    for i in range(len(list)):
        winner = 0
        for j in range(len(list)-i):
            if list[j] > list[winner]:
                winner = j
            #print(winner)
        switch(list, len(list)-i-1, winner)
        #print(list)
    return list

###########################################################################
#                                Merge Sort                               #
#   This is merge sort, which breaks down a list into single elements     #
#   (which are sorted by nature) and merging repeatedly larger slices of  #
#   the list together.  Since merging only works with two sorted lists    #
#   and keeps the new list sorted, it's a magical way of sorting without  #
#   sorting.  I didn't find a python method for merging lists, so I       #
#   created my own.  This running time is O(nlog(n)) because it sliced the#
#   list in half repeatedly and looks through the whole list eventually.  #
###########################################################################

def merge(alist, blist):
    nlist = []
    acount = 0
    bcount = 0
    while acount < len(alist) or bcount < len(blist):
        if acount >= len(alist):
            nlist.append(blist[bcount])
            bcount += 1
        elif bcount >= len(blist):
            nlist.append(alist[acount])
            acount += 1
        elif alist[acount] < blist[bcount]:
            nlist.append(alist[acount])
            acount += 1
        else:
            nlist.append(blist[bcount])
            bcount += 1
    return nlist
        
def merge_sort(list):
    #to see steps
    #print(list)
    if len(list) == 1:
        return list
    if len(list) == 0:
        return list
    lowlist = list[:len(list)//2]
    toplist = list[len(list)//2:]
    return merge(merge_sort(lowlist) , merge_sort(toplist))

###########################################################################
#                                Benchmark                                #
#   This is basically the same benchmark function from assignment 2, only #
#   this time it also checks to see whether it actually did sort the list.#
#   I know I didn't need to create csv's to benchmark them, but it helps  #
#   me compare each sorting method.                                       #
###########################################################################

def benchmark(function, list):
    import time
    start = time.time()
    answer = function(list)
    end = time.time()
    didsort = False
    time = end - start
    list.sort()
    if answer == list:
        didsort = True
    return(str(didsort) + "," + str(len(list)) + "," + str(time) + "\n")

###########################################################################
#                               Shuffle Test                              #
#   This test creats a list with the numbers 1 to n and shuffles them for #
#   a random list of numbers.                                             #
###########################################################################

def shuffle_test(f, start_value, number_of_steps, step_size, filename):
    import random
    f_out = open(filename, "w+")
    for i in range(number_of_steps):
        x = start_value + i * step_size
        ulist = []
        for j in range(x):
            ulist.append(j)
        random.shuffle(ulist)
        f_out.write(benchmark(f, ulist))
    f_out.close()

def total_shuffle_test():
    shuffle_test(bsort, 0, 50, 50, "bsortShuffleTest.csv")
    shuffle_test(merge_sort, 0, 50, 50, "mergeShuffleTest.csv")
    shuffle_test(selectionsort, 0, 50, 50, "selectionShuffleTest.csv")
    shuffle_test(insertionsort, 0, 50, 50, "insertionShuffleTest.csv")

###########################################################################
#                                Sorted Test                              #
#   This test creats a list with the numbers 1 to n for a sorted list.    #                                            #
###########################################################################

def sorted_test(f, start_value, number_of_steps, step_size, filename):
    import random
    f_out = open(filename, "w+")
    for i in range(number_of_steps):
        x = start_value + i * step_size
        ulist = []
        for j in range(x):
            ulist.append(j)
        f_out.write(benchmark(f, ulist))
    f_out.close()

def total_sorted_test():
    shuffle_test(bsort, 0, 50, 50, "bsortSortedTest.csv")
    shuffle_test(merge_sort, 0, 50, 50, "mergeSortedTest.csv")
    shuffle_test(selectionsort, 0, 50, 50, "selectionSortedTest.csv")
    shuffle_test(insertionsort, 0, 50, 50, "insertionSortedTest.csv")

###########################################################################
#                                Reversed Test                            #
#   This test creats a list with the numbers 1 to n then reversing the    #
#   list.  This list created the worst case situation for bubble sort.    #
###########################################################################

def reversed_test(f, start_value, number_of_steps, step_size, filename):
    import random
    f_out = open(filename, "w+")
    for i in range(number_of_steps):
        x = start_value + i * step_size
        ulist = []
        for j in range(x):
            ulist.append(j)
        ulist = ulist[::-1]
        f_out.write(benchmark(f, ulist))
    f_out.close()

def total_reverse_test():
    reversed_test(bsort, 0, 50, 50, "bsortReverseTest.csv")
    reversed_test(merge_sort, 0, 50, 50, "mergeReverseTest.csv")
    reversed_test(selectionsort, 0, 50, 50, "selectionReverseTest.csv")
    reversed_test(insertionsort, 0, 50, 50, "insertionReverseTest.csv")

###########################################################################
#                                Repeated Test                            #
#   This test creats a list with the n copies of 999.  This might create  #
#   bad situations for some sorting algorithms.                           #
###########################################################################

def repeated_test(f, start_value, number_of_steps, step_size, filename):
    import random
    f_out = open(filename, "w+")
    for i in range(number_of_steps):
        x = start_value + i * step_size
        ulist = []
        for j in range(x):
            ulist.append(999)
        f_out.write(benchmark(f, ulist))
    f_out.close()

def total_repeated_test():
    repeated_test(bsort, 0, 50, 50, "bsortRepeatedTest.csv")
    repeated_test(merge_sort, 0, 50, 50, "mergeRepeatedTest.csv")
    repeated_test(selectionsort, 0, 50, 50, "selectionRepeatedTest.csv")
    repeated_test(insertionsort, 0, 50, 50, "insertionRepeatedTest.csv")


#############################################################################
#   Intuitively I thought merge sort is the fastest due to the logarithmic  #
#   structure of dividing the list in half instead of going through the     #
#   whole list. Bubble sort should also take a little longer because it     #
#   switches items more than selection or insertion sorting. Through        #
#   testing this held true, with sorting lists of 2500 items taking about   #
#   .4 seconds with insertion and selection sort, but .01 seconds for merge #
#   sort and 2 seconds for bubble sorting (in some cases). While selection  #
#   and insertion were both faster than bubble sort, all three of them      #
#   still have an exponential growth to them, while merge sort was close to #
#   linear. It is nlog(n), but it's always hard to see the difference.      #
#############################################################################


#############################################################################
#                                   Radix Sort                              #
#   Here is radix sort, which we talked about in class.  It could probably  #
#   look cleaner, but I was having trouble putting theory to practice and   #
#   this worked so I left it.  It definitely has a linear (but probably     #
#   nlog(n)) look of growth in graphs.                                      #
#############################################################################
def radix_sort(list):
    import math
    if len(list) == 0:
        return list
    maxim = max(list)
    mag = math.ceil(math.log(maxim, 10))
    for j in range(mag):
        nlist = []
        #print("Before")
        #print(list)
        div = 10**j
        zeros = []
        ones = []
        twos = []
        threes = []
        fours = []
        fives = []
        sixes = []
        sevens = []
        eights = []
        nines = []
        for i in range(len(list)):
            if (math.floor(list[i]/(div))%10) == 0:
                zeros.append(list[i])
            if (math.floor(list[i]/(div))%10) == 1:
                ones.append(list[i])
            if (math.floor(list[i]/(div))%10) == 2:
                twos.append(list[i])
            if (math.floor(list[i]/(div))%10) == 3:
                threes.append(list[i])
            if (math.floor(list[i]/(div))%10) == 4:
                fours.append(list[i])
            if (math.floor(list[i]/(div))%10) == 5:
                fives.append(list[i])
            if (math.floor(list[i]/(div))%10) == 6:
                sixes.append(list[i])
            if (math.floor(list[i]/(div))%10) == 7:
                sevens.append(list[i])
            if (math.floor(list[i]/(div))%10) == 8:
                eights.append(list[i])
            if (math.floor(list[i]/(div))%10) == 9:
                nines.append(list[i])
        nlist.extend(zeros)
        nlist.extend(ones)
        nlist.extend(twos)
        nlist.extend(threes)
        nlist.extend(fours)
        nlist.extend(fives)
        nlist.extend(sixes)
        nlist.extend(sevens)
        nlist.extend(eights)
        nlist.extend(nines)
        list = nlist
        #print("after")
        #print(list)
    return list



    
