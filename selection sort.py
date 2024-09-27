import numpy as np
def Selection_Sort_1(array):
    for i in range(len(array) - 1, 0, -1):
        max = array[0]
        maxindex = 0
        for j in range(i+1):
            if array[j] > max:
                max, maxindex = array[j], j
        array[i], array[maxindex] = array[maxindex], array[i]

def Selection_Sort_2(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i+1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        array[min_index], array[i] = array[i], array[min_index]


array = np.random.randint(0, 40, size=10)
print(array)
Selection_Sort_2(array)
print(array)