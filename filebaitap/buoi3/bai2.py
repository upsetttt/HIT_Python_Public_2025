k = int(input())
a = []
for i in range(k):
    x = int(input())
    a.append(x)
n = int(input())
m = int(input())
if n * m > k:
    print("Không đủ số lượng")
else:
    tmp = []
    for i in range(n):
        tmp.append(a[i * m : (i + 1) * m])
    print(tmp)
