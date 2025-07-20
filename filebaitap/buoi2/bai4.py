# bai 4:
x = int(input())
COST = 28
cnt = 0;
while x >= COST:
    cnt += 1
    x -= COST
cnt += cnt // 3
print(cnt)