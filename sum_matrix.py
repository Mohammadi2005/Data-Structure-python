def sum_matrix1(array1, array2, row, col):
    array3 = [[0]*col for i in range(row)]
    for i in range(0,row):
        for j in range(0,col):
            array3[i][j] = array1[i][j] + array2[i][j]
    print("sum of the matrixs from function 1 : ")
    for i in range(0,row):
        for j in range(0,col):
            print(array3[i][j],end=" ")
        print()

def sum_matrix2(array1, array2):
    array3 = [[array1[i][j] + array2[i][j] for j in range(len(array1[0]))] for i in range(len(array1))]
    print("sum of the matrixs from function 2 : ")
    print(array3)


row = int(input("Enter the number of rows the matrix : "))
col = int(input("Enter the number of columns for matrix : "))
array_1 = [[0]*col for i in range(row)]
array_2 = [[0]*col for i in range(row)]
print("Start matrix 1 : ")
for i in range(row):
    for j in range(col):
        array_1[i][j] = int(input(f"Enter a number for array_1[{i}][{j}] : "))
print("Start matrix 2 :")
for i in range(row):
    for j in range(col):
        array_2[i][j] = int(input(f"Enter a number for array_2[{i}][{j}] : "))
sum_matrix1(array_1, array_2, row, col)
sum_matrix2(array_1, array_2)







