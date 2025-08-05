a = list(map(str, input().split()))
ans = []
for x in a:
    for i in x:
        if ans.count(i) == 0:
            ans.append(i)
print(ans)