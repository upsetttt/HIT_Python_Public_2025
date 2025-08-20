from functools import reduce
def caculate(lc, *args):
    if lc == "add":
        return reduce(lambda a, b : a + b, args) 
    elif lc == "multiply":
        return reduce(lambda a,b : a * b, args)
    elif lc == "max":
        return max(args)
    elif lc == "min":
        return min(args)
    else: return "Invalid operation"
lc = input()
a = list(map(int, input().split()))
b = caculate(lc, *a)
print(b)
