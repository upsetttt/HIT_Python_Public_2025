tuple1 = tuple(map(int, input().split()))
ans = []
cnt = 1
for i in range(1, len(tuple1)):
    if(tuple1[i] == tuple1[i - 1]):
        cnt += 1;
    else:
        print(cnt)
        if cnt % 5 == 0 and cnt % 10 != 0:
            ans.append(tuple1[i - 1])
        cnt = 1
if cnt % 5 == 0 and cnt % 10 != 0:
        ans.append(tuple1[i - 1])
print(ans) 

