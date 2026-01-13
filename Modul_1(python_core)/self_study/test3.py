abscissas = input().split()
ordinates = input().split()
applicates = input().split()
R = 4
result = []
for i,k,j in zip(abscissas,ordinates,applicates):
    result.append(float(i) ** 2 + float(k) ** 2 + float(j) ** 2 < R)
if all(result):
    print(True)
else:
    print(False)