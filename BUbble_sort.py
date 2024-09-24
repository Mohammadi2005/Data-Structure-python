def BubbleSort(arr):
    n = len(arr)
    # for i in range(n):
    for i in range(len(arr) - 1, 0, -1):
        # for j in range(0, n-i-1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print(arr)


number = int(input("Enter a number: "))
array = []
for i in range(0, number):
    adad = int(input(f"Enter a value {i+1} from array: "))
    array.append(adad)
BubbleSort(array)
print(array)