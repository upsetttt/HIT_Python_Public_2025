# bai 2:
sal = int(input("Nhập số nguyên dương: "))
if sal >= 15000000:
    x = 0.3
elif sal >= 7000000:
    x = 0.2
else:
    x = 0.1
print("Thuế : ", int(sal * x) , "Thu nhập: ", int(sal - (sal * x)))