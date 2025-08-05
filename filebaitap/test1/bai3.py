n = int(input())
a = list(map(int, input().split()))
ans = 100000001
for i in a:
    if(a.count(i + 1) == 0):
        ans = min(ans, i + 1)
print(ans)
