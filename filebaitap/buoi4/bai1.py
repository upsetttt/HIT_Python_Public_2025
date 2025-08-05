n = int(input())
set1 = set()
for i in range(n):
    set1.add(str(input()))
set1 = list(set1)
for i in range(n):
    set1[i] = int(set1[i])
set1 = tuple(set1)
s = 0
for x in set1:
    s += x
s /= len(set1)
print(s)