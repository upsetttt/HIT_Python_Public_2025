def rever(a, n, m):
    b = [[0]  * n for i in range(m)]
    for i in range(n):
        for j in range(m):
            b[j][i] = a[i][j]
    print(b)
n, m = map(int, input().split())
a = []
for i in range(n):
    row = list(map(int, input().split()))
    a.append(row)
rever(a, n, m)
print("và mảng ban đầu là :")
print(a)