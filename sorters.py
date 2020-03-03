# Parameters in the following functions:
#   data: a list of tuples
#   index: the tuple index to sort by
#
# Consider the following example data:
#   data = [
#       ( 'homer', 'simpson', 50 ),
#       ( 'luke', 'skywalker', 87 ),
#       ( 'bilbo', 'baggins', 111 ),
#   ]
#
#   bubble_sort(data, 0) sorts on first name (a..z)
#   bubble_sort(data, 0, True) sorts on first name (z..a)
#   bubble_sort(data, 2) sorts on age (1..infinity)
#
# The data list is sorted in place (anew list is not created).
# You do NOT need to perform validation on input data
# (null data list, index out of bounds, etc.)
#


def bubble_sort(data, index, descending=False):
    '''Sorts using the bubble sort algorithm'''
    # replace this with your own algorithm (do not use Python's sort)
    for item in range(len(data)-1,0,-1):
        for i in range(item):
            if descending == False:
                if data[i][index]>data[i+1][index]:
                    temp = data[i]
                    data[i]=data[i+1]
                    data[i+1]=temp
            else:
                if data[i][index]<data[i+1][index]:
                    temp = data[i]
                    data[i]=data[i+1]
                    data[i+1]=temp
    
    #data.sort(key=lambda t: t[index], reverse=descending)


def insertion_sort(data, index, descending=False):
    '''Sorts using the insertion sort algorithm'''
    # replace this with your own algorithm (do not use Python's sort)
    for item in range(1,len(data)):

        position = item
        currentValue = data[item]
        if descending == True:
            while position > 0 and data[position-1][index]<currentValue[index]:
                data[position]=data[position-1]
                position=position-1
        else:
            while position>0 and data[position-1][index]>currentValue[index]:
                data[position]=data[position-1]
                position=position-1
        
        data[position]=currentValue


def selection_sort(data, index, descending=False):
    '''Sorts using the selection sort algorithm'''
    # replace this with your own algorithm (do not use Python's sort)
    for item in range(len(data)-1,0,-1):
        maxposition=0
        for i in range(1,item+1):
            if descending == False:
                if data[i][index]>data[maxposition][index]:
                    maxposition=i
            else:
                if data[i][index]<data[maxposition][index]:
                    maxposition=i
        temp=data[item]
        data[item]=data[maxposition]
        data[maxposition]=temp

# data = [
#     ( 'bilbo', 'baggins', 111 ),
#     ( 'homer', 'simpson', 50 ),
#     ( 'luke', 'skywalker', 87 ),
#     ( 'frodo', 'baggins', 100 ),
# ]

# selection_sort(data,2)
# print(data)
# bubble_sort(data,0,True)
# print(data)
# insertion_sort(data,1)
# print(data)