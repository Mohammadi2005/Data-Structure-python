import numpy as np
def insertion_sort(array):
    for i in range(1, len(array)):
        j = i - 1
        temp = array[i]
        while j >= 0 and temp < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = temp

arr = np.random.randint(1, 100, 10)
print(f"Before storing : {arr}")
insention_sort(arr)
print(f"After storing : {arr}")

