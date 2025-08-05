a = list(map(str, input().split()))
t1 = tuple(a)
print(t1)
ans = 0
for x in t1:
    check = True
    for k in x:
        if k < '0' or k > '9':
            check = False
    if check == True:
        ans += 1
print(ans)     
