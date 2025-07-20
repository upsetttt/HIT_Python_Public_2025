#bai 3:
x = int(input())
tmp = x
cnt = 0
s = 0
while tmp > 0: 
    cnt += 1
    s += tmp % 10
    tmp //= 10
print("Số chữ số: ", cnt, "Tổng các chữ số: ", s)