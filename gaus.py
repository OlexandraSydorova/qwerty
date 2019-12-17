n = int(input())
matrix = []
for i in range(n):
    row = []
    for j in range(n+1):
        row.append(int(input('Введіть елемент: ')))
    matrix.append(row)

print('Задана матриця: ')
for i in range(n):
    print(matrix[i][:n], "|", matrix[i][n])

count_zero = 0
while count_zero < n-1:
    count_row = n - 1
    while count_row-1 >= count_zero:
        count_column = 0
        var1 = matrix[count_row-1][count_zero]
        var2 = matrix[count_row][count_zero]
        while count_column <= n:
            matrix[count_row][count_column] = var1*matrix[count_row][count_column] - var2 * matrix[count_row-1][count_column]
            count_column += 1
        count_row -= 1
    count_zero += 1
for i in range(n):
    print(matrix[i][:n], "|", matrix[i][n])
list_x = []
list_x.append(matrix[n-1][n]/matrix[n-1][n-1])
i = n-2
while i>=0:
    j = i+1
    suma = 0
    while j <= n-1:
        suma+=(-matrix[i][j]*list_x[n-j-1])
        j+=1
    list_x.append((suma+matrix[i][n])/matrix[i][i])
    i-=1
for i in range(n):
    print("X",n-i,list_x[i])