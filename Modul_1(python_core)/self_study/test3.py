# n = int(input())
# m = int(input())
# matrix = []
# for i in range(n):
#     row = []
#     for j in range(m):
#         row.append(i * j)
#     matrix.append(row)
n = 3
m = 4
matrix = [[0,3,2,4],[2,3,5,5],[5,1,2,3]]
bol = matrix[0][0]
sr = 0
st = 0
for i in range(n):
    for j in range(m):
        if matrix[i][j] > bol:
            sr = i
            st = j
            bol = matrix[i][j]

1`print(sr, st)
