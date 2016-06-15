import re


n,m = (int(i) for i in input().split(" "))
matrix = []
for i in range(n):
    a = [] # промежуточная массив для добавления
    x = input()
    for j in range(m):
        a.append (x[j])
    matrix.append(a)
ans = ""
print (matrix[0][2])
print (matrix[1][2])
for i in range(0,m):
    for j in range(0,n):
        try:
            ans = ans + matrix[n][m]
        except IndexError:
            continue
print (ans)
