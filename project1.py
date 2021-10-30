"""
Math 560
Project 1
Fall 2021

Partner 1:
Partner 2:
Date:
"""

"""
SelectionSort
"""




from numpy.core.function_base import _linspace_dispatcher
from numpy.core.numeric import identity
from project1tests import *
def findMin(list, index):
    # input:
    #       list : a list of int
    #       index : a number
    # output:
    #       the index of the min in list[index ...]
    min = index
    for i in range(index+1, len(list)):
        if(list[i] < list[min]):
            min = i
    return min


def swap(list, a, b):
    # input:
    #       list : list of integer
    #       a, b : index for number to be swapped
    # output:
    #       list with swapped number
    temp = list[a]
    list[a] = list[b]
    list[b] = temp
    return


def SelectionSort(listToSort):
    # the list is divided into sorted part and unsorted part
    # continuously find the smallest number in the unsorted part
    # put the smallest number at the end of the sorted array
    for i in range(len(listToSort)):
        # find the minimum in list[i...]
        min = findMin(listToSort, i)
        swap(listToSort, i, min)
    return


"""
InsertionSort
"""


def insert(list, index, j):
    # insert nuber number at j into index
    # implemented using warp

    # warp forward
    while(j > index):
        swap(list, j-1, j)
        j -= 1


def InsertionSort(listToSort):
    # list is divided into sort anf unsorted part,
    # continuous find the smallest number in unsorted part
    # and insert it into the sorted part
    # input :
    #   listToSort : a list of integer
    # output :
    #   a sorted list
    for i in range(len(listToSort)):
        min = findMin(listToSort, i)
        insert(listToSort, i, min)
    return


"""
BubbleSort
"""


def BubbleSort(listToSort):
    # continuously swap the to push the biggest number to the end at each time
    # thus there will be len(listToSort) outer loops
    # each inner loop will go through and swap
    # early stop based on if swap happens in the inner loop

    # input :
    #       listToSort : list of numbers
    # output :
    #       sorted list

    for i in range(len(listToSort)-1):
        sorted = False
        # if sorted is set to true in the inner loop,
        # then no sort needed, return
        if(sorted):
            return
        for j in range(0, len(listToSort) - 1 - i):
            # flag used to check if swap happened in the inner looop
            hasSwap = False
            # swap continuously
            if(listToSort[j] > listToSort[j+1]):
                swap(listToSort, j, j+1)
                hasSwap = True
            # if swap does not happen, then set sorted to true
            if(hasSwap == False):
                sorted = True
    return


"""
MergeSort
"""


def MergeSortHelp(list, holder, left, right):
    # return the sorted list for list[left:right]

    # base case: only one one element
    if(right - left == 0):
        return
    # else split the array into two half
    mid = (left+right)//2
    # sort the left and right splited array
    MergeSortHelp(list, holder, left, mid)
    MergeSortHelp(list, holder, mid+1, right)

    # merge the left part and right part together

    # push the left and right into the place holder
    i = left
    j = mid + 1
    index = 0
    while(i <= mid and j <= right):
        # compare the two value, smaller one goes into the holder
        if(list[i] <= list[j]):
            holder[index] = list[i]
            i += 1
        else:
            holder[index] = list[j]
            j += 1

        index += 1
    # left part or right part may have some remain
    while(i <= mid or j <= right):
        # left has remain
        if(i <= mid):
            holder[index] = list[i]
            i += 1
        # right has
        else:
            holder[index] = list[j]
            j += 1
        index += 1
    # reassign the value to list
    index = 0
    for i in range(left, right+1):
        list[i] = holder[index]
        index += 1
    return


def MergeSort(listToSort):
    # split the list into two half list
    # sort each list accordingly
    # then merge the two sorted array into one array

    # we need a helper function

    # create preholder to hold the list
    holder = [None] * len(listToSort)

    MergeSortHelp(listToSort, holder, 0, len(listToSort)-1)

    return


"""
QuickSort

Sort a list with the call QuickSort(listToSort),
or additionally specify i and j.
"""

# input :
#   list : with numbers
#   lo : low index
#   high : high index
# output :
#   return the index of the pivot
#   in the left of pivot elements is smaller than or equal to the pivot
#   in the right of the pivot, elements are greater than the pivot


def lomutoPartition(list, lo, hi):
    # we want list[lo...i] contains the number that is smaller or equal than the pivot
    # i is from lo to hi - 1
    # high element holds the pivot
    pivot = list[hi]
    i = lo - 1
    for j in range(lo, hi):
        if(list[j] <= pivot):
            # we find a element that is smaller than pivot
            # put it into the list[lo..i]
            i += 1
            swap(list, i, j)
    # lastly we get list[lo...i] <= pivot and one pivot at list[hi]
    i += 1
    swap(list, i, hi)
    return i


def QuickSortHelperLomuto(listToSort, i, j):
    # base case
    if(i >= j):
        return
    # partition the array
    pivot = lomutoPartition(listToSort, i, j)

    QuickSortHelperLomuto(listToSort, i, pivot-1)
    QuickSortHelperLomuto(listToSort, pivot+1, j)

    return


def hoarePartiton(list, lo, hi):
    # invariant :
    # after each swap :  list[0...left] <= pivot
    #                    list[right..hi] >= pivot

    # after the final loop
    #       list[right] <= pivot
    #       list[right + 1...hi] >= pivot
    #       and list[0...left-1] <= pivot
    #       right <= left

    # we can not set the list[hi] as pivto, which will cause infinite loop
    pivot = list[lo]
    left = lo - 1
    right = hi + 1
    while(True):

        # find the first element in the left that is greater than or equal to the pivot
        while(True):
            left += 1
            if(list[left] >= pivot):
                break
        # find the first element in the right that is smaller than or equal to the pivot
        while(True):
            right -= 1
            if(list[right] <= pivot):
                break

        # left < right, then we should swap, becase it is the wrong order
        # else return
        if(left < right):
            swap(list, left, right)
        else:
            return right


def QuickSortHelperHoare(list, lo, hi):
    if(lo >= hi):
        return
    pivot = hoarePartiton(list, lo, hi)
    QuickSortHelperHoare(list, lo, pivot)
    QuickSortHelperHoare(list, pivot+1, hi)

    return


def QuickSort(listToSort, i=0, j=None):
    if(j == None):
        j = len(listToSort)-1
    else:
        j -= 1
    # QuickSortHelperLomuto(listToSort, i, j)
    QuickSortHelperLomuto(listToSort, i, j)

    return


"""
Importing the testing code after function defs to ensure same references.
"""

"""
Main function.
"""
if __name__ == "__main__":
    print('Testing Selection Sort')
    print()
    testingSuite(SelectionSort)
    print()
    print('Testing Insertion Sort')
    print()
    testingSuite(InsertionSort)
    print()
    print('Testing Bubble Sort')
    print()
    testingSuite(BubbleSort)
    print()
    print('Testing Merge Sort')
    print()
    testingSuite(MergeSort)
    print()
    print('Testing Quick Sort')
    print()
    testingSuite(QuickSort)
    print()
    print('UNSORTED measureTime')
    print()
    measureTime()
    print()
    print('SORTED measureTime')
    print()
    measureTime(True)
