n = int(input())
a =[]
for i in range(n):
    x = int(input())
    a.append(x)
x = int(input())
print(a.count(x))
a[2 : 8] = [8, 5, 4, 0, 1, 3]
print(a)
max = -1e9
min = 1e9
for x in a:
    if(x > max):
        max = x
    if x < min:
        min = x
print(max, min)
y = int(input())
a.insert(0, y)
inc = 1
dec = 1
for i in range(len(a) - 1):
    if(a[i] > a[i + 1]):
        inc = 0
    else:
        if(a[i] < a[i + 1]):
            dec = 0
if inc == 1 : print("tăng")
elif dec == 1: print("giảm")
else:
    print("không tăng không giảm")