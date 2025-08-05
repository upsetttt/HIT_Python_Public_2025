n = int(input())
m = int(input())
set1 = set()
set2 = set()
for i in range(n):
    set1.add(str(input()))
for i in range(m):
    set2.add(str(input()))
ans1 = set1.intersection(set2)
if(len(ans1) == 0):
    print("không")
else:
    print("có")
ans2 = set1.union(set2)
print(ans2)
ans3 = set1.difference(set2)
if(len(ans3) == 0):
    print("không có")
else:
    print(ans3)