s1 = str(input())
s2 = str(input())
tmp =""
for i in range(len(s1) - 1 , -1, -1):
    tmp += s1[i]
print(tmp)
a = int(input())
b = int(input())
s5 = s2[: a-1] + s2[a - 1 : b][::-1] + s2[b:]
print(s5)
s3 =""
for i in range(len(s1)):
    if i % 2 != 0:
        s3 += s1[i]
print(s3)
s4 = ""
for i in range(max(len(s1), len(s2))):
    if(i < len(s1)):
        s4 += s1[i]
    if(i < len(s2)):
        s4 += s2[i]
print(s4)       


